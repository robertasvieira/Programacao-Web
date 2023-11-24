#Importa o módulo sqlite3 para interagir com bancos de dados SQLite
import sqlite3

#Atribui um nome ao arquivo do banco de dados
DATABASE = 'araclin.db'

#Conecta ao banco de dados 
conn = sqlite3.connect(DATABASE)

#Cria um cursor para interagir com o banco de dados
cursor = conn.cursor()

#Cria a tabela 'Usuarios' se ela não existir, com as colunas id, nome e idade
cursor.execute('''
   CREATE TABLE IF NOT EXISTS Usuarios (
       id INTEGER PRIMARY KEY,
       nome TEXT,
       idade INTEGER
   )
''')

#Insere valores na tabela 'Usuarios'
cursor.execute('INSERT INTO Usuarios (nome, idade) VALUES (?, ?)', ('Roberta', 20))
cursor.execute('INSERT INTO Usuarios (nome, idade) VALUES (?, ?)', ('Geovane', 24))
cursor.execute('INSERT INTO Usuarios (nome, idade) VALUES (?, ?)', ('Maria', 47))
cursor.execute('INSERT INTO Usuarios (nome, idade) VALUES (?, ?)', ('Geraldo', 50))

#Aplica as alterações no banco de dados
conn.commit()

#Seleciona todos os registros da tabela 'Usuarios' e os imprimir na tela
cursor.execute('SELECT * FROM Usuarios')
for row in cursor.fetchall():
    print(row)

#Fecha a conexão com o banco de dados
conn.close()
