import numpy as np
import random as rand
import matplotlib.pyplot as plt

arr = np.array([rand.randint(0,2000) for i in range(2000)])
arrnum = [i for i in range(2000)]

arr2 = np.copy(arr)
temp = 0
for i in range(0,(arr2.size - 1)):
    for j in range(i+1,arr2.size):
        if arr2[i] < arr2[j]: 
            temp = arr2[i]
            arr2[i] = arr2[j]
            arr2[j] = temp
            
print("\nМассив:\n", arr,
      "\nОтсортированный массив:\n", arr2,
      "\nМинимальное значение:\t",np.min(arr),
      "\nМаксимальное значение:\t",np.max(arr),
      "\nМедиана:\t\t",np.median(arr),
      "\nСтандартное отклонение:\t",np.std(arr),
      "\nСреднее значение:\t",np.mean(arr),
      "\nДисперсия:\t\t",np.var(arr))

mark = '-------------------------------------------------------------------------------'

plt.figure("FIZTEH:)",figsize = (12,6))

plt.subplot(121)
plt.bar(arrnum,arr)
plt.xlabel("Numbers")
plt.ylabel("Random values")
plt.text(0,np.min(arr),mark,fontsize = 10)
plt.text(0,np.max(arr),mark,fontsize = 10)
plt.text(0,np.median(arr),mark,fontsize = 10)
plt.text(0,np.mean(arr),mark,fontsize = 10)
plt.text(0,np.std(arr),mark,fontsize = 10)

plt.subplot(122)
plt.bar(arrnum,arr2)
plt.xlabel("Numbers")
plt.ylabel("Random values(Sorted)")
plt.text(0,np.min(arr2),mark,fontsize = 10)
plt.text(0,np.max(arr2),mark,fontsize = 10)
plt.text(0,np.median(arr2),mark,fontsize = 10)
plt.text(0,np.mean(arr2),mark,fontsize = 10)
plt.text(0,np.std(arr2),mark,fontsize = 10)

plt.show()

 



