#!/bin/sh
python solr_similarity.py --file chunks/doc_ids_0.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit
python solr_similarity.py --file chunks/doc_ids_500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit
python solr_similarity.py --file chunks/doc_ids_1000000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit
python solr_similarity.py --file chunks/doc_ids_1500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit
python solr_similarity.py --file chunks/doc_ids_2000000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit  
python solr_similarity.py --file chunks/doc_ids_2500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit
python solr_similarity.py --file chunks/doc_ids_3000000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit