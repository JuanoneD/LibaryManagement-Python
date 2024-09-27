import sqlite3 as sq
import os
conn = sq.connect('data/Library.db')

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
    os.system("copy './data/Library.db' ./backups/backup"+{os.popen('date').read().strip()})

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
        insert_books(input("Digite o titulo do Livro:"),input("Digite o autor do livro:"),int(input("Digite o ano de lançameto do livro:")),float(input("Digite o preço:")))
    except:
        print("Erro em Inserir livro")

def GetAllBooks():
    try:
        for row in get_boooks():
            print(row)
    except:
        print("Sem livros Disponiveis")

def UpdatePriceBook():
    try:
        update_book(int(input("Digite o Id do livro:")),float(input("Digite o novo preco do livro:")))
    except:
        print("Erro ao editar livro")

def RemoveBooks():
    try:
        delete_book(int(input("Digite o Id do livro a ser deletado:")))
    except:
        print("Erro ao remover")

def SearchByAuthor():
    try:
        for row in search_author(input("Escreva o nome do autor: ")):
            print(row)
    except:
        print("Erro pesqisar por autor")

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
        case 0:
            backup_database()


