# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil

print(sys.argv)


def copy_file(file):
    if os.path.isdir(file):
        try:
            new_dir = file + '_copy'
            os.mkdir(new_dir)
            files = os.listdir('./' + file)
            for f in files:
                shutil.copy(f, os.path.join(new_dir, f))
        except FileExistsError:
            pass
        except PermissionError:
            pass
    else:
        try:
            new_file = file + '_copy'
            dst = shutil.copyfile(file, new_file)
            print("Копия файла '{}' создана:".format(file))
        except FileNotFoundError:
            print("Не могу создать копию файла. Файл - источник {} не существует:".format(file))
        except PermissionError:
            print("Не могу сменить файл '{}'. Не хватает прав.".format(new_file))


def change_directory(dir):
    try:
        os.chdir(dir)
        print("Директория изменена. Ваш текущий каталог {}".format(dir))
    except FileNotFoundError:
        print("Не удается сменить директорию на '{}'. Такая директория не существует".format(dir))
    except PermissionError:
        print("Не могу сменить директорию на '{}'. Не хватает прав.".format(dir))


def remote_file(file):
    print("Вы точно хотите удалить файл '{}'? [y/n]: ".format(file), end='')
    answer = input().strip()
    if answer == 'y' or answer == 'Y':
        if os.path.isdir(file):
            try:
                shutil.rmtree(file)
                print("Директория '{}' удалена".format(file))
            except FileNotFoundError:
                print("Не могу удалить файл '{}'. Такой файл не существует".format(file))
            except PermissionError:
                print("Не могу удалить файл '{}'. Не хватает прав.".format(file))
        else:
            try:
                os.remove(file)
                print("Файл'{}' удален".format(file))
            except FileNotFoundError:
                print("Не могу удалить файл '{}'. Такой файл не существует".format(file))
            except PermissionError:
                print("Не могу удалить файл '{}'. Не хватает прав.".format(file))


def full_path(dir):
    print(os.getcwd())


current_dir = os.getcwd()

do = {
    'cp': copy_file,
    'rm': remote_file,
    'cd': change_directory,
    'ls': full_path,
}

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    val = sys.argv[2]
except IndexError:
    val = None

if key and do.get(key):
    do[key](val)
else:
    print("Задан неверный ключ")
