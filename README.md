PROYECTO 3 API Y SCRAPING 

Como lazo de unión a ambos ejercicios, he escogido obtener la información necesaria para valorar si una noticia tiene un impacto en el volumen de negociación de una acción. He escogido a la compañía Tesla Inc. (TSLA del US/NASDAQ).

API
Seleccionada la API de Alpha Vantage, que tras la revisión de la documentación, creamos la API KEY y utilizamos la URL que más se ajusta a nuestra petición, modificándola para que nos facilite la información del valor (TSLA) (https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=DIXG291EF6FA5SGZ).
La petición devuelve información en JSON, el cuál trataremos y limpiaremos en un DataFrame con las siguientes modificaciones:
*Creación de columna “Volume” para posteriormente incorporar el dato necesario.
*Limpieza de columnas innecesarias para el ejercicio (Index Meta Data)
*Creamos un bucle que itera cada fila para obtener únicamente el volumen diario e incorporarlo a su correspondiente celda.
A continuación, se han realizado ejercicios de selección y visualización, escogiendo los 10 días con más volumen de los últimos 100 días y así poder comprobar si estos se relacionan con las noticias de esos días.
 
SCRAPING
Selección de página web para scrapear noticias: He escogido investing.com en su pestaña de noticias por compañías(https://www.investing.com/equities/tesla-motors-news) de la que no ha sido una elección de lo más acertada por la complejidad de la página. 
Otras como Bloomberg o la oficial del Nasdaq, daban problemas al parsear.
La mayor dificultad ha sido poder seleccionar el bloque de noticias y poder recabar el título de esta. Para enlazarlo al proyecto, me he dado cuenta de que hubiese estado bien buscar una fuente de información dónde indicase la fecha de publicación.


++En un futuro, debo seleccionar bien la página a scrapear, sabiendo analizar su complejidad y ver si reunirá los recursos necesarios para un ejercicio que me permita realizar un análisis más exhaustivo. 
