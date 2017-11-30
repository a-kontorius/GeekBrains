# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
a = [1, 5, 12, 44.82, 57, 82, 27.9]
b = [x ** 2 for x in a]
print(b)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits_a = ['яблоко', 'банан', 'груша', 'киви', 'хурма']
fruits_b = ['груша','киви','яблоко','абрикос','гранат']
fruits = [x for x in fruits_a if x in fruits_b]
print(fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
'avrora'

a = [random.randint(-100,100) for _ in range(50)]
b = [x for x in a if not x % 3 and x % 4 and x >=0]
print(a)
print(b)