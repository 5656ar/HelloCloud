import psycopg2

try:
    connection= psycopg2.connect(user ='webadmin',
                                password ='VGEzzs03752',
                                host = 'node38349-bunnapon-1867984.proen.app.ruk-com.cloud', 
                                port = '11234',
                                database ='postgres')

    connection.autocommit = True

    cursor = connection.cursor()

    sql = """CREATE database bunnapon"""

    cursor.execute(sql)

    print('Data create sucessful....')

except (Exception,psycopg2.Error) as error:
    print('Error while create',error)


finally:
    if(connection):
        cursor.close()
        connection.close()
        print('Postgres is closed')


