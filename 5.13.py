"""
На вход программе подаётся строка, содержащая слова, разделённые пробелом.
Программа должна вывести статистику длин слов в полученной строке, от меньшей длины слова к большей (см. пример).

Словом считается последовательность произвольных символов, окружённая пробелами либо границами строки.
Заметьте, что знаки препинания также относятся к слову.

Формат ввода:
Одна строка, содержащая последовательности латинских символов и знаков препинания, разделённые пробелом.

Формат вывода:
Для каждой длины слова, встречающейся в исходной строке, нужно указать количество слов с такой длиной
длина: количество
Статистика должна выводиться в порядке увеличения длины.
"""
words_lens = {}
for i in input().split():
    if len(i) in words_lens:
        words_lens[len(i)] += 1
    else:
        words_lens[len(i)] = 1
words_lens = dict(sorted(words_lens.items(), key=lambda x: x[0]))
for items in words_lens.items():
    print(items[0], ': ', items[1])
