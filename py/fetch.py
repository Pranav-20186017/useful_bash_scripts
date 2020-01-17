import pymysql.cursors
index = input("Please enter your id: ")
try:
    connection = pymysql.connect(host='localhost',user='root', password='', db='ks', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        query = "SELECT * FROM `marks` WHERE `id` = %s;"
        cursor.execute(query, (index))
        result = cursor.fetchone()
        connection.commit()
        print(type(result))
finally:
    connection.close()