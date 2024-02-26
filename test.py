import sqlite3
data1=sqlite3.connect("test1.db")
try:
    cur = data1.cursor()
    cur.execute("CREATE TABLE LogPass(name, lastname, email, password, reminder,age)")
except:
    pass

cur=data1.cursor()
cur.execute("""
            SELECT name, lastname, email, password, reminder,age FROM LogPass WHERE email='pawel.milewski01@gmail.com'
            """)
result2 = cur.fetchall()

data1.close()


#ista =[('Pawel', 'Milewski', 'pawel.milewski01@gmail.com', 'Zbyszek123!', 'Imie ojca', 29), ('Emilia', 'Jelińska', 'emilia@gmail.com', 'Emilia8224!', '33', 33),('Adam', 'Nowak', 'emilia@gmail.com', 'Emilia8224!', '33', 33)]
#a = tuple(lista)
#print(lista[2][1][0].index('Adam'))
#print(lista[1])


#print(a.index('Pawel'))
