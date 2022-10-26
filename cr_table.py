import psycopg2
from psycopg2 import Error

try:
    connection= psycopg2.connect(user ='webadmin',
                                password ='MDDnfo15110',
                                host = 'node38352-bunnapon.proen.app.ruk-com.cloud', 
                                port = '11234',
                                database ='testdb')


    cursor = connection.cursor()

    sql = """CREATE TABLE Comments
            (id              SERIAL PRIMARY KEY,
             name            VARCHAR(50) NOT NULL,
             comment         VARCHAR(1000) NOT NULL); """

    cursor.execute(sql)
    connection.commit()

    print('Table create sucessful....')

except (Exception,psycopg2.Error) as error:
    print('Error while create',error)


finally:
    if(connection):
        cursor.close()
        connection.close()
        print('Postgres is closed')


