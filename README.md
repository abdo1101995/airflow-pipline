## Airflow Pipeline
## RedShift Data WareHouse(AWs Cloud)

# about project

A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

our task is extracting data from s3 bucket in redshift cloud in  dimensional tables for their analytics team.


# about data

- Song Dataset

The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are file paths to two files in this dataset.
- Log Dataset

The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate app activity logs from an imaginary music streaming app based on configuration settings.

The log files in the dataset you'll be working with are partitioned by year and month. For example, here are file paths to two files in this dataset.

# Overview

this project about making Etl pipeline 
- connect aws services to airflow
- Etract data from s3 bucket
- transform it to informative tables by using star schema (fact + dimensional tables) 
- load them in redshift to help bi team for analytical tasks


#Star Schema
![alt text](https://github.com/abdo1101995/airflow-pipline/blob/main/Screenshot%202022-11-09%20190054.png)

# Airflow Dags

![alt text](https://github.com/abdo1101995/airflow-pipline/blob/main/udac-example-dag.png)

 # aws_services uses
 
 - s3
 - iam (user +role)
 - ec2(security group)
 - vpc
 - redshift(cluster)
 
 # other tools
 
 - python
 -sql
 -airflow
 

 
