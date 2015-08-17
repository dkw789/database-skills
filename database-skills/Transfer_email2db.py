

import psycopg2


#lines = [line.rstrip('\n') for line in open('email_list.txt')]



#connect to an existing database
conn=psycopg2.connect(dbname = "postgres", user="postgres", password="uaMoolahyai2gang4aeb", host="localhost", port="5432")
#open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new database 

#cur.execute('CREATE TABLE assignment2 (status varchar(10), id varchar(64), "from" varchar(30), time integer);')
'''
for line in lines:
	cur.execute('INSERT INTO mailing values("%s"); ', (lines[index]))
	index = index + 1
'''
f=open("email_list.txt")
cur.copy_from(f, 'mailing', sep=' ') 

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
