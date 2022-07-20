#Реализуйте программу, которая будет вычислять количество различных объектов в списке.
#Два объекта a и b считаются различными, если a is b равно False.

#Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100 объектов. Выведите количество различных объектов в этом списке.

#Формат ожидаемой программы:

#ans = 0
#for obj in objects: # доступная переменная objects
#   ans += 1
#print(ans)

#Примечание:
#Количеством различных объектов называется максимальный размер множества объектов, в котором любые два объекта являются различными.

#Рассмотрим пример:
#objects = [1, 2, 1, 2, 3] # будем считать, что одинаковые числа соответствуют одинаковым объектам, а различные – различным

#Тогда все различные объекты являют собой множество {1, 2, 3}﻿. Таким образом, количество различных объектов равно трём.
object = [1,4,5,6,67,7,8,9]
ans = 0
matches = 0
for i in range(len(objects)):
    for j in range(i + 1, len(objects)):
        if objects[j] is objects[i]:
            matches += 1
    if matches == 0:
        ans += 1
    matches = 0
print(ans)