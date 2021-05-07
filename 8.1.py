"""
Напишите простой интерпретатор математического выражения.

На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором:
a operator b, где вместо operator могут использоваться следующие слова: plus, minus, multiply, divide для,
соответственно, сложения, вычитания, умножения и целочисленного деления.
"""
a, operator, b = input().split()
ops={
    'plus': lambda a, b: a + b,
    'minus': lambda a,b: a - b,
    'multiply': lambda a,b: a * b,
    'divide': lambda a,b: a // b
}
print(ops[operator](int(a),int(b)))