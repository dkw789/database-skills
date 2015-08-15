# database-skills
1,000,0000 email addresses and 10,000 domains using Python and Postgres


HOW TO RUN THE CODE
=============================================================================================================================
1. Ensure that the postgres  database has been created with dbname = "postgres", user="postgres", password="uaMoolahyai2gang4aeb", host="localhost", port="5432"

    N.B The parameters dbname = " ", user=" ", password=" ", host=" ", port=" " 
     Can be modified to according to the user's preferences but the configuration also need to be changed in the python file       email2db.py

2. Install python and psycopg2 (Postgres database connector for python) 

3. Install PgAdmin to be able to see the data being populated.

4.  Run the email2db.py  using python from terminal 
       e.g: (python email2db.py )

5. Connect to the database using PgAdmin in order to see the table and their contents or you can also access the database through terminal.


 Note: Since the database takes for input a text file containing 1,000,0000 random email addresses and 10,000 domains, it   might take a few minutes for all the data to be populated in the tables, but if a smaller text file is used, fro instance one which contains only  10,0000 random email addresses and about 1000 domains then the data is populated almost instantly.
 
 HOW THE CODE ACTUALLY WORKS
=============================================================================================================================
 
 Tables         |               Their descriptions
 
mailing         |  Initially empty but then stores the email addresses imported into the database.

domain_counter  |  The domain_counter which holds a daily count of email addresses by their domain name.

Top_50          |  Contains the top 50 domains by count sorted by percentage growth of the last 30 days compared to the total


 
The first part of the code checks if the tables to be created into the databse exist already if yes, then those are dropped in order to satisfy the requirement that states "The mailing table will initially be empty" at the beginning
 
A text file containing only email addresses is imported into the database, This goes into a table called mailing table.

I would then generated random dates for each email address while adding them to another table called domain_counter table so as to simulate the process of new addresses being added on a daily basis.
 
A query is used to count the email addresses with similar domains, and  sort the domains in descending order for a particular day and add it to the domain_counter table.
 
Next I would indexed the domain_counter table in order to fetch the top 50 domains from the latter and sent them to a new table called Top_50 
 
The Top_50 table would contain only the top 50 domains by count sorted by percentage growth of the last 30 days compared to the total.
 
 
 

