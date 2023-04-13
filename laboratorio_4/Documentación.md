<h1 align="center">RECOLECCIÓN DE SEÑALES ELECTROCARDIOGRÁFICAS</h1>

## Tabla de contenidos

+ [Introducción](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#introducci%C3%B3n)
+ [Marco Teórico](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#marco-te%C3%B3rico)
+ [Materiales](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#materiales)
+ [Posicionamiento de electrodos](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#gu%C3%ADas-elect)
+ [Desarrollo del laboratorio](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#se%C3%B1ales-adquiridas-y-comparaci%C3%B3n)
+ [Discusión](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#discusi%C3%B3n)
+ [Archivos](https://github.com/EstefanyMacedo/Grupo_Neurona/tree/main/laboratorio_4/Archivos)
+ [Bibliografía](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#bibliografia)
 <h2 align="center">INTRODUCCIÓN </h2>
En este laboratorio, utilizaremos Bitalino, para medir y analizar señales de electrocardiograma (ECG). El ECG es una señal eléctrica generada por el corazón que se utiliza para diagnosticar una amplia gama de trastornos cardíacos. Aprender a medir y analizar ECG es una habilidad esencial para cualquier persona interesada en la medicina o la ingeniería biomédica. En este laboratorio, exploraremos los fundamentos de la adquisición de señales ECG y las técnicas de análisis de señales necesarias para comprender la información contenida en la señal. 
<h2 align="center">MARCO TEÓRICO</h2>

### La señal de ECG y su importancia

La señal de ECG es importante porque proporciona información valiosa sobre la función cardíaca del paciente. El ECG es una prueba no invasiva que mide la actividad eléctrica del corazón a través de electrodos colocados en la piel del paciente. La señal de ECG se utiliza comúnmente para detectar y diagnosticar trastornos cardíacos, como arritmias, infarto de miocardio, hipertrofia ventricular y otras condiciones que afectan la función cardíaca.

El ECG también puede ser utilizado para monitorizar la actividad cardíaca durante procedimientos médicos y cirugías, para evaluar la eficacia de los tratamientos para trastornos cardíacos y para evaluar la función cardíaca en pacientes con afecciones crónicas, como la insuficiencia cardíaca.

Además, la señal de ECG es una herramienta importante en la investigación médica y la ingeniería biomédica. Los investigadores utilizan la señal de ECG para estudiar la fisiología del corazón y para desarrollar nuevos métodos de diagnóstico y tratamiento de enfermedades cardíacas.

### Primera y segunda derivada en un ECG

La derivada tiene como función mostrar la tasa de cambio en el ECG. La primera derivada es la pendiente de una recta tangente a la curva electrocardiográfica en cualquier punto. En esta derivada, la mayor excursión se observa cuando el ECG muestra la mayor tasa de cambio. De esta forma, los picos agudos se representan como fluctuaciones en la derivada [1].
<p align="center">
  <img width="600" height="400"src="https://user-images.githubusercontent.com/128627158/231569722-862f1343-70f9-4eb7-8d70-2d1c20a4f22c.png">
</p>
<em><p align="center">Figura 1. Picos y valles de una señal de ECG (3).</p></em>
En el caso de la segunda derivada (el mínimo), su pico indica la curvatura máxima al comienzo del inicio de R que, de la misma forma, representa el pico de la onda Q como se muestra en la Figura 1. Esta derivada no depende de la visibilidad de la onda Q ni de la amplitud del pico. Esto le permite convertirse en un indicador fiable del comienzo de R [2].

### Transformada rápida de Fourier (FFT)
La transformada rápida de Fourier es una herramienta que nos permite conocer qué frecuencias de onda sinusoidal componen una señal. La FFT convierte una señal en componentes espectrales individuales y, por lo tanto, proporciona información de frecuencia sobre la señal [4]. Es por ello que se aplicó la transformada rápida de Fourier a las señales adquiridas:

<h2 align="center">MATERIALES</h2>

<div align="center">

|   **Dispositivo**   | **Descripción** |  **Imagen**  |
|:-------------------:|:---------------:|:------------:|
| BiTalino | FALTA INFO |<img width="200" height="150" src="https://user-images.githubusercontent.com/128627158/231564649-f925e135-93c4-434d-85a4-03b62ff1b628.jpg">|
|       Electrodos      |FALTA INFO |<img width="200" height="150" src="https://user-images.githubusercontent.com/128627158/231566660-9f4676ba-484a-43a2-9236-3595947a1528.jpg">|
|  ProSim 4 vital signal simulator | FALTA INFO |<img width="200" height="150" src="https://user-images.githubusercontent.com/128627158/231566784-4ebd9dc8-586b-4b42-91f6-b3c9daa4a92c.jpg">|


</div>

<h2 align="center">POSICIONAMIENTO DE ELECTRODOS</h2>

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

<h2 align="center">DESARROLLO DEL LABORATORIO</h2>

Durante esta experiencia de laboratorio se realizaron 3 tomas de datos en circunstancias diferentes: Estado basal, aguantando la respiración y después de realizar ejercicio de cardio.

## Sujeto N°1

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

### Resultados:

<p float="center">
  <img src="https://user-images.githubusercontent.com/128627158/231589427-01596550-8895-44ab-907d-f58f5f6a54cd.jpg" width="500" />
  <img src="https://user-images.githubusercontent.com/128627158/231590017-67aeace6-a990-48d6-b00e-335a31eb23c1.jpg" width="500" /> 
</p>
<em><p align="center">Datos graficados en el software Opensignals y Python, respectivamente</p></em>
 
### Toma de datos luego de una actividad física aeróbica:
 
 
### Resultados:
 
 

## Discusión:
 
Como se puede observar en la grabacion e imagenes colocadas, el sensor para EKG del bitalino muestra resultados esperados relativamente buenos al momento de probar
y experimentar con un sujeto real, ya que si bien todas las ondas y formas de los complejos se ven  correctos, existe ruido presente en la onda, producto muchas veces 
de como estan colocados los electrodos en el cuerpo y sus ubicaciones respectivas (tipo de derivación), el tipo de electrodos utilizados, alguna jolleria presente,   carga estatica y/o electrica en el ambiente donde se realiza la medición, etc. 
 
Por otro lado es evidente al comparar las graficas entre el estado basal y luego de haber realizado la actividad fisica, una disminucion del periodo entre onda y onda del EKG (entre complejos P-QRS-T respectivamente), esto es debido a un incremento en la frecuencia cardiaca del sujeto y si bien la amplitud se ve mas reducida para el segundo caso, es simplemente la escala que el programa utiliza para visualizar las ondas de mejor manera, ya que luego de reposar o al aguantar la respiracioón y volver a respirar con normalidad, existen picos mas altos con respecto al momento de tener una frecuencia mayor. Asi mismo el tema del ruido es incrementado en las graficas luego de haber realizado una actividad fisica, lo cual disminuye una vez el sujeto reposa y recupera su frecuencia cardiaca normal.


 
 
## Sujeto N°2

### Colocación de los electrodos
 

### Toma de datos en reposo:
 

### Toma de datos luego de una actividad física aeróbica:
 
 
### Resultados:

## Discusión:
Para el segundo sujeto, al analizar las ondas se cumple el mismo patron en la onda y complejos típicos de un EKG; la unica diferencia que se puede notar es que al realizar la actividad fisica respectiva y comparando con la grafica de estado basal, la frecuencia con la que las ondas aparecen entre complejo y complejo es menor que para el primer sujeto, esto puede ser debido a muchos factores, entre los cuales destaca el hecho de que el segundo sujeto realiza actividad aerobica frecuente, pudiendo asi controlar su frecuencia cardiaca con mayor facilidad y reponerse de manera más rápida.
 
### ProSim-8:
 
 

Discusión: 
Analizando respecto a la salida obtenida para un EKG con el simulador ProSim-8 de la marca fluke, se puede observar un onda con sus complejos de manera mas limpia, libre de ruidos. Esto es debido a que al ser un simulador y contar con parametros que uno mismo como usuario puede establecer, el simulador se encargara de mantenerlas y enviarlas al programa para la visualizacion de las ondas respectivas, lo cual en un sujeto real, al ser un sistema biologico, suceptible a diferentes interferencias del medio que lo rodea presentes (carga del ambiente, vellosidades, tipos de electrodos usados, posicionamiento, etc ) como mencionamos anteriormente, las graficas obtenidas contaran con un ruido presente el cual puede ser atenuado mediantes filtros tanto analogicos como digitales, cosa que el simulador realiza de antemano antes de mandar la señal de onda al programa.

## Bibliografia
1.	Langner P. First Derivative of the Electrocardiogram [Internet]. [citado el 12 de abril de 2023]. Disponible en: https://www.ahajournals.org/doi/pdf/10.1161/01.RES.10.2.220#:~:text=The%20derivative%20shows%20the%20rate,changing%20low%20frequency%20wave%20forms.
2.	Zauner J. Ocular light effects on human autonomous function: the role of intrinsically photosensitive retinal ganglion cell sensitivity and time of day [Internet]. Disponible en: https://edoc.ub.uni-muenchen.de/30150/7/Zauner_Johannes.pdf
3.	Ay Gül AN. Real-time feature extraction of ECG signals using NI LabVIEW.
4. FFT. (n.d.). Nti-audio.com. Retrieved April 12, 2023, from https://www.nti-audio.com/en/support/know-how/fast-fourier-transform-fft 
5.	PLUX Biosignals. How do I know I am alive? [Internet]. [citado el 12 de abril de 2023]. Disponible en: https://www.pluxbiosignals.com/blogs/informative/how-do-i-know-i-am-alive
