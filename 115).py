from random import randint
list1 = []
for i in range(10):
    list1.append(randint(1, 100))
    list1.sort()
print("1st: ",list1)

list2 = []
for i in range(10):
    list2.append(randint(1, 100))
    list2.sort()
print("2nd: ",list2)

def sort_merge(list1, list2):
    return sorted(list1 + list2)
print(sort_merge(list1,list2))
