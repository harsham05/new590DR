#for small Solr Cores, use Luke
#for large Solr Cores, use rows=0to50000

from __future__ import print_function
from pprint import pprint
import json, requests, sys, os, argparse

def main():

    parser = argparse.ArgumentParser(description="fetch all document ids efficiently from Solr index")
    parser.add_argument('--solrURL', required=True, help="Solr Core URL")    
    parser.add_argument('--outFile', required=True, help="text file containing doc IDs")
    args = parser.parse_args()

    if args.solrURL and args.outFile:              # http://imagecat.dyndns.org/solr/dhsnewimagecatdev        
        with open(args.outFile, 'w') as outF:

            lukeURL = "http://" + os.environ["SOLR_SIM_USER"]+":"+os.environ["SOLR_SIM_PASS"]+ "@" + args.solrURL.split("://")[-1].rstrip('/') + "/admin/luke?fl=id&numTerms=1000&wt=json"            
            
            try:
                lukeResponse = requests.get(lukeURL, verify=False).json()
            
                topTerms = lukeResponse["fields"]["id"]["topTerms"]

                i=0
                while i < len(topTerms):
                    print(topTerms[i], file=outF)
                    i+=2

                

            except Exception as e:
                print(e)
            





if __name__ == "__main__":
    main()
