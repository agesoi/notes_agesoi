from function import add, lists, remove
import os







while True:
    data_user = input('Заметки---> ')
    data_userl = data_user.lower()
    if data_userl == "exit":
        break
    
    elif data_userl == "list":
        lists()
        
    elif data_userl == "help":
        print("Все команды:\nlist-список всех заметок\nadd-добавление заметки\nremove (номер заметки)-удаление заметки по номеру\nhelp-список команд\nclear-очистка консоли\nexit-выйти из консоли командой")
        
    elif data_userl == "clear":
        os.system("cls")
        
    elif data_userl == "add":
        add()

    elif data_userl == "remove":
        pass
        
    else:
        print("Ниезвестная команда введите help для вывода всех команд")
