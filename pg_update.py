import psycopg2
try:
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

    #Updated Recordprint("Table After updating record ")
    newselect = """SELECT * FROM stage1.cake_flavours where cake_id = %s"""
    cursor.execute(newselect, (cake_id,))
    record = cursor.fetchone()
    print(record)
    

    #Execute create
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