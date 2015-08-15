# database-skills
1,000,0000 email addresses and 10,000 domains using Python and Postgres


HOW TO RUN
=============================================================================================================================
1. Ensure that the postgres  database has been created with dbname = "postgres", user="postgres", password="uaMoolahyai2gang4aeb", host="localhost", port="5432"

    N.B The parameters dbname = " ", user=" ", password=" ", host=" ", port=" " 
     Can be modified to according to the user's preferences but the configuration also need to be changed in the python file       email2db.py

2. Install python and psycopg2 (Postgres database connector for python) 

3. Install PgAdmin to be able to see the data being populated easily.

4.  Run the email2db.py  using the python in terminal 
       e.g: (python email2db.py )

5. Connect to the databse using PgAdmin in order to see the table and their contents or you can also access the database through terminal.



 Note: Since the database takes for input a text file containing 1,000,0000 random email addresses and 10,000 domains, it   might take a a few minutes for all the data to be populated in the tables but if a small text file is used, onw which contains 10,0000 random email addresses and about 1000 domains then the data is populated alomost instantly.
 
 Also the text file contain only email address so I generate random dates for each address while adding them to the database.
 
 
 

