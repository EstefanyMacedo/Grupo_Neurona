import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
    
direct = "D:\ISB\isb_emg_lab4\ECG-basal.txt"
# cambiar la dirección dependiendo de la laptop
file = pd.read_csv(direct,sep="\t",header=None)
signal = np.array(file[5][0:int(len(file[5]))])
tiempo = np.arange(0,len(signal)/1000,0.001)
# print(len(signal))
# print(len(tiempo))
# print(file)

# print(file)

plt.rcParams["figure.figsize"]=[15,7.50]
plt.plot(tiempo,signal); plt.xlabel("Time(s)");plt.ylabel("Signal");plt.title("ECG basal");plt.xlim(0,4)
plt.grid(True)
plt.show()

plt.figure(2)
plt.rcParams["figure.figsize"]=[15,7.50]
plt.plot(tiempo,signal); plt.xlabel("Time(s)");plt.ylabel("Signal");plt.title("ECG basal 1 seg");plt.xlim(0,1)
plt.grid(True)
plt.show()