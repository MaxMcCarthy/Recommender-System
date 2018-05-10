import os
from database.db import create_connection

path = os.getcwd()

split_path = path.split('/')

while split_path[-1] != 'Recommender-System':
    print(split_path)
    path = "/".join(split_path[:-1])
    print(path)
    split_path = path.split('/')

path += "/recommender-db.db"

print(path)

db = create_connection(path)
