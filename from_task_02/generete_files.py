from random import randint, choices
from string import ascii_lowercase, digits
from os import chdir
from pathlib import Path


def create_files(extension: str, min_len: int = 6, max_len: int = 30, min_size: int = 256, max_size: int = 4096,
                 count: int = 42) -> None:
    for _ in range(count):
        file_name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len, max_len))) + '.' + extension
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(file_name, 'wb') as f:
            f.write(data)


def generate_file(**kwargs):
    for extension, amount in kwargs.items():
        create_files(extension, count=amount)


if __name__ == '__main__':
    generate_file(xlsx=10)