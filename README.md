![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Proyecto 03: API and Web Data Scraping



## 1. Objetivo.

En este proyecto he querido contestar dos simples preguntas:

- En qué provincias de la España peninsular hay los mejores puertos de montaña para el ciclismo?
- En qué época es más benigno el clima de cada provincia?

Para dar respuesta a la primera pregunta necesitaré conocer cuál es la media de dureza para los puertos en cada provincia, así como su desnivel y cota final. Este proceso será conducido mediante el uso de web scraping con una conocida web que recopila los datos de todos los puertos de España, para posteriormente plasmarlos en un dataframe que nos permitirá sacar conclusiones de manera rápida y visual.

Para contestar a la segunda pregunta usaré web scraping mediante Selenium para conseguir un completo resumen climatológico de cada provincia cogiendo como referencia su capital.


## 2. Planificación.

Para obtener los datos de los puertos de montaña españoles se ha usado el exhaustivo catálogo de la web www.altimetrias.net, que posteriormente fueron agrupados por provincia (obteniendo las medias de cada una de ellas) y cuyo resultado ha sido exportado como csv para su posterior análisis.

En cuanto a la meteorología los datos han sido extraídos de los detallados informes realizados por la web www.es.weatherspark.com, que nos proporciona resúmenes meteorológicos para cada capital de provincia.

En base a estos datos se ha decidido cuál es la mejor provincia para los puertos de montaña y en qué época contaremos con la mejor meteo.


## 3. Métodos empleados.

Para el scraping de las altimetrías se ha utilizado **BeautifulSoup**, definiendo una función que nos generase un diccionario con los datos de cada puerto de España. Posteriormente se ha recurrido a **Pandas** para crear un dataframe que agrupara todos los diccionarios, lo cual nos facilita enormemente trabajar con los datos.
Después de limpiar el dataframe se han agrupado los puertos por provincia, obteniendo un DF mucho más compacto desde el que sacar conclusiones. 

A la hora de obtener los datos meteorológicos de Weatherspark se ha optado por usar **Selenium** ya que permitía ejecutar una búsqueda para cada capital de provincia y acceder al HTML conteniendo su resumen meteorológico. Usando **Regex** se ha podido obtener cada parte del resumen meteorológico, asignándolo a un diccionario junto con el nombre de la capital correspondiente.
Para obtener los datos de todas las provincias ha sido creada una función que generaba el diccionario meteorológico simplemente con pasarle como argumento la capital de provincia deseada. Posteriormente se ha pasado cada ciudad a la función para obtener un dataframe en el que asociaba cada provincia a su meteorología. 

Finalmente para data visualization se han creado varios mapas usando la librería **Folium**.
He buscado un archivo *geojson* con las provincias españolas para usar como base, del cual he obtenido los nombres que usaba internamente para denominar cada provincia. Para poder asignar correctamente cada área del mapa a los valores del dataframe ha sido necesario cambiar los nombres de este último a los presentes en el archivo *geojson*, así como la asignación con valores nulos a los elementos faltantes del mapa (de lo contrario aparecen con valores máximos de forma artificial).
Una vez definidos los parámetros, capa base y colores para el mapa *choropleth* es muy simple cambiar los datos que representa así como la leyenda, pudiendo crear diferentes mapas con el mismo dataframe en cuestión de segundos.


## 4. Problemas encontrados.

**Scraping altimetrías:** la web se basa extensivamente en tablas a las cuales he tenido que acceder por índice a base de trial and error. Algunos puertos estaban duplicados y otras páginas estaban vacías, por lo que ha sido necesario usar data cleaning para lo primero y *try/except* para lo segundo.

**Scraping meteo:** muchas ciudades españolas tienen su hermana en Cuba/México/Colombia y en mis primeros intentos la meteorología de algunas provincias parecía ser extrañamente tropical. El error pudo ser solventado añadiendo *España* a los keystrokes para cada búsqueda.
Selenium puede ser muy temperamental cuando entran las cookies en la ecuación, es difícil que el código funcione correctamente a la primera en todas las ocasiones. 

**Creación de mapas:** encontrar un archivo *geojson* válido ha sido un problema bastante importante. También lo ha sido pasar los nombres de provincias al mismo formato que usa el archivo, ya que tanto la *ñ* como los acentos corrompían el topónimo. 


## 5. Futuras mejoras.

Sería muy interesante crear un mapa interactivo con todos los puertos, en el que haciendo click en cada uno de ellos pudiéramos ver su altimetría. El principal problema sería conseguir las coordenadas de inicio y final, ya que no todas las ascensiones empiezan o acaban en lugares con claras referencias topográficas.


## 6. Archivos adicionales.

Para ejecutar correctamente el código es necesario tener el webdriver adecuado para el navegador que se esté utilizando, en este caso he incluido el de Chrome.
Si se quiere generar un mapa mediante *Selenium* será necesario descargar el archivo *provincias.geojson* y tenerlo en el mismo directorio que el código.