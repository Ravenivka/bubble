import random as rd
import math
from easygui import *
from pathlib import Path

moduleName = fileopenbox('Выберите модуль', 'Selection', '*.py','*.py')
f_path = moduleName
moduleName = Path(f_path).stem
module = __import__(moduleName)

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
