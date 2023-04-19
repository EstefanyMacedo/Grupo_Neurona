<h1 align="center">RECOLECCIÓN DE SEÑALES ELECTROENCEFALOGRAFÍAS</h1>

## Tabla de contenidos

+ [Introducción]()
+ [Marco Teórico]()
+ [Materiales]()
+ [Posicionamiento de electrodos]()
+ [Desarrollo del laboratorio]()
+ [Análisis en tiempo]()
+ [Análisis en frecuencia]()
+ [Discusiones]()
+ [Archivos]()
+ [Bibliografía]()
 <h2 align="center">INTRODUCCIÓN </h2>

<h2 align="center">MARCO TEÓRICO</h2>

### La señal de EEC:



<p align="center">
  <img width="600" height="400"src="https://www.heart.org/-/media/Images/Health-Topics/Arrhythmia/ECG-normal.jpg">
</p>
<em><p align="center">Figura 1. Señal ECG.</p></em>

### Primera y segunda derivada en un ECG


<p align="center">
  <img width="600" height="400"src="https://user-images.githubusercontent.com/128627158/231569722-862f1343-70f9-4eb7-8d70-2d1c20a4f22c.png">
</p>
<em><p align="center">Figura 2. Picos y valles de una señal de ECG [5].</p></em>

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

 

<p align="center">
  <img width="500" height="300"src="https://user-images.githubusercontent.com/128627158/231569119-e8a812d9-ce8a-4ceb-ab99-8945dccd9e4a.jpg">
</p>
<em><p align="center">Figura 3. Posicionamiento de los electrodos en el cuerpo [8].</p></em>
Se tomaron referencias de la colocación de los electrodos y buenas prácticas durante la toma de datos las presentes guías:
-

Lo más resaltante es que el paciente esté en una posición cómoda, relajado, sin ningún objeto metálico y que el lugar donde se 
coloquen los respectivos electrodos sobre la piel este limpia.
Además, se debe asegurar la correcta colocación de los electrodos positivo, negativo y de referencia en sus respectivos lugares según indican las guías consultadas.

<h2 align="center">DESARROLLO DEL LABORATORIO</h2>



<h2 align="center">Sujeto 1</h2>

### COLOCACIÓN DE LOS ELECTRODOS

<p float="right">
  <img src="https://user-images.githubusercontent.com/128627158/231570991-32bfd77a-3e97-4edc-94ee-b2ab51dd409a.jpg" width="500" />
  <img src="https://user-images.githubusercontent.com/128627158/231580875-39fe927c-b4b3-49d4-94dc-b51752e64f63.png" width="500" /> 
</p>
<em><p align="center">Ubicación de los electrodos</p></em> 

### TOMA DE DATOS EN REPOSO


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
 
### Discusión de las señales recolectadas con OpenBIC:
 
### Discusión de las señales recolectadas con el sujeto 2:
 

### Discusión de la señal recolectada con el dispositivo patrón: 
 

 
 ### Discusión de FFT de las señales:


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

