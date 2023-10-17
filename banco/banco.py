import sqlite3

print('testando entrada no arquivo')

try:

    conn = sqlite3.connect('aplication.sqlite3')
    print('Voce acessou o sqlite')

except Exception:
    print('Voce nao esta conseguindo se conectar sqlite')

if conn is not None:
    print('Voce estabilizou sua coneccao')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE if not exists pessoa (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome VARCHAR(15) NOT NULL,
                   idade INTEGER NOT NULL,
                   altura VACHAR(20) NOT NULL
                   );
                    ''')
    cursor.execute('''
                   CREATE TABLE if not exists usuarios(
                   nome VARCHAR(15) NOT NULL,
                   nickname VARCHAR(30) PRIMARY KEY NOT NULL,
                   senha VARCHAR(30) NOT NULL
                   );
                   ''')
    print("Tabelas criadas com sucesso")
    conn.commit()
    cursor.close()
    conn.close()