import sqlite3



def lists():    
    with sqlite3.connect('notes_agesoi.db') as x:
    
        b = x.cursor()
        b.execute("SELECT rowid, * FROM notes")
        screen = b.fetchall()
        for el in screen:
            print(str(el[0])+ f" " + el[1])
        

def add():
    #Кул стори тут была проблема с функцией и я думал чё за хуйня?
    #Блять лол я час проебал что бы понять что на 16 строке в переменную user_input надо поставить input какой же я еблан
    user_input = input("Напиши заметку --> ")
    
    with sqlite3.connect('notes_agesoi.db') as x:
    
        b = x.cursor()
        b.execute(f"INSERT INTO notes VALUES ('{user_input}')")
    

        
    

def remove():
    with sqlite3.connect('notes_agesoi.db') as x:
        b = x.cursor()
        
        user_input = int(input("Удалите заметку по id --> "))
        
        b.execute("DELETE FROM notes WHERE rowid = ?", (user_input,))
    



# Создание таблицы йоу
# db = sqlite3.connect('notes_agesoi.db')

# x = db.cursor()
# x.execute("""CREATE TABLE notes (
#     notes 
# )""")

# db.commit()
# db.close()