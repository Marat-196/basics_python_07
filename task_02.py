# 2. Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов
# внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
# берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os
from pathlib import Path


def num_value(count) -> int:
    return 10 ** (count - 1)


def new_clice_name(old_name, lst):
    my_lst = [0, len(old_name)]
    if lst[0] < len(old_name):
        my_lst[0] = lst[0]
    elif lst[0] > len(old_name):
        my_lst[0] = len(old_name)
    if lst[1] < len(old_name):
        my_lst[1] = lst[1]
    elif lst[1] > len(old_name):
        my_lst[1] = len(old_name)
    return old_name[my_lst[0]:my_lst[1]]


def rename_files(new_name: str, number: int, extension_start: str, extension_end: str, slice_name: list):
    count = num_value(number)
    os.chdir('./from_task_02')
    for obj in os.listdir():
        if os.path.isfile(obj):
            if obj.split('.')[1] == extension_start:
                name = new_clice_name(obj, slice_name)
                os.rename(obj, f'{name}{new_name}_{count}.{extension_end}')
                count += 1


if __name__ == '__main__':
    rename_files('access', 3, 'docx', 'csv', [0, 2])
