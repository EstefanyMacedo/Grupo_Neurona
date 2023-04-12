# Recolección de señales electrocardiográficas

## Tabla de Contenidos
+ [Introducción](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#breve-introducci%C3%B3n)
+ [Marco Teórico](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#marco-te%C3%B3rico)
+ [Materiales](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#materiales)
+ [Guías electrocardiacas](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#gu%C3%ADas-elect)
+ [Señales adquiridas y comparación](https://github.com/EstefanyMacedo/Grupo_Neurona/edit/main/laboratorio_4/Documentaci%C3%B3n.md#se%C3%B1ales-adquiridas-y-comparaci%C3%B3n)
+ [Discusión]()
+ [Archivos]()
+ [Bibliografía]()
## Introducción
eso lo pone jesús a
## Marco teórico
- Frecuencia de muestreo: 1000HZ
- Amplitud: [V-2mV]

## Materiales
## Guías elect
Se tomaron referencias de la colocación de los electrodos y buenas prácticas durante la toma de datos las presentes guías:
* Guía De Procedimiento de Electromiografía y velocidad de conducción de nervios periférico. INSN
* Video referencia colocado en la guia de laboratorio mostrando ubicaciones posibles para el EMG.
* Manual del usuario del sensor de electromiografía (EMG) biosignalsplux

Read more: 
- https://www.insnsb.gob.pe/docs-trans/resoluciones/archivopdf.php?pdf=2020/RD%20N%C2%B0%20000226-2020-DG-INSNSB%20Gu%C3%ADa%20Proced%20Electromiograf%C3%ADa_2020%203REV%20UGC%20CHN%2019.06.2020.pdf
- https://www.youtube.com/watch?v=pijLklRQ8MA
- https://manuals.plus/es/biose%C3%B1ales/manual-del-sensor-de-electromiograf%C3%ADa-emg#axzz7y3EF2MKZ.
‌

Lo más resaltante es que el paciente esté en una posición cómoda, relajado, sin ningún objeto metálico y que el lugar donde se 
coloquen los respectivos electrodos sobre la piel este limpia.
Además, se debe asegurar la correcta colocación de los electrodos positivo, negativo y de referencia en sus respectivos lugares según indican las guías consultadas.

## Señales adquiridas y comparación:
Resumen y explicación de las señales ploteadas

### Primera señal &rarr; Nervio musculocutáneo
Ubicación: Bícep izquierdo

<p align="center">
  <img width="460" height="300"src="https://user-images.githubusercontent.com/128627158/230184642-89ec939a-9a52-4705-b99e-379eb1fa4132.jpeg">
</p>
<em><p align="center">Ubicación de los electrodos</p></em>

Se plantea evaluar la señal emitida por el nervio musculocutáneo, el cual, da inervación motora a los músculos bíceps, coracobraquial y braquial como se muestra en la Figura. 
Los resultados observados en la gráfica evidencian un comportamiento de amplitudes constantes cercanas a 0 mV cuando no se genera fuerza en el brazo, es decir, se mantiene relajado. Por otro lado, cuando se realiza la flexión del brazo, la gráfica cambia su comportamiento y las amplitudes aumentan y varían llegando a registrar hasta 1 mV.

<p align="center">
  <img width="560" height="300"src="https://user-images.githubusercontent.com/128627158/230186714-1da3a0bd-84be-4366-9a7d-21cadd3cdf2a.jpeg">
</p>
<em><p align="center">Gráfica obtenida en Opensignals de la señal mioeléctrica</p></em>

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
