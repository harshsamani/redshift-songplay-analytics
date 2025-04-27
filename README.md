# Project Overview
This repository contains an ETL pipeline designed to load and transform data into the Sparkify database hosted on AWS Redshift.

- The goal of this database is to help Sparkify gain valuable insights into user behavior, such as the types of songs users prefer, the artists they listen to, and patterns in user activity based on log and file data. 

- By centralizing and structuring this information in a consistent database, Sparkify can better address a variety of business questions.

![image alt](https://github.com/harshsamani/redshift-songplay-analytics/blob/b5bfd9c8f7f0df75de54041e7894fbe789116409/Amazon-Redshift.png)

## Why AWS Redshift?
Amazon Redshift is a fully managed, cloud-based data warehouse service offered by AWS, designed to handle petabyte-scale data storage and management. It provides an efficient platform for gathering and storing large volumes of data, allowing businesses to analyze information using various business intelligence tools and uncover valuable insights for both internal operations and customer engagement.

## Database Design
The data warehouse employs a star schema architecture, which streamlines query execution and enhances the efficiency of data aggregation. At the core is the songplays fact table, surrounded by dimension tables that provide contextual information. This design facilitates intuitive data exploration and supports rapid analytical queries.

## Data Pipeline Design
The ETL pipeline is developed using Python, leveraging libraries like pandas for effective data manipulation. Python's compatibility with PostgreSQL databases enables seamless data integration and processing.​

The pipeline processes two primary data sources: song data and log data. Song data encompasses details about tracks and artists, which are extracted and loaded into the respective dimension tables.​

Initially, both song and log data, stored in JSON format on Amazon S3, are ingested into staging tables (staging_songs_table and staging_events_table) within Redshift. Subsequently, SQL-based transformations are applied to migrate data from the staging area into the structured fact and dimension tables, adhering to the star schema design.

![image_alt](https://github.com/harshsamani/redshift-songplay-analytics/blob/66b49c9fdb86c7d40d8c5c5d880744f1b660ab6c/Pipeline.png)

## Project Files Overview
create_tables.py: Drops existing tables and creates new ones, including staging, fact, and dimension tables.​

sql_queries.py: Contains all SQL queries and is used by both create_tables.py and etl.py.

etl.py: Loads data into the staging tables and then processes the data into the final fact and dimension tables.

redshift_cluster_setup.py: Automates the setup of the Redshift cluster and creates the IAM role to allow Redshift access to AWS services like S3.

redshift_cluster_teardown.py: Deletes the Redshift cluster and removes the IAM role once the project is complete.

dwh.cfg: Configuration file storing Redshift cluster and database settings. Update this file with your own AWS Redshift cluster details.

## Running the ETL Pipeline
Execute create_tables.py to set up all necessary tables based on the schema. Existing tables will be dropped and recreated.

Then, run etl.py to extract, transform, and load the data into the database tables.
