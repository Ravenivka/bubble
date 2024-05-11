import tracemalloc
import time
import random as rd
import math
from easygui import *
from pathlib import Path


module_Name = fileopenbox('Выберите модуль', 'Selection', '*.py','*.py')
f_path = module_Name
module_Name = Path(f_path).stem
module = __import__(module_Name)
#func_name = input("Укажите имя метода: ")
#F = getattr(module, func_name) Если хотите указать имя функции отличное от 'sort'
F = module.sort

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

s1 = "\tN \ttime,s \tmemory, Kb \n"
s2 = "N;time,s;memory, Kb \n"

#test realize
for i in range(n+1):
    tracemalloc.start()
    start = time.thread_time()  
    arr = F(array[i])
    finish = time.thread_time()
    size, count = tracemalloc.get_traced_memory()
    s_time = str(finish - start)
    N = int(math.pow(10, i))
    s1 = s1 + str(N) + "\t" + s_time + "\t" + str(count) + "\n"
    s2 = s2 + str(N) + ";" + s_time + ";" + str(count) + "\n"


print(f"Peak memory: {count}")
print('Time: ' + str(finish - start))      
