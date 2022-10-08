/* To import this, open the database (.db) file in SQLite, then run the following command:
   source sql/database.sql

   You can also use this if you're lazy:
    sqlite3 database.db < sql/database.sql
*/
create table users(id int PRIMARY KEY AUTOINCREMENT,results int(15));