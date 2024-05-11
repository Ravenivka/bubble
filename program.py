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

  



print(F(array[1]))        
