from mysolr import Solr
import os, sys, requests, json, time, argparse


def atomicUpdate(chunkFile, solrURL):

    session = requests.Session()
    solr = Solr(solrURL, make_request=session, version=4)

    bufferDocs = []

    with open(chunkFile, 'r') as inF:
        for docID in inF:
            docID = docID.strip()

            delta_update = { "id": docID,
                              "dataSource_s_md": "google"} ## Caution change this value

            bufferDocs.append(delta_update)


    x = solr.update(bufferDocs, commit=True)

    if x.raw_content['responseHeader']['status'] != 0:
        print "Solr Commit Failed !!!! Error Status code: ", x.raw_content['responseHeader']['status']
    else:
        print "Awesome!! Solr Commit was a Success"




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="DHS Atomic Update")
    parser.add_argument('-f', '--file', required=True, help='path to file/Chunk containing Image IDs')
    parser.add_argument('--solrURL', required=True, help='Solr Core URL')
    args = parser.parse_args()

    if args.file and args.solrURL:
        atomicUpdate(args.file, args.solrURL)
