from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 redshift_conn_id="",
                 tables=[],
                 sql_test="",
                 expected_value=0,
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id
        self.tables = tables
        self.sql_test = sql_test
        self.expected_value = expected_value

    def execute(self, context):
#         self.log.info('DataQualityOperator not implemented yet')
        redshift_hook = PostgresHook(self.redshift_conn_id)
        for table in self.tables:
            records = redshift_hook.get_records(self.sql_test.format(table))
            
            if len(records) < self.expected_value or len(records[0]) < self.expected_value:
                raise ValueError(f"Data quality check failed. {table} returned no results.")
                
            num_records = records[0][0]
            
            if num_records < self.expected_value:
                raise ValueError(f"Data quality check failed. {table} has no records.")
            
            self.log.info(f"Data quality on table {table} check passed with {records[0][0]} records")

                
            