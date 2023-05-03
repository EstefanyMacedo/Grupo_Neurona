import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

direct = r"C:\Users\javie\Desktop\Code\ISB\ECG-basal.txt"
# cambiar la dirección dependiendo de la laptop y el archivo a plotear
file = pd.read_csv(direct, sep="\t", header=None)
signal = np.array(file[5])

# Number of sample points
N = 2**10
# sample spacing
T = 1.0 / 1000.0
Fs = 1000
signal1 = signal
print(len(signal1))
signal_fft = np.fft.fft(signal1, N)           # fft magtinud
signal_fft = np.round(np.abs(signal_fft),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
signal_aux = signal_fft/signal_fft.max()     # hallamos el maximo para pasar la magnitud a escala db

with np.errstate(divide='ignore'):
    signal_fft_db = 10*np.log10(signal_aux)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero

F_list = np.linspace(0,Fs/2, N//2)
F = np.round(F_list[np.argmax(signal_fft_db)], 1)   # argmax, encuentra el argumento max en un array

plt.plot(F_list, signal_fft_db)  #10 * np.log10(P / Pref) , decibelios
plt.text(F,0, f"{F}Hz")
plt.grid(linestyle=":")
plt.ylabel("Magnitud (db)")
plt.xlabel("Frecuencias (Hz)")
plt.title("FFT-ECG_Basal_Participante1")
plt.xlim([0,200])
plt.xticks(np.arange(0,200,10))
plt.show()
