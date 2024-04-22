""" Нескінченний цикл для запитів. """

from mongoengine import *

from models import Author, Qoutes
from app import URL


connect(db='test', host=URL)


def search_qoutes(command, value):
    if command == "name":
        # Знаходимо автора за ім'ям
        author = Author.objects(fullname=value).first()
        if author:
            qoutes = Qoutes.objects(author=author)
            print_qoutes(qoutes)
        else:
            print("Автора з таким ім'ям не знайдено.")
    elif command == "tag":
        # Знаходимо цитати за тегом
        qoutes = Qoutes.objects(tags=value)
        print_qoutes(qoutes)
    elif command == "tags":
        # Знаходимо цитати за набором тегів
        tags = value.split(",")
        qoutes = Qoutes.objects(tags__in=tags)
        print_qoutes(qoutes)
    elif command == "exit":
        print("Програма завершує роботу.")
        return True
    else:
        print("Непідтримувана команда.")
    return False

def print_qoutes(qoutes):
    # Виводимо знайдені цитати
    for quote in qoutes:
        print(f"Цитата: {quote.qoute}")
        print(f"Автор: {quote.author.fullname}")
        print(f"Теги: {', '.join(quote.tags)}")
        print()

while True:
    user_input = input("Введіть команду та значення (формат: команда:значення): ")
    parts = user_input.split(":", 1)
    
    if len(parts) != 2:
        print("Неправильний формат команди.")
        continue
    
    command, value = parts
    if search_qoutes(command.strip(), value.strip()):
        break
    