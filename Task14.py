# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

print('Введите числа через пробел:')
a = input().split()
b = [a[0]]
for i in range(1, len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            break
        elif j == len(b) - 1:
            b.append(a[i])
print(*b, sep=', ')