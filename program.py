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
min_num = int(input("Укажите минимальное число: "))
max_num = int(input("Укажите максимальное число: "))
step_num = (max_num - min_num) / 10
n = min_num
for i in range(10):    
    tmp = []
    for j in range(n):
        tmp_number = rd.randint(-1000000, 1000000)
        tmp.append(tmp_number)
    array.append(tmp)
    n = int(n + step_num)

s1 = "N \ttime,s \t\tmemory, Kb \t" + module_Name + "\n"
s2 = "N;time,s;memory, Kb;" + module_Name + "\n"

n = min_num
#test realize
for i in range(10):
    tracemalloc.start()
    start = time.thread_time()  
    arr = F(array[i])
    finish = time.thread_time()
    size, count = tracemalloc.get_traced_memory()
    s_time = str(finish - start)    
    s1 = s1 + str(n) + "\t" + s_time + "\t\t" + str(count) + "\n"
    s2 = s2 + str(n) + ";" + s_time + ";" + str(count) + "\n"
    tracemalloc.stop()
    n = n + step_num

print(s1)
#print('Time: ' + str(finish - start))      
