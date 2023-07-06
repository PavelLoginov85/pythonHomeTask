RLE-сжатие – один из самых простых методов сжатия строки, основанный на сокращении подстрок, состоящих из одинаковых символов. Сжатие осуществляется следующим образом:
Строка разбивается на минимальное количество подстрок, состоящих из одинаковых символов. Например, abbcaaa превращается в строки a, bb, c, aaa.

def coding(data):
    encoding = ''
    prev_letter = ''
    count = 1
    if not data: return ''
    for letter in data:
        if letter != prev_letter:
            if prev_letter:
                encoding += str(count) + prev_letter
            count = 1
            prev_letter = letter
        else:
            count += 1
    else:
        encoding += str(count) + prev_letter
        return encoding
text = coding('AAAFFFFDDCCCAAAAWWWWWEEEEQQQQLLLL')

print('AAAFFFFDDCCCAAAAWWWWWEEEEQQQQLLLL')
print(text)


2.Создайте список из случайных чисел. Найдите номер его последнего локального максимума (локальный максимум — это элемент, 
который больше любого из своих соседей).
import random
num = int(input('Введите количество элементов: '))
array = []
inde = 0
ind_max = 0
big = 0

for i in range(num):
    array.append(random.randint(1, 10))
print(array)
for i in range(1,num-1):
    if array[i - 1] < array[i] > array[i + 1]:
        inde = i
        if ind_max < inde:
            ind_max = inde
            big = array[ind_max]
    
print(f'Элемент {big} на позиции {ind_max + 1}') 


3.Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

import random
array = []
count = int(input('Кол-во элементов: '))
for _ in range(count):
    number = random.randint(1, 9)
    array.append(number)
print(array)

def countation(listt):
    max_repeat = 0
    listt_max = listt[0] 
    for i in range(len(listt)):
        repeat = 0
        for j in range(len(listt)):            
            if listt[j] == listt[i]:
                repeat = repeat + 1
        if repeat > max_repeat:
            max_repeat = repeat
            listt_max = listt[i]
            
    print(f"Цифра {listt_max} встретилась {max_repeat} раз ")
print(countation(array))


4.Создайте список из случайных чисел. Найдите второй максимум.
a = [1, 2, 3] # Первый максимум == 3, второй == 2

import random
array = []
count = int(input('Кол-во элементов: '))
for _ in range(count):
    number = random.randint(1, 1000)
    array.append(number)
print(array)

def max1_max2 (list):
    max1 = list[0]
    max2 = list[0]
    for i in range(len(list)):
        if list[i] > max1:
            max2 = max1
            max1 = list[i]
        elif list[i] > max2:
            max2 = list[i]
    print(f"Второй мах {max2}")

print(max1_max2(array))


---------------------------------------------------------      ----------------------------------      ---------------------------------------
---------------------------------------------------------      ----------------------------------      ---------------------------------------


# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


size = int(input("Укажите размер массива "))
t = 0
count = 0
listNumbers = []
for _ in range(size):
    t += 1
    num = input(f"Введите {t}-ое число массива: ")
    num = int(num)
    listNumbers.append(num)
a = int(input("Укажите число которое нужно найти: "))
print()
for i in listNumbers:
    if i == a:
        count += 1
print(listNumbers)
print(f"В массиве значение {a} встречается {count} раз")



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по 
# величине элемент к заданному числу X. Пользователь в первой 
# строке вводит натуральное число N – количество элементов 
# в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X


size = int(input("Введите размер массива "))
listik = []
n = int(input("Введите  число для сравнения: "))

count_min = n
closest_number = 0
for _ in range(size):
    num = int(input("Введите число "))
    listik.append(num)
    count_min += num
#print(listik)
for i in listik:
    count = 0
    j = i
    if n > j:
        while n!= j:
            j+= 1 
            count +=1
        if count < count_min:
            count_min = count
            closest_number = i

    elif n <= j:
        while n!= j:
            j+= -1 
            count+=1
        if count < count_min:
            count_min = count
            closest_number = i

print()
print(f"Ближе всех к числу {n} число {closest_number} ")
print()
print(listik)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа
# X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# Второй вариант ------------------------

# s = int(input("Введите сумму чисел: "))
# m = int(input("Введите произведение чисел: "))
# x1 = 0
# x2 = 0
# x1 = s - x2
# x2 =  m / x1
# print (x1)
# print(x2)

# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# k = int(input("Введите мах число степени: "))
# a = 2
# list = []
# list = [(i, 2**i) for i in range(1, k+1) ] 
# print(f"Это все целые степени цифры 2 - {list}")




# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество
# монет, которые нужно перевернуть.

# qCoin = int(input("Введите общее число монет "))
# coinEagle = 0
# coinRegko = 0
# for _ in range(qCoin):
#     coin = int(input("Укажите что вверху орёл (1) или решко (0) "))
#     if coin == 1:
#         coinEagle += 1
#         qCoin += - 1
#     elif coin == 0:
#         coinRegko += 1
#         qCoin += - 1
       
# print()
# print()
# if coinEagle > coinRegko:
#     print(f"Проще перевернуть {coinRegko} монет c решкой чем {coinEagle} монет с орлом")
# elif coinRegko > coinEagle:
#     print(f"Проще перевернуть {coinEagle} монет c орлом чем {coinRegko} монет с решкой")
# else:
#     print(f"Монет с решкой {coinEagle} и монет c орлом  {coinRegko} крути что хочешь")

# qCoin = int(input("Введите общее число монет "))
# coinEagle = 0
# coinRegko = 0

# while qCoin > 0:
#     coin = int(input("Укажите что вверху орёл (1) или решко (0) "))
#     if coin == 0:
#         qCoin = qCoin - 1
#         coinRegko += 1
#     elif coin == 1:
#         qCoin = qCoin - 1
#         coinEagle = coinEagle + 1
#     else:
#         print("Вводите 0 или 1")

# print()
# if coinEagle > coinRegko:
#     print(f"Проще перевернуть {coinRegko} монет c решкой чем {coinEagle} монет с орлом")
# elif coinRegko > coinEagle:
#     print(f"Проще перевернуть {coinEagle} монет c орлом чем {coinRegko} монет с решкой")
# else:
#     print(f"Монет с решкой {coinEagle} и монет c орлом  {coinRegko} крути что хочешь")


