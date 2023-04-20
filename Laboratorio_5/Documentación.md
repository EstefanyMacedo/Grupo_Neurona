<h1 align="center">RECOLECCIÓN DE SEÑALES ELECTROENCEFALOGRAFÍAS</h1>

## Tabla de contenidos

+ [Introducción](https://github.com/EstefanyMacedo/Grupo_Neurona/blob/main/Laboratorio_5/Documentaci%C3%B3n.md#introducci%C3%B3n-)
+ [Marco Teórico](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/Laboratorio_5/Documentaci%C3%B3n.md#marco-te%C3%B3rico)
+ [Materiales](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/Laboratorio_5/Documentaci%C3%B3n.md#materiales)
+ [Desarrollo del laboratorio](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/Laboratorio_5/Documentaci%C3%B3n.md#desarrollo-del-laboratorio)
+ [Posicionamiento de electrodos](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/Laboratorio_5/Documentaci%C3%B3n.md#posicionamiento-de-electrodos)
+ [Toma de la señal](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/Laboratorio_5/Documentaci%C3%B3n.md#toma-de-la-se%C3%B1al)
+ [Resultados y análisis de la señal](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/Laboratorio_5/Documentaci%C3%B3n.md#resultados-y-an%C3%A1lisis-de-la-se%C3%B1al)
+ [Conclusiones](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/Laboratorio_5/Documentaci%C3%B3n.md#conclusiones)
+ [Archivos](https://github.com/EstefanyMacedo/Grupo_Neurona/blob/main/Laboratorio_5/Archivos)
+ [Bibliografía](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/Laboratorio_5/Documentaci%C3%B3n.md#bibliografia)


<h2 align="center">INTRODUCCIÓN </h2>

En este laboratorio se adquirieron y observaron señales EEG utilizando el ULTRACORTEX "MARK IV" EEG HEADSET con 8 canales y el dispositivo de adquisición de señales biomédicas, Bitalino. El objetivo fue familiarizarse con la adquisición, el análisis y la interpretación de señales EEG. Cada uno de los 8 canales se refiere a una ubicación específica en la cabeza, de acuerdo con el sistema internacional 10-20 utilizado para la colocación de electrodos en el cuero cabelludo [1]. La disposición de los electrodos permite la monitorización y registro de la actividad eléctrica del cerebro en diferentes áreas, lo que permite un análisis más detallado y una mayor precisión en la medición de las señales EEG.

<p align="center">
  <img width="600" height="400"src="https://user-images.githubusercontent.com/128627158/233237767-3f27330d-8e68-4977-8516-4371c0a68785.png">
</p>
<em><p align="center">Figura 1. Ubicación de headset para la obtención de señales de EEG.</p></em>

<h2 align="center">MARCO TEÓRICO</h2>

La electroencefalografía (EEG) es una técnica de registro de los potenciales eléctricos generados por las sinapsis de las neuronas y por lo tanto monitorear la actividad cerebral. Comúnmente, para la adquisición de señales EEG para su uso clínico y académico se utilizan electrodos de superficie, los cuales son colocados sobre el cuero cabelludo del paciente/participante normalmente apoyados por gel conductor o solución salina.

### La señal de EEG:

Esta señal se carácteiza por:
* Ser dinámica
* Existe una simetría entre ambos hemisferios(izquierdo y derecho) 
* No presentar algún patrón en la señal
* Presentar muscho ruido y artefactos

Además, cabe mencionar que el análisis en frecuencia de este tipo de señal es fundamental, ya que nos ofrece más información que en el análisis en el tiempo. En el análisi den frecuencia podemos detectar la presencia de ondas Delta, Alpha, Beta y Gamma. Las cuales se pueden separar por ondas rápidas y ondas lentas. Las presencia de estas ondas nos indica una actividad cerebral específica. 

<p align="center">
  <img width="600" height="400"src="https://user-images.githubusercontent.com/128627158/233340733-f3c1c307-53af-4fd1-8bc0-fa12df6a6666.png">
</p>
<em><p align="center">Figura 2. Ondas cerebrales.</p></em>

### Transformada rápida de Fourier (FFT)
La transformada rápida de Fourier es una herramienta que nos permite conocer qué frecuencias de onda sinusoidal componen una señal. La FFT convierte una señal en componentes espectrales individuales y, por lo tanto, proporciona información de frecuencia sobre la señal [7]. Es por ello que se aplicó la transformada rápida de Fourier a las señales adquiridas.

<h2 align="center">MATERIALES</h2>

<div align="center">

|   **Dispositivo**   | **Descripción** |  **Imagen**  |
|:-------------------:|:---------------:|:------------:|
| BiTalino | Kit de desarrollo de bajo costo que permite medir diferentes señales biomédicas |<img width="200" height="150" src="https://user-images.githubusercontent.com/128627158/231564649-f925e135-93c4-434d-85a4-03b62ff1b628.jpg">|
|       Electrodos      | Dispositivos que se utilizan para medir la actividad eléctrica de los tejidos biológicos. Se colocan en la superficie de la piel y detectan la actividad eléctrica |<img width="200" height="150" src="https://user-images.githubusercontent.com/128627158/231566660-9f4676ba-484a-43a2-9236-3595947a1528.jpg">|
| OpenBCI electrode cap | Es un arreglo de electrodos en forma de casco que permite la toma de señales electroencefálicas. Además de contar con su propio software|<img width="200" height="150" src="https://cdn.shopify.com/s/files/1/0613/9353/products/DSC03020FT.jpg?v=1620934768">|
| Unidades puntiagudas | Electrodos secos (en punta) para ser instalados en los nodos de Ultracortex en partes con cabello|<img width="200" height="150" src="https://docs.openbci.com/assets/images/SpikeyUnits8chan-99e7144f670927d32101ecc9b538934f.JPG">|
| Unidades planas | Electrodos secos (no puntiagudos) para instalar en nodos de Ultracortex sin pelo (por ejemplo en la frente)|<img width="200" height="150" src="https://docs.openbci.com/assets/images/FlatUnits-df330d4b23f905cb642cb423443865a6.JPG">|
| Unidades de confort | Unidades de comodidad utilizadas para distribuir el peso de los auriculares|<img width="200" height="150" src="https://docs.openbci.com/assets/images/blue-comfort-6b3cd03b5f72673b74abfe6322127646.jpg">|
| Clips para las orejas | Electrodo de clip de oreja|<img width="200" height="150" src="https://docs.openbci.com/assets/images/earclips1-8e1a6362faacb68d20ab604da0a7ddaf.jpg">|
| Placa OpenBCI Cyton de 8 canales | Se utiliza para tomar muestras de la actividad cerebral (EEG), la actividad muscular (EMG) y la actividad cardíaca (ECG). La placa se comunica de forma inalámbrica a una computadora a través del USB OpenBCI|<img width="200" height="150" src="https://cdn.shopify.com/s/files/1/0613/9353/products/DSC02779_720x.jpg?v=1614761059">|


</div>

<h2 align="center">DESARROLLO DEL LABORATORIO</h2>

El objetivo de esta experiencia de laboratorio es obtener las señales electroencefálicas mediante electrodos y, a su vez, observar su variación cuando se somete al participante a diferentes pruebas estímulos. Para esto, se realizó un análisis en el dominio y la frecuencia con las herramientas de OpenBCI y Bitalino.

<h2 align="center">POSICIONAMIENTO DE ELECTRODOS</h2>
<p float="right">
  <img src="https://user-images.githubusercontent.com/128627158/233181319-5463dd07-7713-4b00-987c-b714e5b1abe7.jpeg" width="500" height="400"/>
  <img src="https://user-images.githubusercontent.com/128627158/233182507-3db569b4-ffb1-46dc-bf2c-1a8cf8bea8d4.jpg" width="400" height="400"/> 
</p>

<em><p align="center">Figura 3. Posicionamiento de los electrodos con OpenBCI y BiTalino.</p></em>
Se tomaron referencias de la colocación de los electrodos y buenas prácticas durante la toma de datos las presentes guías:
- BITalino (r)evolution Lab Guide:EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS [2]
- OpenCIB [3]  

Lo más resaltante es que el voluntario esté en una posición cómoda, relajado, sin ningún objeto metálico y que el lugar donde se 
coloquen los respectivos electrodos sobre la piel este limpia.
Además, con respecto al casco de electrodos, se tiene que alinear el orificio del centro con la nariz, asimismo, ajustar los electodos una vez colocado.

<h2 align="center">TOMA DE LA SEÑAL</h2>

Antes de la realización de cada ejercicio, se dejó que el participante descansara 30 segundos con la finalidad de encontrar un estado base.

### Ejercicio 1: Abrir y cerrar los ojos

Se le pidió al participante que abriera 5 segundos y cerrara los ojos, el mismo periodo de tiempo, esto se repitió 5 veces.

<div align="center">
 <video src="https://user-images.githubusercontent.com/128627158/233190763-8cbee2e9-f066-40b2-b163-09381bfdc946.mp4" width="400" height="400">
  </div>
 
<em><p align="center">Ejercicio 1 medido con el OpenBCI</p></em>
 
 <div align="center">
    <video src="">
   
</div>
 
<em><p align="center">Ejercicio 1 medido con el BiTalino</p></em>

### Ejercicio 2: Ejercicios de razonamiento matemático

Durante este ejercicio se le presentaron 5 preguntas de razonamiento matemático y adivinanzas al participante. Cada una con un periodo de descanso de 12 segundos.
 
<div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/233207943-97a08def-e021-4a2a-a767-60c2f35d8237.mp4">
</div>
 
 <em><p align="center">Ejercicio 2 medido con el OpenBCI</p></em>
 
 <div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/233214573-0f65be6b-71d0-4c0d-a914-4ea86ec33c2e.mp4">
   
</div>
 
<em><p align="center">Ejercicio 2 medido con el BiTalino</p></em>
 
### Ejercicio 3: Exposición brusca a la luz
Durante este ejercicio se le taparon los ojos al particiante durante 5 minutos y después se le sometió a un flash bruscamente. Cabe mencionar que el este ejercicio solo se realizó con el BiTalino.
<div align="center">
    <video src="https://user-images.githubusercontent.com/128627158/233213583-0278e03a-d092-4546-8363-64c821370249.mp4">
</div>
<em><p align="center">Ejercicio 3 medido con el BiTalino</p></em>

<h2 align="center">RESULTADOS Y ANÁLISIS DE LA SEÑAL</h2>
 
### Resultados

<em><h3>Análisis en el rango del tiempo</h3></em>

<h3 align="center">Resultados del ejercicio 1</h3>
<p float="right">
  <img src="https://user-images.githubusercontent.com/128627158/233239858-04f0bdac-b309-4b31-811e-35556c5c4085.png" width="500" height="400"/>
  <img src="https://user-images.githubusercontent.com/128627158/233240094-04eb3750-6477-4b18-9b22-25f48b993640.png" width="500" height="400"/> 
</p>
<em><p align="center">Figura x x. Señal ploteada de los 8 canales de OpenBCI.</p></em>

 <p align="center">
  <img width="700" height="500"src="">
</p>
<em><p align="center">Figura x x. Señal ploteada en Opensignals.</p></em>

<h3 align="center">Resultados del ejercicio 2</h3>
<p float="right">
  <img src="https://user-images.githubusercontent.com/128627158/233242915-bcab816b-fa3f-4a84-8c4e-e6489937f55f.png" width="500" height="400"/>
  <img src="https://user-images.githubusercontent.com/128627158/233243160-a8da9313-12a3-46a2-a8f2-e282ffd9b054.png" width="500" height="400"/> 
</p>
<em><p align="center">Figura x x. Señal ploteada de los 8 canales de OpenBCI.</p></em>
 <p align="center">
  <img width="700" height="500"src="">
</p>
<em><p align="center">Figura x x. Señal ploteada en Opensignals.</p></em>
<h3 align="center">Resultados del ejercicio 3</h3>
 <p align="center">
  <img width="700" height="500"src="">
</p>
<em><p align="center">Figura x x. Señal ploteada en Opensignals.</p></em>

<em><h3>Análisis en el rango de la frecuencia</h3></em>

<h3 align="center">Resultados del ejercicio 1</h3>
 <p align="center">
  <img width="800" height="500"src="https://user-images.githubusercontent.com/128627158/233244717-a7cc9790-5de0-4fdb-b8c7-9c0af6ce7f7f.png">
</p>
<em><p align="center">Datos procesados a través de Python. OpenBCI </p></em>
 <p align="center">
  <img width="700" height="500"src="">
</p>
<em><p align="center">Datos graficados en Python. BiTalino</p></em>
 <p float="right">
  <img src="https://user-images.githubusercontent.com/128627158/233239858-04f0bdac-b309-4b31-811e-35556c5c4085.png" width="500" height="400"/>
  <img src="https://user-images.githubusercontent.com/128627158/233240094-04eb3750-6477-4b18-9b22-25f48b993640.png" width="500" height="400"/> 
</p>
Para este item se aplicó la Transformada de Fourier a los datos hallados en el dominio del tiempo
<p align="center">
  <img width="700" height="500"src="">
</p>
<em><p align="center">Datos procesados a través de Python. OpenBCI </p></em>
 <p align="center">
  <img width="700" height="500"src="">
</p>
<em><p align="center">Datos graficados en Python. BiTalino</p></em>

<p align="center">
  <img width="700" height="500"src="https://user-images.githubusercontent.com/128627158/231635768-e2e3bc1f-fea0-4493-a1b4-1fd46edc8fc4.png">
</p>
<em><p align="center">Transformada de Fourier del estado Basal.</p></em>

</div>
<em><p align="center">Toma de datos</p></em>

 

 <h2 align="center">CONCLUSIONES</h2>
 
### Discusión de las señales recolectadas con OpenBIC:
   
Para las señales obtenidas con el OpenBIC se pudieron observar señales capturadas lo suficientemente optimas, con poco ruido y lo suficientemente sensible ante las variaciones y estimulos mentales del sujeto de prueba; esto lo pudimos evidenciar luego de realizar los ejercicios de estimulo correspondientes, donde en base a una señal de reposo o "base" los picos y patrones de la señal se vieron aumentados y alterados progresivamente de acuerdo al esfuerzo mental que el sujeto realizaba; siendo así, donde se obtuvo un mayor estimulo en la prueba de ojos vendados y exposicion a la luz, como segundo lugar la prueba de razonamiento matemático y por ultimo la prueba de abrir y cerrar los ojos.
   
**Análisis en el tiempo - Ejercicio1:** En los canales 0, 6 y 7 se observa que la mayor actividad cerebral (mV) se da en los primeros segundos de la toma de datos, dado que se observa una mayor amplitud. Por otro lado, los canales 1, 4 y 5 registran mayor actividad cerebral en los segundos finales. Esto puede deberse a que en este ejercicio se le solicitó al participante que abra y cierra los ojos (y en este momento se le solicitó relajarse), teniendo de esta forma periodos de mayor actividad cerebral (ojos abiertos) y periodos con menor actividad cerebral (ojos cerrados). De acuerdo a un experimento realizado por Barry et al. [cita], en adultos jóvenes y niños, el estado de reposo con los ojos cerrados es uno de baja excitación EEG, y el cambio a los ojos abiertos implica principalmente un aumento de la excitación.
   Barry, R. J., & De Blasio, F. M. (2017). EEG differences between eyes-closed and eyes-open resting remain in healthy ageing. Biological psychology, 129, 293–304. https://doi.org/10.1016/j.biopsycho.2017.09.010

**Análisis en la frecuencia - Ejercicio1:** De acuerdo al espectro de la FFT, la mayor parte de la señal tiene frecuencias que oscilan entre los 0.1-100 Hz, lo cual corresponde a las ondas EEG conocidas. Sin embargo, se observan también picos en frecuencias altas que probablemente correspondan a artefactos.
 
**Análisis en el tiempo - Ejercicio2:** Al igual que en el Ejercicio 1 se observan periodos de mayor actividad cerebral y periodos con menor actividad cerebral. En este ejercicio se le solicitó al participante mantener los ojos cerrados y se le realizaron ciertas preguntas. En la mayoría de los canales se observan comportamientos similares a los del ejercicio 1, pero con la diferencia marcada de ciertos picos de actividad cerebral, lo que deducimos corresponde al momento en el tiempo en que el participante piensa en la respuesta a la pregunta que se le realizó.

**Análisis en la frecuencia - Ejercicio2:** De acuerdo al espectro de la FFT, hay una diferencia respecto al ejercicio 1. En el ejercicio 1 las frecuencias presentaban una amplitud decayente entre 0.1-100 Hz. Siendo las frecuencias con mayor presencia las delta,teta y alfa. En el ejercicio 2, algunos canales también presentan este comportamiento pero otros canales presentan una señal con más frecuencias alrededor de 100 Hz, es decir corresponden mayormente a ondas Gama, que justamente está relacionado al estado cerebral de mayor atención, según la Tabla 1. Esto se relaciona al hecho de que el participante tuvo que requerir una mayor actividad cerebral para formular una respuesta.
   
### Discusión de las señales recolectadas con bitalino:

Para las señales obtenidas con el bitalino, se pudieron obtener señales razonablemente optimas, ya que estas señales obtenidas contaban con mas ruido evidenciado en cuanto al patron de ondas mostradas en el monitor, pero en cuanto a los ejercicios de estimulo mencionados con anterioridad, si se pudo observar el mismo patron cumpliendo que las variaciones en la señal se dieron con mayor intensidad para la prueba de ojos vendados y exposicion a la luz, como segundo lugar la prueba de razonamiento matemático y por ultimo la prueba de abrir y cerrar los ojos.
   

### Conclusiones y comparaciones: 
 
Una de las mas grandes diferencias entre la adquisicion de señales EEG en cuanto al OpenBIC y bitalino es que el primero contaba con mayor puntos de contacto en cuanto a los electrodos usados con la superficie del craneo, por lo que las señales obtenidas son mas fidedignas a comparacion del bitalino , en el cual solo se utilizaron 3 puntos como referencia para la adquisicion de las señales. 

Asimismo, como se mencionó en el análisis en frecuencia, se observan picos a frecuencias altas que no correspoden totalmente a la actividad cerebral, sino a posibles artefactos. La fuente de artefactos puede provenir de problemas relacionados con el instrumento, como electrodos defectuosos, ruido de línea o alta impedancia de los electrodos, o pueden provenir de la fisiología del sujeto que se está registrando. Esto puede incluir parpadeos y movimientos oculares, actividad cardíaca y actividad muscular. Esto perjudica de cierta manera el análisis de la señal EEG, dado que como se observa en la tabla inferior, las ondas EEG corresponden a ciertos estados cerebrales como: relajación , concentración o nervios. 
 
 
 <p align="center">
  <img width="300" height="300"src="https://user-images.githubusercontent.com/128627620/233263839-489245ae-1694-40df-9b07-78f6aabf2e27.png">
</p>
  <em><p align="center">Tabla 1: Ondas EEG y estados cerebrales [cita]</p></em>
   
   Yasin, S., Hussain, S. A., Aslan, S., Raza, I., Muzammel, M., & Othmani, A. (2021). EEG based Major Depressive disorder and Bipolar disorder detection using Neural Networks:A review. Computer Methods and Programs in Biomedicine, 202, 106007. doi:10.1016/j.cmpb.2021.106007  

 
## Bibliografia
 
[1] American Electroencephalographic Society Guidelines for Standard Electrode Position Nomenclature". Journal of Clinical Neurophysiology. 8 (2): 200–202. April 1991. doi:10.1097/00004691-199104000-00007
(1) Fundamentals of EEG Signal Processing. EEG Signal Processing and Machine Learning. 2021;:77–113.

