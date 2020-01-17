import random
for i in range (1,500001):
    ind = str(i).zfill(6)
    ind_marks = []
    ind_marks.append(ind)
    ind_marks += random.sample(range(1,100), 6)
    index, one, two, three, four, five, six = ind_marks
    q = "'" + index + "'" + "," + str(one) + ", " + str(two) + ", " + str(three) + ", " + str(four) + ", " + str(five) + ", " + str(six)
    query = "INSERT INTO `marks` (`id`, `one`, `two`, `three`, `four`, `five`, `six`) VALUES (" + q + ");"
    print(query)
    