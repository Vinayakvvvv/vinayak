import numpy as np
import random 
class Random:
    def RandomMain():
        arr_1=np.random.randint(10,90,15)
        arr_2=np.random.randint(10,90,15)
        arr_3=np.random.randint(10,90,15)
        print(arr_1)
        print(arr_2)
        print(arr_3)
        arr_1=np.array_spilt(arr_1,1)
        arr_2=np.array_split(arr_1,1)
        arr_3=np.array_split(arr_1,1)
        print(arr_1)
        print(arr_2)
        print(arr_3)
        
Random.RandomMain()