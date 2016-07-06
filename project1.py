import random
import numpy as np
import matplotlib.pyplot as plt
ch=[["HH",0],['HT',0],['TH',0],['TT',0]]
for i in range(10000):
    x=random.randint(0,3)
    ch[x][1]+=1
print(ch)
ch=np.array(ch)
ch1=np.array(ch[:,1],'int')
plt.plot(ch1)
plt.yticks(np.arange(2000,4000,100))
plt.xticks([0,1,2,3],ch[:,0])
plt.show()
#on manual HH 13 HT 16 TT 9 TH 12
