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

- Etract data from s3 bucket
- transform it to informative tables by using star schema (fact + dimensional tables) 
- load them in redshift to help bi team for analytical tasks

# files 

- dwh.cfg

put all aws configurations

- sql_queries.py

make all queries drop ,create , insert.

we first make staging data to help us in insert fact and dimensional tables.

we used s3 bucket to extract data from it and put in staging tables .

# fact Table
songplays - records in event data associated with song plays i.e. records with page NextSong
{songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent}.

# dimensional tables

- users - users in the app
{user_id, first_name, last_name, gender, level}
- songs - songs in music database
{song_id, title, artist_id, year, duration}
- artists - artists in music database
{artist_id, name, location, lattitude, longitude}
- time - timestamps of records in songplays broken down into specific units
{start_time, hour, day, week, month, year, weekday}

- create_tables.py

 connect in database in redshift and create all schema .
 
 - etl.py
 
 load data in staging and insert data in tables.
 
 # aws_services uses
 
 - s3
 - iam (user +role)
 - ec2(security group)
 - vpc
 - redshift(cluster)
 
 # other tools
 
 - python(configparser+ psycopg2)
 
 
 # how to run the Python scripts
 
 after making redshift clould and putting configurations
 - make all queries in sql_queries.py
 - first run create_tables.py in terminal
 - second  run etl.py in terminal
