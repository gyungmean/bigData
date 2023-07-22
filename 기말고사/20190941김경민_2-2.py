import sqlite3

con=sqlite3.connect("countDB2")
cur=con.cursor()

line_counter = 0
with open('output.txt', 'r', encoding='utf-8') as file:
    while 1:
        word = file.readline()
        if not word: break
        if line_counter == 0:
            line_counter += 1
            continue
        else:
            data = word.split(",")
            sql = "INSERT INTO countTable VALUES('" + data[0] + "','" + data[1] + ")"
            cur.execute(sql)

con.commit()
cur = con.cursor()
cur.execute("SELECT * FROM countTable ORDER BY '빈도수' DESC")
while 1:
    row = cur.fetchone()
    if row == None:
        break;
    data1 = row[0]
    data2 = row[1]
    print(data1, data2)
con.commit()
con,close()
