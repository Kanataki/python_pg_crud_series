import psycopg2
try:
    #Define connection
    connection = psycopg2.connect(user = "postgres",
                                  password = "xxxxx",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "crudseries")
    cursor = connection.cursor()
    #define Insert Query
    query = """INSERT INTO stage1.cake_flavours
                (cake_type, tasty_meter)
                VALUES (%s,%s);"""

    record = ('Red Velvet', 'Awesome')

    #Execute Insert
    cursor.execute(query, record)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record has been Inserted successfully!")
except (Exception, psycopg2.Error) as error :
    print ("Error encountered while Inserting Record :-(", error)
finally:
    #Close DB connection
        if(connection):
            cursor.close()
            connection.close()
            print("Postgres connection has been closed")