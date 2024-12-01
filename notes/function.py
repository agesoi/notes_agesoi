import json
import os


def lists():
    with open('data.json', "r", encoding='utf-16') as file:
        for line in file:
            print(line)


def add():
    qq = input("Введите заметку ")
    with open("data.json", "a", encoding='utf-16') as file:
        file.write(f"{qq}\n")

        
    

def remove():
    pass

