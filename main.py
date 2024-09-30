import sqlite3 as sq
import pandas as pd
import os
import time

def create_tables():
    conn.execute('''
        CREATE TABLE iF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publish_year INTEGER NOT NULL,
            price REAL NOT NULL 
        );
    ''')

def backup_database():
    if not os.path.exists(".\\backups"):
        os.system("mkdir backups")
    else:
        files = os.listdir(".\\backups")
        if len(files)>4:
            os.remove(".\\backups\\"+files[0])
            
    os.system(f'copy ".\\data\\Library.db" ".\\backups\\backup_{time.strftime("%Y%m%d_%H%M%S")}.db"')

def insert_books(title,author,publish_year,price):
    conn.execute("INSERT INTO books(title,author,publish_year,price) Values('%s','%s',%i,%f);"%(title,author,publish_year,price))
    conn.commit()

def get_boooks():
    return conn.execute("Select * from books")

def update_book(id_book,new_price):
    conn.execute("Update books set price=%f where id=%i"%(new_price,id_book))
    conn.commit()

def delete_book(id_book):
    conn.execute("Delete from books where id=%i"%(id_book))
    conn.commit()

def search_author(author):
    return conn.execute("Select * from books where author like '%"+author+"%'")

def InsertBook():
    try:
        backup_database()
        insert_books(input("Digite o titulo do Livro:"),input("Digite o autor do livro:"),int(input("Digite o ano de lançameto do livro:")),float(input("Digite o preço:")))
    except:
        print("Erro em Inserir livro:")

def GetAllBooks():
    try:
        print("Livros Disponiveis:")
        for row in get_boooks():
            print(row)
    except:
        print("Sem livros Disponiveis")

def UpdatePriceBook():
    try:
        backup_database()
        update_book(int(input("Digite o Id do livro:")),float(input("Digite o novo preco do livro:")))
    except:
        print("Erro ao editar livro")

def RemoveBooks():
    try:
        backup_database()
        delete_book(int(input("Digite o Id do livro a ser deletado:")))
    except:
        print("Erro ao remover")

def SearchByAuthor():
    try:
        for row in search_author(input("Escreva o nome do autor: ")):
            print(row)
    except:
        print("Erro pesqisar por autor")
        
def ToCSV():
    backup_database()
    df = pd.read_sql_query("select * from books",conn)
    if not os.path.exists(".\\exports"):
        os.system("mkdir exports")
    df.to_csv(".\\exports\\"+input("Escreva o nome do arquivo: "))
    
def FromCSV():
    backup_database()
    df = pd.read_csv("./"+input("Escreva o nome do arquivo:"))
    df.to_sql('books',conn,if_exists="replace",index=False)
        
#MAIN #############################      
if not os.path.exists(".\\data"):
    os.makedirs("data")
conn = sq.connect('data/Library.db')


create_tables()

while 1:
    menu = int(input('''
        1. Adicionar novo livro
        2. Exibir todos os livros
        3. Atualizar preço de um livro
        4. Remover um livro
        5. Buscar livros por autor
        6. Exportar dados para CSV
        7. Importar dados de CSV
        8. Fazer backup do banco de dados
        9. Sair
    '''))
    match menu:
        case 9:
            break
        case 1:
            InsertBook()
        case 2:
            GetAllBooks()
        case 3:
            UpdatePriceBook()
        case 4:
            RemoveBooks()
        case 5:
            SearchByAuthor()
        case 6:
            ToCSV()
        case 7:
            FromCSV()
        case 8:
            backup_database()


