#!/usr/bin/env python2.7
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

from pprint import pprint
import os, sys, requests, json, time, argparse
from mysolr import Solr
'''
    Calculates Metadata similarity scores for Chunked Image IDs/files & updates them as dynamic fields into Solr Index
    i.e script just iterates through each distinct Chunked File containing Image IDs
    **can be parallelized through multiple Python processes by leveraging chunked files**
    chunked File size determines the buffer size before commit is performed
'''
def compute_scores(chunkFile, solr, union_feature_names, commitFlag, outputDir):

    total_num_features = len(union_feature_names)
    resemblance_scores = {}                             
    query_Error = {}
    bufferDocs = []
    
    with open(chunkFile, 'r') as inF:
        for docID in inF:
            docID = docID.strip()
            response = solr.search(q='id:"{0}"'.format(docID))

            if response.raw_content['responseHeader']['status'] == 0:                       #query returned no errors

                document = response.documents[0]
                if document["id"] == docID:                                                 #Solr query is a successful match
                    overlap = {}
                    overlap = set(document.keys()) & set(union_feature_names)

                    resemblance_scores[document["id"]] = float(len(overlap))/total_num_features
                    
                    document["metadataSimilarityScore_f_md"] = float(len(overlap))/total_num_features      # perform update here
                    
                    if commitFlag:     #buffer docs to be committed at the end
                        bufferDocs.append(document)
                        
                    else:
                        if outputDir:
                            docName = document["id"].split("/")[-1].split(".")[0]                       #parse to obtain only filename
                            updatedFile = os.path.abspath(outputDir) + '/' + docName + ".json"
                            with open(updatedFile, 'w') as tempF:
                                json.dump(document, tempF, indent=4, sort_keys=True, separators=(',', ': '))

                        else:
                            sys.exit("\n\tUsage Error: please enter a output Directory\n")
            else:
                query_Error[docID] = response.raw_content['responseHeader']['status']

    print "Successful Solr Core queries:\t", len(resemblance_scores)

    if len(query_Error) > 0:
        print "Failed Solr Core queries, Documents IDs along with status codes:"
        pprint(query_Error, width=1)

    if commitFlag:                          #perform commit in the end
        atomic_docs = []
        for document in bufferDocs:
        
            doc_id_score = {"id": document["id"],
                            "metadataSimilarityScore_f_md" : {"set" : document["metadataSimilarityScore_f_md"]}
            }
            atomic_docs.append(doc_id_score)

        x = solr.update(atomic_docs, commit=True)

        if x.raw_content['responseHeader']['status'] != 0:
            print "Solr Commit Failed !!!! Error Status code: ", x.raw_content['responseHeader']['status']
        else:
            print "Awesome!! Solr Commit was a Success"
        
    #pprint(resemblance_scores)

def solr_similarity(chunkFile, solrURL, httpType, commitFlag, outputDir):

    lukeURL = "{0}://{1}:{2}@{3}/admin/luke?numTerms=0&wt=json".format(httpType, os.environ["SOLR_SIM_USER"], os.environ["SOLR_SIM_PASS"], solrURL.split("://")[-1].rstrip('/'))    

    try:  #validating luke in turn validates solrURL
        solr_metadata_dump = requests.get(lukeURL).json()
    except:
        print "\n\tUsage Error: please enter a Valid solrURL in the below format"
        print "\tEg: {0}://localhost:8983/solr/core1\n".format(httpType)
        sys.exit()

    union_feature_names = set(solr_metadata_dump["fields"].keys())

    session = requests.Session()
    session.auth = (os.environ["SOLR_SIM_USER"], os.environ["SOLR_SIM_PASS"])
    solr = Solr(solrURL, make_request=session, version=4)

    try:        
        compute_scores(chunkFile, solr, union_feature_names, commitFlag, outputDir)
    except SystemExit as e:
        print e, "terminating..........."        #print "\nError: not a valid file, please check if file exists"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Jaccard Solr Metadata Similarity')
    parser.add_argument('-f', '--file', required=True, help='path to file/Chunk containing Image IDs')
    parser.add_argument('--solrURL', required=True, help='Solr Core localhost complete URL or Solr Core REST endpoint')
    parser.add_argument('--type', required=True, help='http or https')
    parser.add_argument('--commit', action='store_true', help='Include *commit Flag option* to commit calculated metadata similarity scores to Solr Index')
    parser.add_argument('--outputDir', help='Output Directory Path to store updated JSON Solr Response documents if commit is not required')
    args = parser.parse_args()

    if args.file and args.solrURL and args.type:
        solr_similarity(args.file, args.solrURL, args.type, args.commit, args.outputDir)