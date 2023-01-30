from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'
  
    @apply_defaults
    def __init__(self,
                 
                 red_shift_conn="",

                        table="",
                        sql_help="",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        
        self.red_shift_conn=red_shift_conn
        
        self.table=table 
        self.sql_help=sql_help
    def execute(self, context):
        redshift=PostgresHook(postgres_conn_id=self.red_shift_conn)
        
        self.log.info("Clearing data from destination Redshift table")
        redshift.run("DELETE FROM {}".format(self.table))
        self.log.info('LoadDimension into Table')
        redshift.run("insert into {} {}".format(self.table,self.sql_help))
        
