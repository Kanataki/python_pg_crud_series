import psycopg2
def deletecake(cake_id):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "xxxxxxx",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "crudseries")
        cursor = connection.cursor()
        #view record before deleting
        print("Cake records")
        select = """SELECT * FROM stage1.cake_flavours
                                where cake_id = %s;"""
        cursor.execute(select, (cake_id, ))
        record = cursor.fetchone()
        print(record)

        #Delete the frigging cake
        delete = """Delete FROM stage1.cake_flavours
                    where cake_id = %s"""
        cursor.execute(delete, (cake_id, ))
        connection.commit()
        count = cursor.rowcount
        print(count, "cake has been successfully deleted")

    except (Exception, psycopg2.Error) as error :
        print ("Error encountered while deleting cake :-(", error)
    finally:
        #Closing DB connection
            if(connection):
                cursor.close()
                connection.close()
                print("Postgres connection has been closed")
cake_id = 2
deletecake(cake_id)