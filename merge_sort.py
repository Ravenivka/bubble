#merge sort
#Производительность алгоритма O(N log N) 
import random

N = int(input('Задайте размер массива '))
rndarray = list()
for i in range(N):
    rndarray.append(random.randint(-100, 100))

print ('Массив случайных чисел')
print (rndarray)

def merge_sort(nums): 
    if len(nums) > 1: 
        mid = len(nums)//2
        left = nums[:mid] 
        right = nums[mid:]
        left=merge_sort(left) 
        right=merge_sort(right) 
        i = j = k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                nums[k] = left[i] 
                i+=1
            else: 
                nums[k] = right[j] 
                j+=1
            k+=1
        while i < len(left): 
            nums[k] = left[i] 
            i+=1
            k+=1
        while j < len(right): 
            nums[k] = right[j] 
            j+=1
            k+=1
    return nums
 
    
    

            

    


print ('Массив отсортированных чисел')
print(merge_sort(rndarray))
