# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def check_file(file, str_search):
    full_name = os.path.join(current_dir, file)
    with open(full_name) as f:
        text = f.read()
        if str_search in text:
            return True
    return False


def filter_files(all_files, str_search):
    new_files = []
    for file in all_files:
        if check_file(file, str_search):
            new_files.append(file)
    return new_files


if __name__ == '__main__':
    files = [f for f in os.listdir(current_dir) if f.endswith('.sql')]
    while True:
        inp = input('Найдётся всё! Введите строку поиска:')
        if inp == '':
            print('надо хоть что-то вести...')
            continue
        else:
            files = filter_files(files, inp)
            for cur_file in files:
                print(os.path.join(current_dir, cur_file))
            print('Всего:', len(files))
