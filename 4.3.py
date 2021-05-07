"""
Шифр Цезаря заключается в замене каждого символа входной строки на символ,
находящийся на несколько позиций левее или правее его в алфавите.

Для всех символов сдвиг один и тот же. Сдвиг циклический, т.е. если к последнему символу алфавита
применить единичный сдвиг, то он заменится на первый символ, и наоборот.

Напишите программу, которая шифрует текст шифром Цезаря.

Используемый алфавит -− пробел и малые символы латинского алфавита: ' abcdefghijklmnopqrstuvwxyz'

Формат ввода:
На первой строке указывается используемый сдвиг шифрования: целое число. Положительное число соответствует сдвигу вправо.
На второй строке указывается непустая фраза для шифрования. Ведущие и завершающие пробелы не учитывать.

Формат вывода:
Единственная строка, в которой записана фраза: Result: "..." ,
где вместо многоточия внутри кавычек записана зашифрованная последовательность.
"""
alphabet = ' abcdefghijklmnopqrstuvwxyz'
move = int(input())
phrase = input().strip()
new_phrase=''
for i in range(len(phrase)):
#for i in phrase:
    #phrase=phrase.replace(phrase[i],alphabet[(alphabet.find(phrase[i])+move)%27],1)
    b= alphabet[(alphabet.find(phrase[i]) + move) % 27]
    new_phrase+=b
print(f'Result: "{new_phrase}"')