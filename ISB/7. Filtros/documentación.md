Se eligió un filtro Butterworth IIR para filtrar las señales ECG debido a su respuesta en frecuencia suave y fase lineal. A continuación se presenta algunas de sus ventajas para esta aplicación [1][2]:

Respuesta en frecuencia suave: El filtro Butterworth tiene una respuesta en frecuencia plana dentro de su banda de paso, lo que significa que atenúa las frecuencias fuera de la banda de paso suavemente y sin ondulaciones. Esto lo convierte en una buena opción para filtrar señales de ECG ya que la banda de paso contiene componentes de frecuencia importantes que deben ser preservados mientras se atenúan las frecuencias no deseadas.

Respuesta de fase lineal: El filtro Butterworth tiene una respuesta de fase lineal, lo que significa que introduce un retardo constante a todos los componentes de frecuencia de la señal. Esto es deseable para señales de ECG ya que preserva la forma de la señal y no distorsiona la forma de onda.

Buen rendimiento: Un filtro Butterworth puede lograr un buen equilibrio entre la cantidad de atenuación en la banda de rechazo y la pendiente de la banda de transición. Esto significa que puede eliminar eficazmente el ruido y los componentes no deseados de la señal mientras se preservan las características importantes de ECG.


Para el diseño del filtro IIR, empleamos la función buttord de la librería scipy para obtener las características necesarias como el número de orden mínimo y la frecuencia de corte. Para esto, se definen como banda de paso y banda de corte 94 rad/s y 157 rad/s, respectivamente. Como dato, se recomendó usar 20Hz como la frecuencia de corte. Sin embargo, la frecuencia obtenida empleando la función buttord fue de 14.96 Hz, la cual, será utilizada en el resto del desarrollo.

Luego, definimos el filtro con la función butter, especificando el tipo de filtro, el cual en este caso, se trata de un filtro pasabajas. Asimismo, el parámetro analog se define como True, ya que esto nos permite diseñar un filtro analógico. El filtro diseñado se puede encontrar en los archivos.
