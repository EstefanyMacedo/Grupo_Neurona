<h1 align="center"> ANÁLISIS BÁSICO DE LA SEÑAL EMG</h1>

## Tabla de Contenidos
+ [Introducción](url)
+ [Interpretación y conclusiones](url)

<h2 align="center">INTRODUCCIÓN</h2>
Las señales electromiográficas (EMG) son señales eléctricas producidas por un músculo durante el proceso de contracción y relajación.

<p align="center">
  <img width="600" height="400"src="https://media.discordapp.net/attachments/781169694949244932/1114649847493038080/9k.png?width=360&height=218">
</p>
<em><p align="center">Figura 1. Señal EMG.</p></em>

<h2 align="center">PROCESAMIENTO</h2>

Se realiza un filtrado a la señal para eliminar ruido y artefactos, para ello se implementó un filtro pasabanda con frecuencias de corte de 10 y 300 Hz. 
![image](https://github.com/EstefanyMacedo/Grupo_Neurona/assets/128627620/ed2a6e00-cb98-40f0-956b-68faf6bd6843)

Posterior a ello se realizó una normalización a la señal para poder comparar y analizar señales EMG de diferentes personas. 
![image](https://github.com/EstefanyMacedo/Grupo_Neurona/assets/128627620/67ec4724-4071-41ab-89e0-97812b3e92aa)

Se obtuvo la señal al cuadrado para poder visualizar la potencia de la señal y detectar los instantes de contracción muscular. Para ello, se determinaron umbrales mínimos y máximos y se representó la acción de contracción mediante un área cuadrada sobre la señal. 

![image](https://github.com/EstefanyMacedo/Grupo_Neurona/assets/128627620/76459e98-57ad-4b27-952a-e6a665ff78aa)

Asimismo, se calcular otras características de utilidad como el RMS (root mean square), área bajo la curva y potencia espectral.
- RMS (Root Mean Square):
El valor RMS es una medida utilizada para cuantificar la amplitud promedio de una señal. Se calcula tomando la raíz cuadrada de la media de los cuadrados de los valores de la señal. El RMS proporciona una medida de la amplitud eficaz de la señal, teniendo en cuenta tanto los valores positivos como los negativos.

- Área bajo la curva:
El área bajo la curva se refiere al cálculo de la integral de una señal en un intervalo de tiempo determinado. Proporciona una medida de la energía o el contenido total de una señal en ese intervalo de tiempo.

- Potencia espectral:
La potencia espectral es una medida utilizada en el dominio de la frecuencia para analizar la distribución de energía de una señal en diferentes frecuencias. Se calcula utilizando la transformada de Fourier de la señal y tomando el valor cuadrado de la magnitud de la transformada.
La potencia espectral proporciona información sobre la distribución de energía de una señal en el dominio de la frecuencia y es útil para identificar las frecuencias dominantes, las características espectrales y los componentes de una señal. 

<h2 align="center">INTERPRETACIÓN Y CONCLUSIONES</h2>
Para el análisis respectivo de las señales electromiográficas, es necesario realizar el tratamiento respectivo de la señal. Primero eliminando la línea base, con el fin de la que las señales están centradas en el cero, como segundo la normalización para que se encuentre en una escala más fácil de interpretar (valores en milivoltios), y como tercer paso el respectivo filtrado, para eliminar ruido de la señal.

Dadas las gráficas para los respectivos músculos del dedo, de la pantorrilla, y del bíceps, se puede apreciar que para el emg del dedo se tienen picos de amplitud con períodos cortos, y por el contrario para los otros dos músculos, la amplitud es prolongada y con picos de similar amplitud por un periodo de tiempo. Esto se debe a que la cantidad de fibras musculares es mayor en los bíceps y pantorrillas, que a diferencia del dedo, que cuenta con menor cantidad de estas fibras.

La cantidad de fibras o grupos musculares involucrados en una acción de contracción del músculo está relacionado a la cantidad de ruido de la señal, caso del emg del bíceps, donde el ruido es mayor y a lo largo de toda la señal a diferencia del emg del dedo.
