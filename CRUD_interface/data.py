import sqlite3 
from sqlite3 import Error
#estabelecendo conexao
con = sqlite3.connect("banco.py") 

#criando tabela
try:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXIST professor(" 
    "id INTEGER AUTOINCREMENT PRIMARY KEY, " 
    "nome TEXT, " 
    "disc  TEXT)")  
    con.commit() 
    print("tabela criada")

except Error: 
    print("Erro")

res = cur.execute("SELECT * FROM professor") 

coluna = res.fetchall() 
'''
for i in coluna: 
    print(i) 
'''
