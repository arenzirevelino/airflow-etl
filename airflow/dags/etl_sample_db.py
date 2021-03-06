import os
import sqlite3
import pandas as pd
from sqlalchemy import create_engine
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

DATA_SOURCE = str(os.path.abspath('../'+'airflow-etl/sample_data/chinook.db'))
DATABASE_LOCATION = str(os.path.abspath('../'+'airflow-etl/sample_data/chinook_invoice_by_sales.sqlite'))
CSV_OUTPUT = str(os.path.abspath('../'+'airflow-etl/sample_data/chinook_invoice_csv.csv'))
SQL_QUERY = str(os.path.abspath('../'+'airflow-etl/sample_data/invoice_by_sales.sql'))

default_args = {
	'owner':'renzi',
	'email':'renzivelino@gmail.com',
	'email_on_failure':True,
	}

dag = 	DAG(
	'etl_sample_db',
	default_args = default_args,
	schedule_interval = None,
	start_date = days_ago(1),
	)

def extract_transform(**kwargs):
	ti = kwargs['ti']
	output_csv = CSV_OUTPUT

	conn1 = sqlite3.connect(DATA_SOURCE)
	with open(SQL_QUERY, "r") as sql_query:
		df = pd.read_sql(sql_query.read(), conn1)

		df.to_csv(output_csv, index=False)
		ti.xcom_push('chinook', output_csv)


def load(**kwargs):
	ti = kwargs['ti']
	input_csv = ti.xcom_pull(task_ids='extract_transform', key='chinook')
	conn2 = sqlite3.connect(DATABASE_LOCATION)

	df = pd.read_csv(input_csv)
	df.to_sql('chinook_invoice_by_sales', conn2, index=False, if_exists='replace')


start 		= DummyOperator(
			task_id='start',
			dag = dag)

end			= DummyOperator(
			task_id='end',
			dag = dag)

extract_transform_task	= PythonOperator(task_id='extract_transform',
			python_callable = extract_transform,
			dag = dag)

load_task	= PythonOperator(task_id='load',
			python_callable = load,
			dag = dag)

start >> extract_transform_task >> load_task >> end
	
	
	
