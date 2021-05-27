import mariadb 

conn = mariadb.connect(
    user="ubuntu",
    password="abcd",
    host="localhost",
    database="crypto")
cur = conn.cursor() 


#insert information 
try: 
    cur.execute(#"CREATE OR REPLACE TABLE test (a int, b char(10));"
    #"INSERT INTO test (a, b) VALUES (1, 'Doe')"
    "SELECT * FROM test;"
    ) 
    for (a,b) in cur:
        print(a,b)
except mariadb.Error as e: 
    print(f"Error: {e}")

conn.commit() 
conn.close()