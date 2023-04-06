import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
    
direct = "C:/Code Justfun/isb_emg_lab3/dedo.txt"
# cambiar la dirección dependiendo de la laptop y el archivo a plotear
file = pd.read_csv(direct,sep="\t",header=None)
signal = np.array(file[5])
tiempo = np.arange(0,len(signal)/1000,0.001)
print(len(signal))
print(len(tiempo))
print(file)

print(file)

plt.rcParams["figure.figsize"]=[12,7.50]
plt.plot(tiempo,signal); plt.xlabel("Time(s)");plt.ylabel("Signal");plt.title("EMG Dedo Pulgar")
plt.grid(True)
plt.show()
