import psycopg2


# Connect to an existing database
# Please change the database information according to your own parameters for connection

conn=psycopg2.connect(dbname = "postgres", user="postgres", password="uaMoolahyai2gang4aeb", host="localhost", port="5432")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this Drop existing database

cur.execute('DROP TABLE IF EXISTS  mailing ;')
cur.execute('DROP TABLE IF EXISTS  domain_counter ;')
cur.execute('DROP TABLE IF EXISTS  Top_50 ;')

# Execute a command: this creates a new databases

cur.execute('CREATE TABLE mailing (addr VARCHAR(255) NOT NULL);')

cur.execute('CREATE TABLE domain_counter ( domain varchar(255), domaincount BIGINT , Date VARCHAR(255) );')

cur.execute('CREATE TABLE Top_50 (domain varchar(255), domaincount BIGINT , Date VARCHAR(255) );')

# load email addresses from text file

f=open("email_list_copy.txt")

cur.copy_from(f, 'mailing', sep=' ')

# Execute a command: this add a new column called date and generates a random date for each email address.

cur.execute("""ALTER TABLE mailing ADD Date  VARCHAR(255);""")

cur.execute("""UPDATE mailing SET Date = NOW() - '1 day'::INTERVAL * ROUND(RANDOM() * 31);""")

# Execute a command: returns domain_count according to the days and domain names

cur.execute("""INSERT INTO domain_counter SELECT SUBSTRING(addr from position('@' in addr)+1) AS domain, count(*) AS count, Date FROM mailing GROUP BY Date, domain ORDER BY count DESC;""")

# Execute a command: this creates a new column called index for indexing the above table

cur.execute("""ALTER TABLE domain_counter ADD index serial ;""")

# Execute a command: this insert top_50 domains in a new table according to their index

cur.execute("""INSERT INTO Top_50 SELECT  domain, domaincount, Date FROM domain_counter WHERE index < 51 ;""")


# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()

