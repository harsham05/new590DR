#for small Solr Cores, use Luke
#for large Solr Cores, use rows=0to50000

from __future__ import print_function
import json, requests, sys, os

def main():

    solrCoreURL = sys.argv[1]       # http://imagecat.dyndns.org/solr/dhsnewimagecatdev
    solrCoreURL = solrCoreURL.split("://")[-1].rstrip('/')

    lukeURL = "http://" + os.environ["SOLR_SIM_USER"]+":"+os.environ["SOLR_SIM_PASS"]+ "@" + solrCoreURL + "/admin/luke?fl=id&numTerms=1000&wt=json"

    

    try:
        lukeResponse = requests.get(lukeURL)
        pprint(lukeResponse)

    except:
        print "Invalid Solr Core URL"



if __name__ == "__main__":
    main()
