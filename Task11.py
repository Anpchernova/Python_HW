#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

print('Введите число:')
N = int(input())
a = []
x = 0
while N >= 1:
    a.append(N % 2)
    N = N // 2
print(*list(reversed(a)), sep='')