<h1 align="center">RECOLECCIÓN DE SEÑALES ELECTROCARDIOGRÁFICAS</h1>

## Tabla de contenidos

+ [Introducción](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#introducci%C3%B3n)
+ [Marco Teórico](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#marco-te%C3%B3rico)
+ [Materiales](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#materiales)
+ [Posicionamiento de electrodos](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#gu%C3%ADas-elect)
+ [Desarrollo del laboratorio](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#se%C3%B1ales-adquiridas-y-comparaci%C3%B3n)
+ [Discusiones](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#discusiones)
+ [Archivos](https://github.com/EstefanyMacedo/Grupo_Neurona/tree/main/laboratorio_4/Archivos)
+ [Bibliografía](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#bibliografia)
 <h2 align="center">INTRODUCCIÓN </h2>
En este laboratorio, utilizaremos Bitalino, para medir y analizar señales de electrocardiograma (ECG). El ECG es una señal eléctrica generada por el corazón que se utiliza para diagnosticar una amplia gama de trastornos cardíacos. Aprender a medir y analizar ECG es una habilidad esencial para cualquier persona interesada en la medicina o la ingeniería biomédica. En este laboratorio, exploraremos los fundamentos de la adquisición de señales ECG y las técnicas de análisis de señales necesarias para comprender la información contenida en la señal. 
<h2 align="center">MARCO TEÓRICO</h2>

### La señal de ECG y su importancia

La señal de ECG es importante porque proporciona información valiosa sobre la función cardíaca del paciente. El ECG es una prueba no invasiva que mide la actividad eléctrica del corazón a través de electrodos colocados en la piel del paciente. La señal de ECG se utiliza comúnmente para detectar y diagnosticar trastornos cardíacos, como arritmias, infarto de miocardio, hipertrofia ventricular y otras condiciones que afectan la función cardíaca [1].

El ECG también puede ser utilizado para monitorizar la actividad cardíaca durante procedimientos médicos y cirugías, para evaluar la eficacia de los tratamientos para trastornos cardíacos y para evaluar la función cardíaca en pacientes con afecciones crónicas, como la insuficiencia cardíaca [2].

Además, la señal de ECG es una herramienta importante en la investigación médica y la ingeniería biomédica. Los investigadores utilizan la señal de ECG para estudiar la fisiología del corazón y para desarrollar nuevos métodos de diagnóstico y tratamiento de enfermedades cardíacas [3].

<p align="center">
  <img width="600" height="400"src="https://www.heart.org/-/media/Images/Health-Topics/Arrhythmia/ECG-normal.jpg">
</p>
<em><p align="center">Figura 1. Señal ECG.</p></em>

### Primera y segunda derivada en un ECG

La derivada tiene como función mostrar la tasa de cambio en el ECG. La primera derivada es la pendiente de una recta tangente a la curva electrocardiográfica en cualquier punto. En esta derivada, la mayor excursión se observa cuando el ECG muestra la mayor tasa de cambio. De esta forma, los picos agudos se representan como fluctuaciones en la derivada [4].
<p align="center">
  <img width="600" height="400"src="https://user-images.githubusercontent.com/128627158/231569722-862f1343-70f9-4eb7-8d70-2d1c20a4f22c.png">
</p>
<em><p align="center">Figura 2. Picos y valles de una señal de ECG [5].</p></em>
En el caso de la segunda derivada (el mínimo), su pico indica la curvatura máxima al comienzo del inicio de R que, de la misma forma, representa el pico de la onda Q como se muestra en la Figura 2. Esta derivada no depende de la visibilidad de la onda Q ni de la amplitud del pico. Esto le permite convertirse en un indicador fiable del comienzo de R [5].

### Transformada rápida de Fourier (FFT)
La transformada rápida de Fourier es una herramienta que nos permite conocer qué frecuencias de onda sinusoidal componen una señal. La FFT convierte una señal en componentes espectrales individuales y, por lo tanto, proporciona información de frecuencia sobre la señal [7]. Es por ello que se aplicó la transformada rápida de Fourier a las señales adquiridas.

<h2 align="center">MATERIALES</h2>

<div align="center">

|   **Dispositivo**   | **Descripción** |  **Imagen**  |
|:-------------------:|:---------------:|:------------:|
| BiTalino | Kit de desarrollo de bajo costo que permite medir diferentes señales biomédicas |<img width="200" height="150" src="https://user-images.githubusercontent.com/128627158/231564649-f925e135-93c4-434d-85a4-03b62ff1b628.jpg">|
|       Electrodos      | Dispositivos que se utilizan para medir la actividad eléctrica de los tejidos biológicos. Se colocan en la superficie de la piel y detectan la actividad eléctrica |<img width="200" height="150" src="https://user-images.githubusercontent.com/128627158/231566660-9f4676ba-484a-43a2-9236-3595947a1528.jpg">|
|  ProSim 4 vital signal simulator | Simulador portátil utilizado para evaluar la precisión y el rendimiento de los equipos médicos de monitoreo y diagnóstico. Puede simular una amplia gama de señales fisiológicas |<img width="200" height="150" src="https://user-images.githubusercontent.com/128627158/231566784-4ebd9dc8-586b-4b42-91f6-b3c9daa4a92c.jpg">|


</div>

<h2 align="center">POSICIONAMIENTO DE ELECTRODOS</h2>

Se realizó el sistema de 3 electrodos considerando la cresta iliaca como referencia. En Figura 2, se muestra a detalle el sistema planteado. Se observa que en la muñeca izquierda, se encuentra el polo positivo (+); en la derecha, el polo negativo (-); y en la cresta iliaca la referencia. Este posicionamiento permite colocar los electrodos en zonas de baja actividad muscular para reducir el ruido de la activación de los músculos causada por diferentes actividades realizadas por el usuario como moverse o manipular objetos [8]. 

<p align="center">
  <img width="500" height="300"src="https://user-images.githubusercontent.com/128627158/231569119-e8a812d9-ce8a-4ceb-ab99-8945dccd9e4a.jpg">
</p>
<em><p align="center">Figura 3. Posicionamiento de los electrodos en el cuerpo [8].</p></em>
Se tomaron referencias de la colocación de los electrodos y buenas prácticas durante la toma de datos las presentes guías:
* a

Lo más resaltante es que el paciente esté en una posición cómoda, relajado, sin ningún objeto metálico y que el lugar donde se 
coloquen los respectivos electrodos sobre la piel este limpia.
Además, se debe asegurar la correcta colocación de los electrodos positivo, negativo y de referencia en sus respectivos lugares según indican las guías consultadas.

<h2 align="center">DESARROLLO DEL LABORATORIO</h2>

Durante esta experiencia de laboratorio se realizaron 3 tomas de datos en circunstancias diferentes: Estado basal, aguantando la respiración y después de realizar ejercicio de cardio.
Posteriormente, se procesaron las señales en Python tanto en el rango del tiempo, como en el de la frecuencia, esto con la finalidad de tener un mejor análisis de los resultados. Para esta última acción se ultilizó la Transformada de Fourier y la Transformada de Wavelet.


<h2 align="center">Sujeto 1</h2>

### COLOCACIÓN DE LOS ELECTRODOS

<p float="right">
  <img src="https://user-images.githubusercontent.com/128627158/231570991-32bfd77a-3e97-4edc-94ee-b2ab51dd409a.jpg" width="500" />
  <img src="https://user-images.githubusercontent.com/128627158/231580875-39fe927c-b4b3-49d4-94dc-b51752e64f63.png" width="500" /> 
</p>
<em><p align="center">Ubicación de los electrodos</p></em> 

### TOMA DE DATOS EN REPOSO

Esta toma de datos, nos permite registrar una referencia basal del ECG cuando el sujeto se encuentra en reposo.

<div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/231582212-aa004901-4b90-42d4-8d26-320108efb6da.mp4">
</div>
<em><p align="center">Toma de datos en reposo</p></em>

### Resultados
 
<em><h3>Análisis en el rango del tiempo</h3></em>

 <p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231589427-01596550-8895-44ab-907d-f58f5f6a54cd.jpg">
</p>
<em><p align="center">Datos graficados en el software Opensignals </p></em>
 <p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231634077-ba00bc86-2fa3-481c-a2ad-6a1f2954f5f4.png">
</p>
<em><p align="center">Datos graficados en Python .</p></em>

<em><h3>Análisis en el rango de la frecuencia</h3></em>

<p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231635768-e2e3bc1f-fea0-4493-a1b4-1fd46edc8fc4.png">
</p>
<em><p align="center">Transformada de Fourier del estado Basal.</p></em>
 
### TOMA DE DATOS CUANDO AGUANTA LA RESPIRACIÓN
 
 <div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/231624463-df299443-7ecb-41e3-999e-a6ead1ec4a41.mp4
">
</div>
<em><p align="center">Toma de datos</p></em>
  
### Resultados
 
<em><h3>Análisis en el rango del tiempo</h3></em>

 <p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231627730-9d44178d-a90c-4cdd-bb3e-e86a5ab2f6b1.jpg">
</p>
<em><p align="center">Datos graficados en el software Opensignals </p></em>
 <p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231627585-ef6bc634-6d09-47e9-afb9-1b7d8fd40575.jpg">
</p>
<em><p align="center">Datos graficados en Python .</p></em>

<em><h3>Análisis en el rango de la frecuencia</h3></em>

<p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231636138-aff5dde5-72b4-4ed0-a91d-80daa1e26869.png">
</p>
<em><p align="center">Transformada de Fourier de la señal después de aguantar la resiración.</p></em>
 
### TOMA DE DATOS DESPUÉS DE ACTIVIDAD FÍSICA DE CARDIO:
 
 Se le pidió al sujeto de estudio que realice actividad física hasta llegar a la fatiga; para esto se realizaron 40 planchas y 10 burpees.
<div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/231623579-0f4ab714-ba29-4d8f-84eb-8a497b4df26f.mp4">
</div>
<em><p align="center">Ejercicio que se realizó</p></em>
 
<div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/231625774-325f2c3f-7d55-4390-a369-da54a995ce4b.mp4">
</div>
<em><p align="center">ECG después del ejercicio</p></em>

### Resultados:
 
 <em><h3>Análisis en el rango del tiempo</h3></em>

<p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231635146-fb311207-10ec-4363-8e9e-98415160b261.jpg">
</p>
<em><p align="center">Datos graficados en el software Opensignals </p></em>
 
 <p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231634975-650eaee7-20d8-490a-8333-3b924adc95a1.jpg">
</p>
<em><p align="center">Datos graficados en Python .</p></em>

<em><h3>Análisis en el rango de la frecuencia</h3></em>

<p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231635972-55145861-cfeb-43c7-ba60-668c68debda6.png">
</p>
<em><p align="center">Transformada de Fourier de la señal después de realizar ejercicio</p></em>
 
<h2 align="center">Sujeto 2</h2>

### COLOCACIÓN DE LOS ELECTRODOS
 
 <p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231637877-0bda9bac-e632-4f7c-a132-d1f26a344192.jpeg">
</p>
<em><p align="center">Ubicación de los electrodos</p></em> 

### TOMA DE DATOS EN REPOSO

Esta toma de datos, nos permite registrar una referencia basal del ECG cuando el sujeto se encuentra en reposo.

<div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/231652696-1357f306-1788-454e-b8ab-0529c7da4491.mp4">
</div>
<em><p align="center">Toma de datos en reposo</p></em>

### Resultados
 
<em><h3>Análisis en el rango del tiempo</h3></em>

<p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231653980-36e67ff2-1a55-42ff-848a-0fe5d609ecbd.jpg">
</p>
<em><p align="center">Datos graficados en el software Opensignals </p></em>
 <p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231653797-aee807ae-1b61-4ba8-8b28-b81fc2e0884d.jpg">
</p>
<em><p align="center">Datos graficados en Python .</p></em>

<em><h3>Análisis en el rango de la frecuencia</h3></em>

<p align="center">
  <img width="700" height="500" src="https://user-images.githubusercontent.com/128627158/231653750-f0f908ef-da80-48af-be69-392461f1ba4b.png">
</p>
<em><p align="center">Transformada de Fourier del estado Basal.</p></em>
 
### TOMA DE DATOS CUANDO AGUANTA LA RESPIRACIÓN
 
 <div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/231654287-0e52dc61-d971-4a9d-a863-23d0f6ad8c50.mp4">
</div>
<em><p align="center">Toma de datos</p></em>

### Resultados
 
<em><h3>Análisis en el rango del tiempo</h3></em>

 <p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231654760-8b8b5835-8a5e-4813-b85f-99691a31696c.png">
</p>
<em><p align="center">Datos graficados en el software Opensignals </p></em>
 <p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231655977-65e92db8-2334-469b-8913-74793aac4dc3.jpg">
</p>
<em><p align="center">Datos graficados en Python .</p></em>

<em><h3>Análisis en el rango de la frecuencia</h3></em>

<p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231653676-a0bea1d7-9c1e-466b-a6f6-ca0bddc07bfa.png">
</p>
<em><p align="center">Transformada de Fourier de la señal después de aguantar la resiración.</p></em>
 
### TOMA DE DATOS DESPUÉS DE ACTIVIDAD FÍSICA DE CARDIO:
 
 Se le pidió al sujeto de estudio que realice actividad física hasta llegar a la fatiga; para esto se realizaron plichinelas y burbees durante 3 minutos en total.
<div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/231652464-7075abad-a356-428d-bc6f-4871a5731dde.mp4">
</div>
<em><p align="center">Ejercicio que se realizó</p></em>
 
### Resultados:
 
 <em><h3>Análisis en el rango del tiempo</h3></em>

<p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231656211-b37b50ef-36a4-481a-8435-32ec9cbf7604.jpg">
</p>
<em><p align="center">Datos graficados en el software Opensignals </p></em>
 
 <p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231655620-d3d2769a-e749-4e3c-8d93-4b34a6d605a4.jpg">
</p>
<em><p align="center">Datos graficados en Python .</p></em>

<em><h3>Análisis en el rango de la frecuencia</h3></em>

<p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231658916-7dfad5ad-efc2-41b3-9bf4-e359cbe6958c.png">
</p>
<em><p align="center">Transformada de Fourier de la señal después de realizar ejercicio</p></em>

 
### ProSim-8:
 Gracias al ProSim-8 podemos verificar si el Bitalino está funcionando de manera adecuada para la adquisición de la señal ECG. También nos permite comparar como sería una adquisición ideal de una señal ECG con una real y con ello, mejorar la adquisición de la señal, observar la forma de las ondas que componen el ECG de una mejor manera, etc.
 <p align="center">
  <img width="300" height="500"src="https://user-images.githubusercontent.com/128627158/231651789-da5354fe-2de5-4bd0-9531-cdcadd04699f.jpg">
</p>
<em><p align="center">Configuración del ProSim-8</p></em>
 
<div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/231652013-fb7b1570-19fd-4676-89f8-612d9c704692.mp4">
</div>
 
<em><p align="center">ECG después del ejercicio</p></em>
 <h2 align="center">DISCUSIONES</h2>
 
### Discusión de las señales recolectadas con el sujeto 1:
 
Como se puede observar en la grabación e imágenes colocadas, el sensor para EKG del Bitalino muestra resultados esperados relativamente buenos al momento de probar
y experimentar con un sujeto real, ya que si bien todas las ondas y formas de los complejos se pueden apreciar, existe ruido presente en la señal, producto muchas de como estan colocados los electrodos en el cuerpo y sus ubicaciones respectivas (según el tipo de derivación), el tipo de electrodos utilizados, movimiento muscular del sujeto de prueba, ruido eléctrico en el ambiente donde se realiza la medición, etc. 
 
Por otro lado es evidente al comparar las gráficas entre el estado basal y luego de haber realizado la actividad física, una disminución del periodo entre onda y onda del EKG (entre complejos P-QRS-T respectivamente), esto es debido a un incremento en la frecuencia cardiaca del sujeto y si bien la amplitud se ve mas reducida para el segundo caso, es simplemente la escala que el programa utiliza para visualizar las ondas de mejor manera, ya que luego de reposar o al aguantar la respiración y al volver a respirar con normalidad, la amplitud de la señal aumenta mientras que la frecuencia disminuye. Asi mismo, el tema del ruido se incrementa y esto es apreciable en las gráficas luego de haber realizado una actividad física. Si el sujeto reposa, recupera su frecuencia cardiaca normal y el ruido disminuye. 
 
### Discusión de las señales recolectadas con el sujeto 2:
 
Para el segundo sujeto, al analizar las ondas se cumple el mismo patrón en la onda y complejos típicos de un EKG; la unica diferencia que se puede notar es que al realizar la actividad física respectiva y comparando con la gráfica de estado basal, la frecuencia con la que las ondas aparecen entre complejo y complejo es menor que para el primer sujeto, esto puede ser debido a muchos factores, entre los cuales destaca el hecho de que el segundo sujeto realiza actividad aeróbica frecuente, pudiendo asi controlar su frecuencia cardiaca con mayor facilidad y reponerse de manera más rápida.

### Discusión de la señal recolectada con el dispositivo patrón: 
 
Analizando respecto a la salida obtenida para un EKG con el simulador ProSim-8 de la marca fluke, se puede observar un onda con sus complejos de manera mas limpia, libre de ruidos. Esto es debido a que al ser un simulador y contar con parametros que uno mismo como usuario puede establecer, el simulador se encargara de mantenerlas y enviarlas al programa para la visualizacion de las ondas respectivas, lo cual en un sujeto real y al ser un sistema biologico suceptible a diferentes interferencias del medio que lo rodeapresentes (carga del ambiente, vellosidades, tipos de electrodos usados, posicionamiento, etc.) las gráficas obtenidas contaran con un ruido presente el cual puede ser atenuado mediantes filtros tanto analógicos como digitales, mientras que el simulador envía una señal artificial ya libre de ruido.
### Discusión de FFT:
 En las figuras del ECG Basal del participante 1 y 2 se observa que las frecuencias que tiene mayor predominio en la señal están en el rango de 0 a 50 Hz debido a su amplitud o mayor área bajo la curva. Esto tiene sentido dado que el ritmo sinusal normal tiene frecuencias bajas (entre 1 y 2 Hz). Las otras frecuencias pueden deberse a posibles ruidos. Esto también se presenta en las señales ECG con actividad física y sin respirar, pero varía las frecuencias debido a los eventos fisiológicos que involucra cada uno.
 
 ### Discusión de FFT de las señales:
 En las figuras del ECG Basal del participante 1 y 2 se observa que las frecuencias que tiene mayor predominio en la señal están en el rango de 0 a 50 Hz debido a su amplitud o mayor área bajo la curva. Esto tiene sentido dado que el ritmo sinusal normal tiene frecuencias bajas (entre 1 y 2 Hz). Las otras frecuencias pueden deberse a posibles ruidos. Esto también se presenta en las señales ECG con actividad física y sin respirar, pero varía las frecuencias debido a los eventos fisiológicos que involucra cada uno.

Según Vikanda et al. [8] es posible que las mediciones de ECG contengan diferentes ruidos, como la interferencia de la línea de alimentación (PI), la desviación de la línea de base (BW), los artefactos musculares (MA) y los artefactos de movimiento de los electrodos (EM). Al comparar la FFT de su señal sinusal normal con ruido EM con nuestra FFT, notamos que era el ruido que tenía mayor similitud.
 
 <p align="center">
  <img width="400" height="500"src="https://user-images.githubusercontent.com/128627158/231657688-0b9346b3-acc0-4e69-8ef0-ec57e495e51c.png">
</p>
 
## Bibliografia
 
1. Rafie, Nikita, Anthony H. Kashou, and Peter A. Noseworthy. "ECG Interpretation: Clinical Relevance, Challenges, and Advances." Hearts 2.4 (2021): 505-513. https://www.mdpi.com/2673-3846/2/4/39
2. Esteban Álvarez-Reséndiz G, Ochoa-Gaitán G, Velazco-González JG, Clara D, Gutiérrez-Porras L, Monares-Zepeda E, et al. Monitoreo anestésico básico [Internet]. Medigraphic.com. [citado el 13 de abril de 2023]. Disponible en: https://www.medigraphic.com/pdfs/rma/cma-2013/cmas131r.pdf
3. Serhani MA, T El Kassabi H, Ismail H, Nujum Navaz A. ECG monitoring systems: Review, architecture, processes, and key challenges. Sensors (Basel) [Internet]. 2020 [citado el 13 de abril de 2023];20(6):1796. Disponible en: https://www.mdpi.com/1424-8220/20/6/1796
4.	Langner P. First Derivative of the Electrocardiogram [Internet]. [citado el 12 de abril de 2023]. Disponible en: https://www.ahajournals.org/doi/pdf/10.1161/01.RES.10.2.220#:~:text=The%20derivative%20shows%20the%20rate,changing%20low%20frequency%20wave%20forms.
5.	Zauner J. Ocular light effects on human autonomous function: the role of intrinsically photosensitive retinal ganglion cell sensitivity and time of day [Internet]. Disponible en: https://edoc.ub.uni-muenchen.de/30150/7/Zauner_Johannes.pdf
6.	Ay Gül AN. Real-time feature extraction of ECG signals using NI LabVIEW.
7. FFT. (n.d.). Nti-audio.com. Retrieved April 12, 2023, from https://www.nti-audio.com/en/support/know-how/fast-fourier-transform-fft 
8.	PLUX Biosignals. How do I know I am alive? [Internet]. [citado el 12 de abril de 2023]. Disponible en: https://www.pluxbiosignals.com/blogs/informative/how-do-i-know-i-am-alive 
