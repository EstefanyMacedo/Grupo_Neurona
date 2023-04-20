import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

direct = r"C:\Users\javie\Desktop\Code\ISB\segunda_medicion.csv"
# cambiar la dirección dependiendo de la laptop y el archivo a plotear
file = pd.read_csv(direct,sep=";", header=None)
print(file)

exg0 = file.iloc[:,1].values
print(exg0)
exg1 = file.iloc[:,2].values
exg2 = file.iloc[:,3].values
exg3 = file.iloc[:,4].values
exg4 = file.iloc[:,5].values
exg5 = file.iloc[:,6].values
exg6 = file.iloc[:,7].values
exg7 = file.iloc[:,8].values

Fs = 250
time = np.arange(0,len(exg0)/Fs,1/Fs)

# Create a grid of subplots
fig, axs = plt.subplots(4, 1, figsize=(8, 10), sharex=True)

# Plot data in each subplot
axs[0].plot(time, exg0)
axs[1].plot(time, exg1,color="red")
axs[2].plot(time, exg2,color="green")
axs[3].plot(time, exg3,color="black")

# Add titles and labels
axs[0].set(title='EXG Channel 0', ylabel='mV')
axs[1].set(title='EXG Channel 1', ylabel='mV')
axs[2].set(title='EXG Channel 2', ylabel='mV')
axs[3].set(title='EXG Channel 3', ylabel='mV', xlabel='Time')
plt.xlim([0,70])
plt.show()

# Create a grid of subplots
fig2, axs = plt.subplots(4, 1, figsize=(8, 10), sharex=True)

# Plot data in each subplot
axs[0].plot(time, exg4,color="red")
axs[1].plot(time, exg5,color="green")
axs[2].plot(time, exg6,color="black")
axs[3].plot(time, exg7)

# Add titles and labels
axs[0].set(title='EXG Channel 4', ylabel='mV')
axs[1].set(title='EXG Channel 5', ylabel='mV')
axs[2].set(title='EXG Channel 6', ylabel='mV')
axs[3].set(title='EXG Channel 7', ylabel='mV', xlabel='Time')
plt.xlim([0,70])
plt.show()