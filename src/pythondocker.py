import pymysql.cursors

# specify database configurations
connection = pymysql.connect(host='localhost', 
                             user='root',
                             password='',
                             database='',
                             port=3308,
                             cursorclass=pymysql.cursors.DictCursor)
                             



last_name_input = input("Enter a last name.")                             
first_name_input = input("Enter a first name.")



print(first_name_input, last_name_input)
with connection:
    with connection.cursor() as cursor:        
        sql = f"INSERT INTO new_names (lastName, firstName) VALUES ('{last_name_input}', '{first_name_input}')"
        cursor.execute(sql)
        connection.commit()
        cursor.close()

        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {create_a_table};"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            cursor.close()
            
            