import psycopg2
try:
    #Define connection
    connection = psycopg2.connect(user = "postgres",
                                  password = "xxxxxx",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "crudseries")
    cursor = connection.cursor()
    cake_id = 2
    cake_type = 'Passion'
    
    #Get record as it is pre edit
    print("Table Records")
    select = """SELECT * FROM stage1.cake_flavours
                            where cake_id = %s;"""

    cursor.execute(select, (cake_id, ))
    record = cursor.fetchone()
    print(record)

    # Update the record
    update = """Update stage1.cake_flavours set cake_type = %s where cake_id = %s"""
    cursor.execute(update, (cake_type, cake_id))
    connection.commit()
    count = cursor.rowcount
    print(count, "Record Updated successfully ")

    #Print Updated Record
    newselect = """SELECT * FROM stage1.cake_flavours where cake_id = %s"""
    cursor.execute(newselect, (cake_id,))
    record = cursor.fetchone()
    print(record)
    

    #Execute
    cursor.execute(query, record)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record Inserted successfully!")
except (Exception, psycopg2.Error) as error :
    print ("Error encountered while Inserting Record :-(", error)
finally:
    #Close DB connection.
        if(connection):
            cursor.close()
            connection.close()
            print("Postgres connection has been closed")