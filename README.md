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


## Test the API

- IF want to review automatic documentation provided by Swagger UI go to follow path

* [Documentation] (http://localhost:8000/docs)

- on Swagger can test the endpoints list that are:
    
    * POST -> /extracts -> will extract data from a pdf file, based on doc_path query parameter

    * GET -> /db_data  -> Will get a list of the inserted rows on the table base on table_name query parameter


### Run TESTS

- If need run the tests execute the follow command

    ```
        $ docker-compose exec backend pytest
    ```


## Live program running

- Can review the program running in the next urls

    * [Documentation] (http://:8000/docs)
    * [test_from_browser] (http://:8000/ap1/v1/extract?doc_path=/app/src/Doc2.pdf) or (http://:8000/ap1/v1/db_data?table_name=extractions)