import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "xxxx",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "crudseries")
    cursor = connection.cursor()
    #define Create Query
    create = '''create table stage1.cake_flavours
                (
                  cake_id serial not null,
                  cake_type varchar(30),
                  tasty_meter varchar(30),
                  primary key (cake_id)
                );'''

    #Execute create
    cursor.execute(create)
    connection.commit()
    print("Table was created successfully!")
except (Exception, psycopg2.Error) as error :
    print ("Error encountered while Creating Table :-(", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("Postgres connection has been closed")