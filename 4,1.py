"""
Кодирование длин серий — это базовый алгоритм сжатия данных.

В этой задаче мы реализуем одну из самых простых его вариантов.

На вход алгоритму подаётся строка, содержащая символы латинского алфавита.
Эта строка разбивается на группы одинаковых символов, идущих подряд ("серии").
Каждая серия характеризуется повторяющимся символом и количеством повторений.
Именно эта информация и записывается в код: сначала пишется длина серии повторяющихся символов, затем сам символ.
У серий длиной в один символ количество повторений будем опускать.
Например, рассмотрим строку

aaabccccCCaB
Разобъём её на серии
aaa b cccc CC a B
После чего закодируем серии и получим итоговую строку, которую и будем считать результатом работы алгоритма.
3ab4c2CaB
"""
from itertools import groupby
inp = input()
#inp='aaabccccCCaB'
res=[]
for i,j in groupby(inp):
    res.append(len(list(j)))
    res.append(i)
for i in res:
    if i==1:
        res.remove(i)
print(*res, sep='')

"""
from itertools import groupby

for i, j in groupby(input()):
    c = len(list(j))
    print(str(c)*(c > 1), i, sep='', end='')
"""


