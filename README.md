# P3_CMPSC431W

##### How to use the database system: 

Download the spotify_songs.csv file to your local device. 

Open the P3_queries.sql file and change the path in line 2 (\copy (SELECT * FROM csv_test) to '/path/to/spotify_songs.csv' with CSV HEADER;) to the path on your local device. 

Save the file and run the commands in P3_queries.sql file in a PostgreSQL environment to create the database schema (description of database schema below). 

Open the db_test.py file. 

Replace the host_name, db_user, db_password, and db_name variables with the appropriate variables on your local device.  

Run db_test.py to interact with the interface and database. 

##### Description of Database Schema: 

TABLE tracks (track_id varchar, track_name varchar) 

TABLE artists (track_id varchar, track_artist varchar, track_popularity varchar) 

TABLE album (track_id varchar, track_album_id varchar, track_album_name varchar, 	track_album_release_date varchar) 

TABLE playlist (track_id varchar, playlist_id varchar, playlist_name varchar) 

TABLE genre (track_id varchar, genre varchar, subgenre varchar) 

TABLE speed_stats (track_id varchar, tempo float8, duration_ms float8) 

TABLE sound_stats (track_id varchar, key integer, mode integer, speech float8, acoustics 	float8, loudness float8, instrumentals float8)

*dummy table csv_test
