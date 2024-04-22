""" З'єднання та завантаження Json файліву хмарну базу даних. """

import json
from models import Author, Qoutes

from mongoengine import connect

with open('password.txt', 'r') as file_pass:
    password = file_pass.read()

URL = f'mongodb+srv://tapxyh1445:{password}@nosqlbase.zekqidk.mongodb.net/'
connect(host=URL)

authors_file = 'authors.json'
qoutes_file = 'qoutes.json'

# Завантажуємо авторів та цитати
def upgrade_authors_and_qoutes():
    with open(authors_file, 'r', encoding='UTF-8') as fn:
        authors_json_file = json.load(fn)
    
    with open(qoutes_file, 'r', encoding='UTF-8') as fn:
        qoutes_json_file = json.load(fn)
    
    try:
        for author_dict in authors_json_file:
            author = Author(
                fullname=author_dict.get('fullname'),
                born_date=author_dict.get('born_date'),
                born_location=author_dict.get('born_location'),
                description=author_dict.get('description')
            )
            author.save()

        for qoute_dict in qoutes_json_file:
            author_name = qoute_dict.get('author')
            author = Author.objects(fullname=author_name).first()
            if author:
                qoute = Qoutes(
                    author=author,
                    tags=qoute_dict.get('tags'),
                    qoute=qoute_dict.get('qoute')
                )
                qoute.save()
        print('Loading complite.')  
    except:
        print(f'This author is already in the database, or is repeated in your file.')

if __name__ == "__main__":

    upgrade_authors_and_qoutes()

