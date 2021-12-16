#11.3
from random import randint
def pod(n):
    b = 0
    c = []

    for i in range(n):
        c.append(randint(1, 100))
    print(c)

    a = []
    for f in range(101):
        a += [0]
    for f in c:
        a[f] += 1

    for q in range(101):
        if a[q] > 0:
            for r in range(a[q]):
                c[b] = q
                b += 1
    print('После сортировки подсчётом', c)

print(pod(5))

#11.4 Мы считаем количество встречающихся чисел в массиве для каждого элемента
#потом заполнячем массив числами, в количестве посчитаном ранее для каждого числа
#Значит сложность O(n) 
