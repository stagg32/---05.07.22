import os
import shutil
import sys

while True:
    choice = input("Введите варианты действий: \n1.создать папку\n2.создать файл\n"
                   "3.удалить (файл/папку)\n4.копировать (файл/папку)"
                   "\n5.просмотр содержимого рабочей директории\n6.посмотреть только папки\n"
                   "7.посмотреть только файлы\n8.просмотр информации об операционной системе\n"
                   "9.создатель программы\n10.играть в викторину\n11.мой банковский счет\n"
                   "12.выход\nВаш выбор - ")
    if choice == '1':
        newfolder = input("Введите название папки: ")
        os.mkdir(f'{newfolder}')
    elif choice == '2':
        filename = input("Введите имя файла: ")
        f = open(filename, "w")
    elif choice == '3':
        delete_file = input("Введите имя удаляемого файла/папки: ")
        if os.path.isdir(f'{delete_file}'):
            shutil.rmtree(delete_file)
        else:
            os.remove(delete_file)
    elif choice == '4':
        name = input("Введите имя копируемого файла/папки: ")
        newname = input("Введите новое название файла/папки: ")
        if os.path.isdir(f'{name}'):
            shutil.copytree(name, newname)
        else:
            shutil.copy(name, newname)
    elif choice == '5':
        print(f'{"Список файлов и папок:"}', os.listdir())
    elif choice == '6':
        for item in os.listdir():
            if os.path.isdir(item):
                print(item)
    elif choice == '7':
        for item in os.listdir():
            if os.path.isfile(item):
                print(item)
    elif choice == '8':
        print('My OS is', sys.platform, '(', os.name, ')')
    elif choice == '9':
        print('Copyright:', sys.copyright)
    elif choice == '10':
        import victory

    elif choice == '11':
        import use_functions

    elif choice == '12':
        print("До свидания!")
        break
    else:
        print("Неверный пункт меню!")
