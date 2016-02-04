#!/bin/sh
python solr_similarity.py --file chunks/doc_ids_3500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit
python solr_similarity.py --file chunks/doc_ids_4000000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit
python solr_similarity.py --file chunks/doc_ids_4500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit
python solr_similarity.py --file chunks/doc_ids_5000000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit
python solr_similarity.py --file chunks/doc_ids_5500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit
python solr_similarity.py --file chunks/doc_ids_6000000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit
python solr_similarity.py --file chunks/doc_ids_6500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit