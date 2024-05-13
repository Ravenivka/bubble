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
step_num = (max_num - min_num) / 9
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
    s_time = finish - start
    s1 = s1 + "{0}\t{1:9.3f}\t{2}\n".format(n, s_time, count)
    s2 = s2 + str(n) + ";" + str(s_time) + ";" + str(count) + ";\n"
    tracemalloc.stop()
    n = int(n + step_num)

print(s1)
flag = input("Вывести результат в файл? y/n: ")
if flag == "y":
    file_name = module_Name + '.csv'
    with open(file_name, 'a') as f:
        f.write(s2)
        print("Данные записаны")    
