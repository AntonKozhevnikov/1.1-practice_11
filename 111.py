#11.1
from random import randint
def pyz(n):
    per = 0
    a= []
    for i in range(n):
        a.append(randint(0,100))
    print(a)
    for i in range (len(a)):
        for j in range (len(a)-1):
            if a[j] > a[j + 1]:
                per = a[j+1]
                a[j+1] = a[j]
                a[j] = per
    print("После пузырька: ", a)
print(pyz(6))

#11.2 Так как цикл вложенный, сложность алгоритма О(n^2)
    
    
