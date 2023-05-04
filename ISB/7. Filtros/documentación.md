<h1 align="center">DISEÑO DE FILTROS IIR y FIR</h1>

<h2 align="center">FILTRO IIR</h2>
Es posible elegir diferentes tipos de filtros analógicos como los que se muestran en la Figura 1. Cada uno de estos es elegido respecto a las características deseadas de la salida como el rizado máximo o mínimo, atenuación, tamaño de la banda de transición o propiedades específicas de cada filtro.

<p align="center">
  <img width="350" height="400"src="https://user-images.githubusercontent.com/128627312/236081055-a75a374e-5e0c-4370-bfc1-372ce90d89ee.png">
</p>
<em><p align="center">Figura 1. Tipos de filtros digitales.</p></em>

Se eligió un filtro Butterworth para filtrar las señales ECG debido a su respuesta en frecuencia suave y fase lineal. A continuación se presenta algunas de sus ventajas para esta aplicación [1][2]:

- Respuesta en frecuencia suave: El filtro Butterworth tiene una respuesta en frecuencia plana dentro de su banda de paso, lo que significa que atenúa las frecuencias fuera de la banda de paso suavemente y sin ondulaciones. Esto lo convierte en una buena opción para filtrar señales de ECG ya que la banda de paso contiene componentes de frecuencia importantes que deben ser preservados mientras se atenúan las frecuencias no deseadas.

- Respuesta de fase lineal: El filtro Butterworth tiene una respuesta de fase lineal, lo que significa que introduce un retardo constante a todos los componentes de frecuencia de la señal. Esto es deseable para señales de ECG ya que preserva la forma de la señal y no distorsiona la forma de onda.

- Buen rendimiento: Un filtro Butterworth puede lograr un buen equilibrio entre la cantidad de atenuación en la banda de rechazo y la pendiente de la banda de transición. Esto significa que puede eliminar eficazmente el ruido y los componentes no deseados de la señal mientras se preservan las características importantes de ECG.

Por otro lado, un filtro elíptico tiene una caída más pronunciada en la banda de rechazo pero una ondulación en la banda de paso. Esto significa que un filtro elíptico puede lograr una transición más rápida de la banda de paso a la de rechazo que un filtro Butterworth, pero a costa de cierta distorsión en la banda de paso. Los filtros elípticos son más difíciles de implementar.

Para el diseño del filtro IIR, empleamos la función buttord de la librería scipy para obtener las características necesarias como el número de orden mínimo y la frecuencia de corte. Para esto, se definen como banda de paso y banda de corte 94 rad/s y 157 rad/s, respectivamente. Como dato, se recomendó usar 20Hz como la frecuencia de corte. Sin embargo, la frecuencia obtenida empleando la función buttord fue de 14.96 Hz, la cual, será utilizada en el resto del desarrollo.

Luego, definimos el filtro con la función butter, especificando el tipo de filtro, el cual en este caso, se trata de un filtro pasabajas. Asimismo, el parámetro analog se define como True, ya que esto nos permite diseñar un filtro analógico. El filtro diseñado se puede encontrar en los archivos.


<h2 align="center">FILTRO FIR</h2>
En el caso de los filtros FIR, para su diseño, se debe escoger la ventana apropiada para su desarrollo. Los tipos de ventanas se muestran en la Figura 2. Es posible inferir que la ventana rectangular engloba más valores que el resto de ventana.

<p align="center">
  <img width="600" height="400"src="https://user-images.githubusercontent.com/128627312/236081059-e05caf58-ac57-443f-881d-7bfbc9a16605.png">
</p>
<em><p align="center">Figura 2. Tipos de ventanas para el diseño de filtros digitales.</p></em>

<h2 align="center">RESULTADOS</h2>
A continuacion mostraremos los resultados de las señales extraidas de nuestro data-set (estado basal, sin respirar, y ejercicio). Estas señales fueron pasadas por un filtro IIR de tipo butterworth y Eliptica. Además, más abajo se muestran los resultados de aplicar un filtro FIR de tipo Hamming y Blackman respectivamente. 
<div align="center">

|   **Estado**   | **Señal cruda** |  **Filtro IIR: Butterworth**  | **Filtro IIR: Elíptica**  |
|:-------------------:|:---------------:|:------------:|:------------:|
| Basal | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103701538062479400/image.png">| <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103701720137216143/image.png"> | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103706165768110140/image.png"> | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103707818378412164/image.png"> | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103708799925239828/image.png"> |
|      Aguantando la respiración    | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103702258400637020/image.png"> | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103702307809533972/image.png"> | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103706273901465711/image.png">| <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103707878247911494/image.png"> | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103708871148699720/image.png"> |
| Post-Ejercicio | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103704368429154425/image.png"> | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103704444551573565/image.png"> | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103706333049532546/image.png">| <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103707963354513471/image.png"> | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103708931810926704/image.png"> |

  
 
|   **Estado**   | **Señal cruda** | **Filtro FIR: Hamming**  | **Filtro FIR: Blackman**  |
|:-------------------:|:---------------:|:------------:|:------------:|
| Basal | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103701538062479400/image.png">| <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103707818378412164/image.png"> | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103708799925239828/image.png"> |
|      Aguantando la respiración    | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103702258400637020/image.png"> |  <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103707878247911494/image.png"> | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103708871148699720/image.png"> |
| Post-Ejercicio | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103704368429154425/image.png"> | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103707963354513471/image.png"> | <img width="200" height="150" src="https://cdn.discordapp.com/attachments/781169694949244932/1103708931810926704/image.png"> |


**IIR:** 
  
<br> Se puede observar que ambos filtros muestran buenos resultados. En otros estudios se ha analizado el rendimiento de estos filtros para señales ECG: Guler et al. mostraron que los filtros IIR elípticos proporcionan una mayor atenuación de ruido en la banda de rechazo en comparación con los filtros Butterworth, pero también presentaron una mayor distorsión en la banda de paso [3]. Ye et al. mostraron que los filtros Butterworth son más adecuados para eliminar estos artefactos, mientras que los filtros elípticos pueden ser más adecuados para aplicaciones que requieren una alta precisión en la detección de eventos ECG [4]. Asimismo, Çiloglu et al. mostraron que los filtros elípticos proporcionaron una mayor precisión en la detección de arritmias en comparación con los filtros Butterworth [5].
  
</div>
       

<h2 align="center">Bibliografía</h2>
[1] Raja, R. and Rajaguru, R., "A Comparative Study of IIR and FIR Filters for ECG Signal Processing," International Journal of Engineering Science and Computing, vol. 6, no. 6, pp. 7128-7133, 2016. Available: https://www.ijesc.org/upload/b17f3cdd290a5e5f0328795f2a5a4c4d.A%20Comparative%20Study%20of%20IIR%20and%20FIR%20Filters%20for%20ECG%20Signal%20Processing.pdf   
[2] Li, Y., Li, Z., Zhang, H., Wang, Y. and Yang, Z., "Comparison of ECG Signal Filtering Methods," Proceedings of the 2015 IEEE International Conference on Signal Processing, Communications and Computing, pp. 1-5, 2015. Available: https://ieeexplore.ieee.org/document/7312973 
[3] Güler, I., & Übeyli, E. D. (2013). Performance evaluation of IIR elliptic and Butterworth filters for real-time ECG signal processing. Journal of medical systems, 37(3), 1-7.
[4] Ye, J., & Chen, X. (2016). Comparison of IIR filters for ECG signal denoising. Journal of healthcare engineering, 2016, 1-9.
[5] Çiloglu, T., & Kuntalp, M. (2017). Comparison of Butterworth and elliptic filters in arrhythmia detection from ECG signals. Biomedical engineering online, 16(1), 1-10.
