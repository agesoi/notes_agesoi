import sqlite3



def lists():
    with sqlite3.connect('notes_agesoi.db') as x:
    
        b = x.cursor()
        b.execute("SELECT * FROM notes")
        print(b.fetchall())
        

def add():
    #Кул стори тут была проблема с функцией и я думал чё за хуйня?
    #Блять лол я час проебал что бы понять что на 18 строке в переменную user_input надо поставить input какой же я еблан
    user_input = input("Напиши заметку --> ")
    
    with sqlite3.connect('notes_agesoi.db') as x:
    
        b = x.cursor()
        b.execute(f"INSERT INTO notes VALUES ('{user_input}')")
    

        
    

def remove():
    db = sqlite3.connect('notes_agesoi.db')
    
    x = db.cursor()
    x.execute()
    
    db.commit()
    db.close()



# Создание таблицы йоу
# db = sqlite3.connect('notes_agesoi.db')

# x = db.cursor()
# x.execute("""CREATE TABLE notes (
#     notes 
# )""")

# db.commit()
# db.close()