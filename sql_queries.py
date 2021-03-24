
#DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

#CREATE TABLES 

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
    songplay_id SERIAL PRIMARY KEY, 
    start_time bigint NOT NULL, 
    user_id int NOT NULL, 
    level varchar,
    song_id varchar, 
    artist_id varchar, 
    session_id int, 
    location text, 
    user_agent text)
""")

user_table_create = (""" 
CREATE TABLE IF NOT EXISTS users(
    user_id int PRIMARY KEY, 
    first_name varchar, 
    last_name varchar, 
    gender varchar(1), 
    level varchar
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
    song_id varchar PRIMARY KEY, 
    title text, 
    artist_id varchar, 
    year int, 
    duration numeric
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
    artist_id varchar PRIMARY KEY, 
    name varchar, 
    location text, 
    latitude decimal, 
    longitude decimal
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
    start_time bigint PRIMARY KEY, 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday varchar
)
""")