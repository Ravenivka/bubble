import random as rd
import math
import bubble


#arrays array create
array = []
n = int(input("Укажите масимальную степень десяти для длины массива: "))
for i in range(n+1):
    N = int(math.pow(10, i))
    tmp = []
    for j in range(N):
        tmp_number = rd.randint(-1000000, 1000000)
        tmp.append(tmp_number)
    array.append(tmp)

print("Выбор метода сортировки:\n")
print("\t0 - сортировка пузырьком\n")
print("\t1 - timsort\n")    
method = int(input("\t2 - radix sort: "))

F = None
match method:
    case 0:
        F = bubble.Bubble


print(F(array[1]))        
