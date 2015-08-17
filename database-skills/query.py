import psycopg2


#connect to an existing database
conn=psycopg2.connect(dbname = "postgres", user="postgres", password="uaMoolahyai2gang4aeb", host="localhost", port="5432")
#open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new database 

#cur.execute('CREATE TABLE assignment2 (status varchar(10), id varchar(64), "from" varchar(30), time integer);')
#cur.execute('CREATE TABLE mailing (addr VARCHAR(255) NOT NULL);')
cur.execute("""INSERT INTO domain_counter SELECT SUBSTRING(addr from position('@' in addr)+1) AS domain, count(*) AS count FROM mailing GROUP BY domain ORDER BY count DESC;""")


###SELECT SUBSTRING(addr from position('@' in addr)+1) AS domain, count(*) AS count FROM mailing GROUP BY domain ORDER BY count DESC; #working for postgresql need to writing in python


# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
