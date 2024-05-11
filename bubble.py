import random as rd
A = [rd.randint(-100, 100) for i in range (10)]
print (A)
def Bubble(X: list):
    flag = True
    while(flag):
        flag = False        
        for i in range(len(X)-1):
            tmp = X[i+1]
            if X[i] > tmp:
                X[i+1] = X[i]
                X[i] = tmp
                flag = True
    return X
print(Bubble(A))

    
