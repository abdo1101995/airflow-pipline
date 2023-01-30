import datetime

from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator

default_args = {
    'owner': 'udacity',
    'start_date':datetime.datetime.now()
}

dag = DAG('create_dag',
          default_args=default_args,
          description='Create tables to load data in fact and dimension tables'

        )
drop_tables=PostgresOperator(
    task_id="drop",
    dag=dag,
    postgres_conn_id="redshift",
    sql="drop_tables.sql"
)
create_tables=PostgresOperator(
    task_id="create_tables",
    dag=dag,
    postgres_conn_id="redshift",
    sql="create_tables.sql"
)

drop_tables>>create_tables
