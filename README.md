
## Solr Metadata Similarity

### Dependencies

1. Build from source [mysolr 0.8.3](https://github.com/RedTuna/mysolr)


2. Set the Solr REST Endpoint credentials as environment variables in ~/.bashrc

    ```
    export SOLR_SIM_USER=""
    export SOLR_SIM_PASS=""
    ```

3. Define static field in Solr Schema

    ```
    <field name="metadataSimilarityScore_d_md" type="float" default="0.0" indexed="true" stored="true" multiValued="false"/>  
    ```

### Usage

```
usage: solr_similarity.py [-h] -f FILE --solrURL SOLRURL [--commit] [--outputDir OUTPUTDIR]

-f FILE, --file FILE    path to file/Chunk containing Image IDs (one Image ID per line)

--solrURL SOLRURL       Solr Core localhost URL or Solr Core REST endpoint, **Please include complete URL like below**
                        Eg: https://localhost:8983/solr/core1
  
--commit                Include *commit Flag option* to commit calculated metadata similarity scores to Solr Index
  
--outputDir OUTPUTDIR   path to Output Directory to store updated JSON Solr Response documents if commit is not required

```




### License

This project is licensed under the [Apache License, version 2.0](http://www.apache.org/licenses/LICENSE-2.0).



