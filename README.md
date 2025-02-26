# Banking Transactions application
## Some considerations
1. I have not give this project any identifiable name, so please do not judge me on that.
2. I have added only the GET and POST calls for now and added comments for DELETE and PUT for future implimentations.
3. I have used SQLITE as DB for this project.
4. Using FastAPI and UVICRON for creating the RestFul APIs.
5. Used SqlAlchemy for ORM.
6. It took me 5 hours to setup: VSCode, Git bash, SSH key, Project, Dockerisation, Documentation.

## Setup
1. Clone this repository in you system using git clone `git clone git@github.com:pranaybankar/backend_dev.git`.
2. Make sure Docker is running on your laptop.
3. Go inside peoject and run this command `docker-compose up --build` in `git bash` or `Terminal` to build this project. FastAPI will take some time to run the project.
4. Please click this [link](http://127.0.0.1:8000/) to access the project UI. And follow the instructions.

## Play Around
1. When you are at the the [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs), you will see 2 APIs, GET and POST. <img width="927" alt="image" src="https://github.com/user-attachments/assets/266f1c72-51b5-4b6e-8e80-25c48455753d">

2. To try them click on anyone and click on the `Try it out!` button. <img width="929" alt="image" src="https://github.com/user-attachments/assets/b068b15a-4349-4883-8e65-5a10355dba94">

3. To execute the GET API click the blue `Execute` button.

4. To execute the POST API upload the json file first. You can use the json files from the project or upload your files. Then click the blue `Execute` button. <img width="928" alt="image" src="https://github.com/user-attachments/assets/3fc1aedb-9fe0-43ad-836c-8872dc1350cf">

## What to Expect
1. In POST call: If you provide the json as per the provided assesment pdf format you will see the JSON after the POST API call. If you upload any file with wrong input you will get to see the error in Response body. <img width="692" alt="image" src="https://github.com/user-attachments/assets/c4634c43-7761-434f-9958-a920402591b4">

4. In GET call: You will see the saved data as JSON.

## File usage
1. In the app folder, the `application.py` file is the entry point for the Rest API. This file has the Restful APIs defained.2. 
3. The `db_handler.py` file handles the connection to the Database. I have setup the `DATABASE_URL` in `docker-compose.yaml` file.
4. The `model.py` file has the `db_handlers` `declarative_base` model which connects the DB with python code. I have added the table name and columns in this file's class.
5. The `schema.py` file is a collection of database objects that are logically grouped together.
6. The `crud.py` have methods for CRUD operation.

