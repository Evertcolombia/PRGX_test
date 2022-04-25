# PRGX_test

## Backend Requirements

* Docker
* Docker Compose

## Build PRogram

- The follow command will install and prepare the environment for the program

    ```
        $ docker-compose build
    ```

## Start Program

- The follow command will startup the program

    ```
        $ docker-compose up -d
    ```

# Source PDF Files

- the files to thes the program are in the path --> /app/src/filename  use this file to exec the POST endpoint

## Test the API with Swagger UI

- IF want to review automatic documentation provided by Swagger UI go to follow path

* [Documentation] (http://localhost:8000/docs)

- on Swagger can test the endpoints list that are:
    
    * POST -> /extracts -> will extract data from a pdf file, based on doc_path query parameter, the doc_path must be "/app/src/filename". see files names in /app/src folder
    * EXAMPLE: doc_path = /app/src/Doc2.pdf
  

    * GET -> /db_data  -> Will get a list of the inserted rows on the table base on table_name query parameter, tha table name to use is "extractions"
    * EXAMPLE: table_name = extractions

## TEST the API with Curl

- Is also possibly test the api with curl

    * POST: 
    ```
        $ curl -X 'POST' 'http://localhost:8000/api/v1/extract?doc_path=%2Fapp%2Fsrc%2FDoc2.pdf' \
            -H 'accept: application/json' \
            -d ''
    ```
    
    * GET
    ```
        $ curl -X 'GET' 'http://localhost:8000/api/v1/db_data?table_name=extractions' \
            -H 'accept: application/json'
    ```


### Run TESTS

- If need run the tests execute the follow command

    ```
        $ docker-compose exec backend pytest
    ```


## Live program running

- Can review the program running in the next urls

    * [Documentation] (http://35.223.102.245:8000/docs)
    * [test_from_browser] (http://35.223.102.245:8000/api/v1/db_data?table_name=extractions)
