#Задача 2: Найдите сумму цифр трехзначного числа.

print("Введите число")
array_string = input()

str = list(array_string)
count_array = len(str)
print(str)
s = 0
for i in range(count_array):
    str[i] = int(str[i])

    s = s + str[i]

print(s)