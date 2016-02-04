#!/bin/sh
python solr_similarity.py --file chunks/doc_ids_0.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &
python solr_similarity.py --file chunks/doc_ids_500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &
python solr_similarity.py --file chunks/doc_ids_1000000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &
python solr_similarity.py --file chunks/doc_ids_1500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &
sleep 10
python solr_similarity.py --file chunks/doc_ids_2000000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &
python solr_similarity.py --file chunks/doc_ids_2500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &
python solr_similarity.py --file chunks/doc_ids_3000000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &
python solr_similarity.py --file chunks/doc_ids_3500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &
wait
python solr_similarity.py --file chunks/doc_ids_4000000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &
python solr_similarity.py --file chunks/doc_ids_4500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &
python solr_similarity.py --file chunks/doc_ids_5000000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &
sleep 10
python solr_similarity.py --file chunks/doc_ids_5500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &
python solr_similarity.py --file chunks/doc_ids_6000000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &
python solr_similarity.py --file chunks/doc_ids_6500000.txt --solrURL http://localhost:8983/solr/imagecatdev --type http --commit &