import sqlite3



def lists():
    db = sqlite3.connect('notes_agesoi.db')
    
    x = db.cursor()
    x.execute()
    
    db.commit()
    db.close()


def add():
    #Кул стори тут была проблема с функцией и я думал чё за хуйня?
    #Блять лол я час проебал что бы понять что на 18 строке в переменную user_input надо поставить input какой же я еблан
    user_input = input("add notes")
    
    db = sqlite3.connect('notes_agesoi.db')
    
    x = db.cursor()
    x.execute(f"INSERT INTO notes VALUES ('{user_input}')")
    
    db.commit()
    db.close()

        
    

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
#     notes text
# )""")

# db.commit()
# db.close()