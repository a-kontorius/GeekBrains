# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
current_dir = os.getcwd()
print(current_dir)

for x in range(1,10):
    new_catalog_name = 'dir_'+str(x)
    new_dir_path = os.path.join(current_dir,new_catalog_name)
    try:
        os.mkdir(new_dir_path)
        print("Каталог '{0}' успешно создан".format(new_dir_path))
    except FileExistsError:
        print("Не могу создать каталог '{}'. Такой каталог уже существует.".format(new_dir_path))
    except PermissionError:
        print("Не могу создать каталог '{0}'. Не хватает прав.".format(new_dir_path))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os

current_dir = '.'
directories = [f for f in os.listdir(current_dir) if os.path.isdir(f)]
print(directories) if len(directories) else print("Текущая директория не содержит папок")

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import shutil

current_direcotry = os.getcwd()
current_file = os.path.join(current_direcotry, os.path.basename(__file__))

file_name, file_extension = os.path.splitext(current_file)
new_file = os.path.join(current_direcotry, file_name + '_copy' + file_extension)

try:
    dst = shutil.copyfile(current_file, new_file)
    print("Копия файла создана:", dst)
except Exception as e:
    print("Не могу создать копию файла. Ошибка:", e.args[1])
