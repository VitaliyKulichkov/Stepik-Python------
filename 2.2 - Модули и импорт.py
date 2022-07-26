# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
#
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.
#
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta для прибавления дней к дате.

# put your python code here
from datetime import date, timedelta
inp1 = list(map(int, input().split()))
inp2 = int(input())

date = date(*inp1)
days = timedelta(days=inp2)
result = date + days

print(result.year, result.month, result.day)