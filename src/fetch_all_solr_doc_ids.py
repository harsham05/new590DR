#for small Solr Cores, use Luke
#for large Solr Cores, use rows=0to50000

from __future__ import print_function
from pprint import pprint
import json, requests, sys, os, argparse


def lukeHandler(solrURL, outF):
    
    lukeURL = "http://" + os.environ["SOLR_SIM_USER"]+":"+os.environ["SOLR_SIM_PASS"]+ "@" + solrURL.split("://")[-1].rstrip('/') + "/admin/luke?fl=id&numTerms=7120000&wt=json"
    #print(lukeURL)
    try:
        lukeResponse = requests.get(lukeURL, verify=False).json()        
        topTerms = lukeResponse["fields"]["id"]["topTerms"]

        i=0
        while i < len(topTerms):
            print(topTerms[i], file=outF)
            i+=2

    except Exception as e:
        print(e)
        

def solrHandler(solrURL, outF, startRow):

    solrURL = "http://{0}:{1}@{2}/select?q=*:*&fl=id&start={3}&rows=500000&wt=json".format(os.environ["SOLR_SIM_USER"], os.environ["SOLR_SIM_PASS"], solrURL.split("://")[-1].rstrip('/'), startRow)

    #print(solrURL)

    solrResponse = requests.get(solrURL, verify=False).json()

    if solrResponse['responseHeader']['status'] == 0:
        for document in solrResponse['response']['docs']:
            print(document["id"], file=outF)
    



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="fetch all document ids efficiently from Solr index")
    parser.add_argument('--solrURL', required=True, help="Solr Core URL")    
    #parser.add_argument('--outFile', required=True, help="text file containing doc IDs")       and args.outFile 
    parser.add_argument('--startRow', required=True, help="start index, 0, 500000, 1000000, etc")
    args = parser.parse_args()

    if args.solrURL and args.startRow:              # http://imagecat.dyndns.org/solr/dhsnewimagecatdev        
        
        outStr = "doc_ids_{0}.txt".format(args.startRow)
        with open(outStr, 'w') as outF:
            solrHandler(args.solrURL, outF, args.startRow)