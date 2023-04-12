# RECOLECCIÓN DE SEÑALES ELECTROCARDIOGRÁFICAS

## Tabla de Contenidos
+ [Introducción](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#breve-introducci%C3%B3n)
+ [Marco Teórico](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#marco-te%C3%B3rico)
+ [Materiales](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#materiales)
+ [Posicionamiento de electrodos](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#gu%C3%ADas-elect)
+ [Desarrollo del laboratorio](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#se%C3%B1ales-adquiridas-y-comparaci%C3%B3n)
+ [Discusión](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#discusi%C3%B3n)
+ [Archivos](https://github.com/EstefanyMacedo/Grupo_Neurona/tree/main/laboratorio_4/Archivos)
+ [Bibliografía](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#bibliografia)
## Introducción
eso lo pone jesús a
## Marco teórico
### Primera y segunda derivada en un ECG

La derivada tiene como función mostrar la tasa de cambio en el ECG. La primera derivada es la pendiente de una recta tangente a la curva electrocardiográfica en cualquier punto. En esta derivada, la mayor excursión se observa cuando el ECG muestra la mayor tasa de cambio. De esta forma, los picos agudos se representan como fluctuaciones en la derivada [1].
<p align="center">
  <img width="600" height="400"src="https://user-images.githubusercontent.com/128627158/231569722-862f1343-70f9-4eb7-8d70-2d1c20a4f22c.png">
</p>
<em><p align="center">Figura 1. Picos y valles de una señal de ECG (3).</p></em>
En el caso de la segunda derivada (el mínimo), su pico indica la curvatura máxima al comienzo del inicio de R que, de la misma forma, representa el pico de la onda Q como se muestra en la Figura 1. Esta derivada no depende de la visibilidad de la onda Q ni de la amplitud del pico. Esto le permite convertirse en un indicador fiable del comienzo de R [2].
### Transformada rápida de Fourier (FFT)
La transformada rápida de Fourier es una herramienta que nos permite conocer qué frecuencias de onda sinusoidal componen una señal. La FFT convierte una señal en componentes espectrales individuales y, por lo tanto, proporciona información de frecuencia sobre la señal [4]. Es por ello que se aplicó la transformada rápida de Fourier a las señales adquiridas:


## Materiales
| --- | Materiales | Imagen referencial|
|--- | --- | ---|
| #1 | BiTalino |![304214-17590223](https://user-images.githubusercontent.com/128627158/231564649-f925e135-93c4-434d-85a4-03b62ff1b628.jpg)|
| #2 | Electrodos | ![electrodo-de-superficie-circular-50mm-10551605z0-22432241](https://user-images.githubusercontent.com/128627158/231566660-9f4676ba-484a-43a2-9236-3595947a1528.jpg) |
|#3|ProSim 4 vital signal simulator| ![fb-prosim4_02b_c](https://user-images.githubusercontent.com/128627158/231566784-4ebd9dc8-586b-4b42-91f6-b3c9daa4a92c.jpg)| 


## Posicionamiento de electrodos:
Se realizó el sistema de 3 electrodos considerando la cresta iliaca como referencia. En Figura 2, se muestra a detalle el sistema planteado. Se observa que en la muñeca izquierda, se encuentra el polo positivo (+); en la derecha, el polo negativo (-); y en la cresta iliaca la referencia. Este posicionamiento permite colocar los electrodos en zonas de baja actividad muscular para reducir el ruido de la activación de los músculos causada por diferentes actividades realizadas por el usuario como moverse o manipular objetos [5]. 

<p align="center">
  <img width="500" height="300"src="https://user-images.githubusercontent.com/128627158/231569119-e8a812d9-ce8a-4ceb-ab99-8945dccd9e4a.jpg">
</p>
<em><p align="center">Figura 2. Posicionamiento de los electrodos en el cuerpo [5].</p></em>
Se tomaron referencias de la colocación de los electrodos y buenas prácticas durante la toma de datos las presentes guías:
* a

Lo más resaltante es que el paciente esté en una posición cómoda, relajado, sin ningún objeto metálico y que el lugar donde se 
coloquen los respectivos electrodos sobre la piel este limpia.
Además, se debe asegurar la correcta colocación de los electrodos positivo, negativo y de referencia en sus respectivos lugares según indican las guías consultadas.

## Desarrollo del laboratorio:
### SUJETO N°1

### Colocación de los electrodos

<p float="right">
  <img src="https://user-images.githubusercontent.com/128627158/231570991-32bfd77a-3e97-4edc-94ee-b2ab51dd409a.jpg" width="500" />
  <img src="https://user-images.githubusercontent.com/128627158/231580875-39fe927c-b4b3-49d4-94dc-b51752e64f63.png" width="500" /> 
</p>
<em><p align="center">Ubicación de los electrodos</p></em> 

### Toma de datos en reposo:

Esta toma de datos, nos permite registrar una referencia basal del ECG cuando el sujeto se encuentra en reposo.

<div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/231582212-aa004901-4b90-42d4-8d26-320108efb6da.mp4">
</div>
<em><p align="center">Toma de datos en reposo</p></em>

#### Procesamiento de los datos en Python

<p align="center">
  <img width="560" height="300"src="https://user-images.githubusercontent.com/128627158/230188757-c65fbb6e-83a7-41be-9111-180fc0f4424e.jpeg">
</p>

<em><p align="center">Gráfica obtenida en Opensignal de la señal mioeléctrica</p></em>

#### Comparación de gráficas obtenidas y vídeo de la toma de datos
<p align="center">
  <img width="700" height="600"src="https://user-images.githubusercontent.com/128627158/230194010-d18b37f1-48bd-4cfc-8599-fbc1091500e8.jpg">
</p>
<em><p align="center">Comparación de ambas gráficas obtenidas</p></em>

<div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/230207238-a84a00f7-d3e3-4084-a2e5-456a6b52ef43.mp4">

</div>

<em><p align="center">Vídeo de la toma de datos</p></em>
### Segunda señal &rarr; Nervio del cuadrado femoral
Ubicación: Pantorrilla derecha

<p align="center">
  <img width="200" height="300"src="https://user-images.githubusercontent.com/128627158/230196679-79cb4509-277c-4f0a-9a19-c0dff8b4d270.jpeg">
</p>
<em><p align="center">Ubicación de los electrodos</p></em>

El nervio del cuadrado femoral provee inervación al músculo cuadrado femoral y al músculo gemelo inferior. Como se aprecia en la Figura, mientras la persona se mantiene en reposo en el suelo, los valores de voltaje se encuentran muy cercanos a cero. Por otro lado, al aplicar una fuerza externa en el cuerpo hacia abajo, los valores de voltaje aumentan significativamente hasta alcanzar un máximo de amplitud de 2 mV.

<p align="center">
  <img width="560" height="300"src="https://user-images.githubusercontent.com/128627158/230199303-83e05c28-5b58-45b0-af26-db36664c8b9d.jpeg">
</p>
<em><p align="center">Gráfica obtenida en Opensignals de la señal mioeléctrica</p></em>

#### Procesamiento de los datos en Python
<p align="center">
  <img width="560" height="300"src="https://user-images.githubusercontent.com/128627158/230199508-b295963e-a66b-42a3-8101-96cbba6dcd1d.jpeg">
</p>

<em><p align="center">Gráfica obtenida en Opensignal de la señal mioeléctrica</p></em>

#### Comparación de gráficas obtenidas y vídeo de la toma de datos
<p align="center">
  <img width="700" height="700"src="https://user-images.githubusercontent.com/128627158/230200477-7a949465-32aa-4bc0-bea8-6d2e7612059b.jpg">
</p>
<em><p align="center">Comparación de ambas gráficas obtenidas</p></em>

<div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/230205987-0129f298-7a0e-440e-bdcf-172f2410fb8f.mp4">

</div>

<em><p align="center">Vídeo de la toma de datos</p></em>
### Tercera señal &rarr; Nervio radial
Ubicación: Dedo pulgar izquierdo

<p align="center">
  <img width="460" height="300"src="https://user-images.githubusercontent.com/128627158/230202714-87c61c32-f950-4203-b62d-9bdd203bbe89.jpeg">
</p>
<em><p align="center">Ubicación de los electrodos</p></em>

Principalmente, el nervio radial inerva los músculos posteriores del antebrazo. En la Figura, se aprecia el cambio significativo en la gráfica al mantener el dedo pulgar relajado y al aplicar una fuerza externa (flexión).
Cuando no se aplica alguna fuerza directamente, la señal presenta un valor constante de aproximadamente 0 mV. Por el contrario, cuando se aplica una fuerza externa, el voltaje aumenta hasta aproximadamente 2 mV.

<p align="center">
  <img width="460" height="300"src="https://user-images.githubusercontent.com/128627158/230203230-95122fc2-16e3-4f0d-8795-0f23815ffb39.jpeg">
</p>
<em><p align="center">Gráfica obtenida en Opensignals de la señal mioeléctrica</p></em>

#### Procesamiento de los datos en Python
<p align="center">
  <img width="460" height="300"src="https://user-images.githubusercontent.com/128627158/230202864-414b027c-7e77-4d28-94b4-a13ebc366af8.jpeg">
</p>

<em><p align="center">Gráfica obtenida en Opensignal de la señal mioeléctrica</p></em>

#### Comparación de gráficas obtenidas y vídeo de la toma de datos
<p align="center">
  <img width="700" height="700"src="https://user-images.githubusercontent.com/128627158/230204380-c5cc89ad-8d3f-4c69-a66b-ccb0ff2eac62.jpg">
</p>
<em><p align="center">Comparación de ambas gráficas obtenidas</p></em>

<div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/230207106-6128a020-58e5-4b95-a607-6b6bb6e54ac3.mp4">

</div>

<em><p align="center">Vídeo de la toma de datos</p></em>
## Discusión:

## Bibliografia
1.	Langner P. First Derivative of the Electrocardiogram [Internet]. [citado el 12 de abril de 2023]. Disponible en: https://www.ahajournals.org/doi/pdf/10.1161/01.RES.10.2.220#:~:text=The%20derivative%20shows%20the%20rate,changing%20low%20frequency%20wave%20forms.
2.	Zauner J. Ocular light effects on human autonomous function: the role of intrinsically photosensitive retinal ganglion cell sensitivity and time of day [Internet]. Disponible en: https://edoc.ub.uni-muenchen.de/30150/7/Zauner_Johannes.pdf
3.	Ay Gül AN. Real-time feature extraction of ECG signals using NI LabVIEW.
4. FFT. (n.d.). Nti-audio.com. Retrieved April 12, 2023, from https://www.nti-audio.com/en/support/know-how/fast-fourier-transform-fft 
5.	PLUX Biosignals. How do I know I am alive? [Internet]. [citado el 12 de abril de 2023]. Disponible en: https://www.pluxbiosignals.com/blogs/informative/how-do-i-know-i-am-alive
