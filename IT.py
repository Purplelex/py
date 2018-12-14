import matplotlib.pyplot as plt
import random as rand

values = []
string = []
for i in range(26):
    values.append(rand.randint(11,99))
for i in range(len(values)-1):
    for j in range(i+1,26):
        if values[i]==values[j]:
            while(values[i]==values[j]):
                values[i]=rand.randint(11,99)
for i in range(32,128):
    if 'a' <= chr(i) <= 'z':
        string.append(chr(i))

plt.figure(1,figsize=(18,9))

plt.subplot(131)
plt.bar(string,values)
plt.subplot(132)
plt.scatter(string,values)
plt.subplot(133)
plt.plot(string,values)
plt.suptitle('Some Data Science')
plt.show()
