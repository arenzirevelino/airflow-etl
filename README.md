# airflow-etl on local

Hi, I try to learn re-create Airflow ETL on my local and using this repo for my documentation of learning step-by-step.

## I am using:
1. Python 3.9
2. Apache Airflow
3. pipenv for virtual environment

## step-by-step
1. create project directory `mkdir airflow-etl` and then go to the folder `cd airflow-etl`
2. install the some of library using `pipenv` -> `pipenv install --python 3.9` and `pipenv install apache-airflow`
3. after that, set home for airflow in a root of your project (specified in .env file)
  `echo "AIRFLOW_HOME=${PWD}/airflow" >> .env`
4. running your virtual env using `pipenv shell`. If you want to run airflow webserver you have to run your virtual env first.
5. Initialize airflow -> `airflow db init`. Try `airflow dags list` to see some dags example.
6. after that, create dags directory on airflow_home directory --> `mkdir ${AIRFLOW_HOME}/dags/`
7. setup the `.env` file to set `${AIRFLOW_HOME}/dags` as `dags_floder`, you can change into different location for `dags_floder` by change the configuration on `.env` file.
    `echo "AIRFLOW__CORE__DAGS_FOLDER=${AIRFLOW_HOME}/dags" >> .env`.
    so this is my folder structure:
    ```
    my_project
    ├── airflow
    │   ├── airflow.cfg
    │   ├── airflow.db
    |   ├── airflow-webserver.pid
    |   ├── webserver_config.py
    │   ├── dags
    │   └── logs
    │      └── scheduler 
    ├── .env
    ├── Pipfile
    └── Pipfile.lock      
    ```                  
8. create user airflow 
    ```
    airflow users create \ 
    --username [your username to login] \ 
    --firstname [your first name] \ 
    --lastname [your lastname] \ 
    --role Admin \ 
    --email [your email]
    ```
9. try to run on different terminal window `airflow webserver --port 8080` to check airflow webserver can running on your `localhost:8080`
10. in here, I am using sample db from [Chinook DB](https://www.sqlitetutorial.net/sqlite-sample-database/) for trial extract some data from result SQL to CSV end load into a table.


**This is my first time making something like this, so I apologize if there are many shortcomings**

Reference:
https://github.com/arizalsandi/etl-local-airflow