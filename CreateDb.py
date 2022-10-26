import psycopg2

try:
    connection= psycopg2.connect(user ='webadmin',
                                password ='MDDnfo15110',
                                host = 'node38352-bunnapon.proen.app.ruk-com.cloud', 
                                port = '11234',
                                database ='postgres')

    connection.autocommit = True

    cursor = connection.cursor()

    sql = """CREATE database testdb"""

    cursor.execute(sql)

    print('Data create sucessful....')

except (Exception,psycopg2.Error) as error:
    print('Error while create',error)


finally:
    if(connection):
        cursor.close()
        connection.close()
        print('Postgres is closed')


