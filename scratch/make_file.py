from http import HTTPStatus
from random import choice

with open('errors.txt', 'w') as f:
    for i in range(100):
        f.write(f"{i} {choice(list(HTTPStatus))} \n")

