# Project Purpose
A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

They have decided to bring you into the project and expect you to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

# Technologies
- Python
- Apache Airflow
- Amazon Redshift
- Amazon S3

# Schema Design:
The schema design being used is the STAR schema with 1 fact table: songplays and 4 dimension tables: artists, songs, users, and time.

![Schema Image](./star.png "Schema Image")

# DAG Design
Created four custom operators to perform tasks such as staging the data, filling the data warehouse, and running checks on the data as the final step. 

![DAG Image](./dag.png "DAG Image")

# Challenges
Understanding how the Airflow UI works was initially a challenge but eventually I understood how to use it to connect additional services such as AWS as well as inspecting each of the nodes within the DAG.

![Dag Nodes Image](./dag-nodes.png "Nodes Image")

# Improvements
Currently the pipeline only has a single data quality check which checks whether or not Redshift is empty after the ETL procedure has completed. This can be improved by accepting multiple data quality checks that can be defined by the user.
```python
checks = [
  {'test_sql': ..., 'expected_result': ...},
  {'test_sql': ..., 'expected_result': ...}
]
```
