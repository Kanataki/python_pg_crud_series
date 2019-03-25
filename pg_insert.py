import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "NAivasha12",
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
    print(count, "Record Inserted successfully!")
except (Exception, psycopg2.Error) as error :
    print ("Error while attempting to Insert Record :-(", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")