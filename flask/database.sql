/* To import this, open the database (.db) file in SQLite, then run the following command:
   source sql/database.sql

   You can also use this if you're lazy:
    sqlite3 flask/database.db < flask/database.sql
*/
create table users(id varchar,cookies int, viren int, phishing int);