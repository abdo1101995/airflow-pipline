from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries

# AWS_KEY = os.environ.get('AWS_KEY')
# AWS_SECRET = os.environ.get('AWS_SECRET')

default_args = {
    'owner': 'udacity',
    'start_date': datetime(2018, 11, 1),
    'catchup': False,
    'email_on_retry': False,
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('udac_example_dag',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
          end_date=datetime(2018, 11, 5),
          schedule_interval='0 * * * *'
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)




stage_events_to_redshift = StageToRedshiftOperator(
    task_id='Stage_events',
    dag=dag,
    red_shift_conn="redshift",
    aws_credential="aws_credentials",
    table="staging_events",
    s3_key="log_data/{execution_date.year}/{execution_date.month}/",
    s_bucket="udacity-dend",
    region="us-west-2",
    json_path="s3://udacity-dend/log_json_path.json",
     provide_context=True
    
)

stage_songs_to_redshift = StageToRedshiftOperator(
    task_id='Stage_songs',
    dag=dag,
    red_shift_conn="redshift",
    aws_credential="aws_credentials",
    table="staging_songs",
    s3_key="song_data/A/A/A",
    s_bucket="udacity-dend",
    region="us-west-2",
    json_path="auto"
)

load_songplays_table = LoadFactOperator(
    task_id='Load_songplays_fact_table',
    dag=dag,
    red_shift_conn="redshift",
    table="songplays",
    sql_help=SqlQueries.songplay_table_insert
)

load_user_dimension_table = LoadDimensionOperator(
    task_id='Load_user_dim_table',
    dag=dag,
    red_shift_conn="redshift",
    table="users",
    sql_help=SqlQueries.user_table_insert 
    
    
)

load_song_dimension_table = LoadDimensionOperator(
    task_id='Load_song_dim_table',
    dag=dag,
    red_shift_conn="redshift",
    table="songs",
    sql_help=SqlQueries.song_table_insert
)

load_artist_dimension_table = LoadDimensionOperator(
    task_id='Load_artist_dim_table',
    dag=dag,
    red_shift_conn="redshift",
    table="artists",
    sql_help=SqlQueries.artist_table_insert
    
)

load_time_dimension_table = LoadDimensionOperator(
    task_id='Load_time_dim_table',
    dag=dag,
    red_shift_conn="redshift",
    table="time",
    sql_help=SqlQueries.time_table_insert
)

run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    red_shift_conn="redshift",
    tables=["time","songs","artists","users","songplays"]
   
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

start_operator>>stage_events_to_redshift 
start_operator>>stage_songs_to_redshift 

stage_events_to_redshift>>load_songplays_table
stage_songs_to_redshift>>load_songplays_table



load_songplays_table>>load_artist_dimension_table
load_songplays_table>>load_user_dimension_table 
load_songplays_table>>load_song_dimension_table
load_songplays_table>>load_time_dimension_table

load_artist_dimension_table>>run_quality_checks
load_user_dimension_table>>run_quality_checks 
load_song_dimension_table>>run_quality_checks
load_time_dimension_table>>run_quality_checks

run_quality_checks>>end_operator



