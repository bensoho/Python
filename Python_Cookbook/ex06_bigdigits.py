#!/usr/bin/env python3
#print big digits.py
import sys

zero = ['* * * * * * *','*           *','*           *','*           *','*           *','*           *','*           *','*           *','*           *','*           *','* * * * * * *']
one = ['            *','            *','            *','            *','            *','            *','            *','            *','            *','            *','            *']
two = ['* * * * * * *','            *','            *','            *','            *','* * * * * * *','*            ','*            ','*            ','*            ','* * * * * * *',]
three = ['* * * * * * *','            *','            *','            *','            *','* * * * * * *','            *','            *','            *','            *','* * * * * * *',]
four = ['*           *','*           *','*           *','*           *','*           *','* * * * * * *','            *','            *','            *','            *','            *',]
five = ['* * * * * * *','*            ','*            ','*            ','*            ','* * * * * * *','            *','            *','            *','            *','* * * * * * *',]
six = ['* * * * * * *','*            ','*            ','*            ','*            ','* * * * * * *','*           *','*           *','*           *','*           *','* * * * * * *',]
seven = ['  * * * * * *','            *','            *','            *','            *','            *','            *','            *','            *','            *','            *',]


eight = ['* * * * * * *','*           *','*           *','*           *','*           *','* * * * * * *','*           *','*           *','*           *','*           *','* * * * * * *',]
nine = ['* * * * * * *','*           *','*           *','*           *','*           *','* * * * * * *','            *','            *','            *','            *','* * * * * * *',]

Digits = [zero,one,two,three,four,five,six,seven,eight,nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 11:
        line = ''
        column = 0
        while column < len(digits):
            number = int(digits[column]) #number = 0
            digit = Digits[number] #digit = [' list with *  ']
            # Here we transfer digit list with digit number in stead of '*' 
            for c in digit[row]:
                if c == '*':
                    c = str(number)
                line += c
            line += '    '
            column += 1
        print(line)
        row += 1

except IndexError:
    print('usage: bigdigits.py <number>')

