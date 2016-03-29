from __future__ import print_function
def main():

    inF = open('solrDocIDs_no_spaces/superIDs', 'r')
    superSet = set(inF.readlines())

    inF = open('solrDocIDs_no_spaces/onlyDHS_ids', 'r')
    googleSet = set(inF.readlines())

    #prefix = "file:/data/dhs/ice_ctceu_related_images"

    dhs_set = superSet - googleSet 

    with open('google__ids', 'w') as outF:
        for docID in dhs_set:
            if "DS_Store" not in docID:
                print(docID, file=outF, end='')
                #print(prefix+docID.lstrip('.'), file=outF, end='')
  

if __name__ == "__main__":
    main()
