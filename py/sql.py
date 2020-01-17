import random
import pymysql.cursors
for i in range(1, 500001):
    index = str(i).zfill(6)
    ind_marks = []
    ind_marks.append(index)
    # for j in range(1,7):
    #     ind_marks.append(random.randrange(0,100,1))
    ind_marks += random.sample(range(1,100), 6)
    ind_marks = tuple(ind_marks)
    print(ind_marks)
    try:
        connection = pymysql.connect(host='localhost',user='root', password='', db='ks', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            query = "INSERT INTO `marks` (`id`, `one`, `two`, `three`, `four`, `five`, `six`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(query, ind_marks)
            connection.commit()
            print(str(i) + "th row inserted\n-----------------")
    finally:
        connection.close()



#random.sample(range(1,100), 6)

    
