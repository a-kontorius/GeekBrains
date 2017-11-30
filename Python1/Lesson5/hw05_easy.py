# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil


def create_folder(folder):
    current_directory = os.getcwd()
    new_dir_path = os.path.join(current_directory, folder)

    try:
        os.mkdir(new_dir_path)
        print("Каталог '{0}' успешно создан".format(new_dir_path))
    except FileExistsError:
        print("Не могу создать каталог '{}'. Такой каталог уже существует.".format(new_dir_path))
    except PermissionError:
        print("Не могу создать каталог '{0}'. Не хватает прав.".format(new_dir_path))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_current_directory():
    directories = [f for f in os.listdir(os.getcwd()) if os.path.isdir(f)]
    [print(dir) for dir in directories] if directories else print("Текущая директория не содержит папок")


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def create_copy_of_file(src_file):
    file_name, file_extension = os.path.splitext(src_file)
    current_direcotry = os.getcwd()
    new_file = os.path.join(current_direcotry, file_name + '_copy' + file_extension)

    try:
        dst = shutil.copyfile(src_file, new_file)
        print("Копия файла создана:", dst)
    except Exception as e:
        print("Не могу создать копию файла. Ошибка:", e.args[1])


if __name__ == "__main__":
    # Задача-1:
    for x in range(1, 10):
        create_folder('dir_' + str(x))

    # Задача-2:
    show_current_directory()

    # Задача-3:
    src_file = os.path.join(os.getcwd(), os.path.basename(__file__))
    create_copy_of_file(src_file)
