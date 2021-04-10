En este proyecto he combinado conocimiento de scrapeo y apis con limpieza de Pandas.

El proyecto tenía como objetivo obtener información sobre el alquiler de los pisos en barcelona ya que en septiembre me mudo con unos amigos. Quería obtener información que sé que es relevante para los 4 amigos y, además, obtener coordenadas geográficas para poder calcular la distancia entre los pios y ciertos puntos de intertés para los integrantes de cada piso. De este manera, espero poder tomar una decisón más acertada a la hora de escoger un piso que se adapte a las necesidades de los 4 integrantes.

He escrapeado la sección de Alquiler de pisos en Barcelona de la web de Habitaclia, obteniendo una Data Set de unos 11.000 pisos. La información obtenida es, entre otra, el precio, habitaciones, baños, terraza, latitud, longitud, etc.

Estas dos últimas variables me han sido útiles para calcular la duración del trayecto desde cada uno de los pisos hasta mi trabajo, el trabajo de los amigos que vivirán conmigo y hasta algunos puntos de interés (pistas de padel).

Una vez filtrado el Data Set por las variables de interés (precio máximo, 4 habitaciones, terraza, etc) me he quedado con un Data Set de 51 pisos. A partir de aquí, la idea sería basarme en esta lista, junto con el tiempo de viaje hasta cada una de las destinaciones, para poder escoger uno de los pisos.

Entregables:

	1) barcelona_alquiler.py: es el escrapeo de una sola página de habitaclia. Me fue útil para realizar pruebas antes de ejecutar el código que escrapea toda la página web

	2) todo_barcelona_alquiler.py: es el escrapeo de toda la página web de idealisat (alquiler, barcelona). Es lo mismo que el fichero anterior pero añadiendo la funcionalidad de pasar de página.

	3) barcelona_compra.py y todo_barcelona_compra.py: son la misma idea que los de alquiler pero hacen el análisis a nivel de compra de pisos. No están completos pero ya vi que no difiere mucho resoecto a los de alquiler

	4) API.ipynb: documento en el que accedo a la API de Google y obtengo las duraciones de trayecto. También realizo limpieza del Data Set y lo exporto a mi ordenador.

	5) Carpeta Data: Hay dos documentos csv:
		5.1) barcelona_todo_alquiler.csv: son los 11.000 pisos que escrapeo gracias al código "todo_barcelona_alquiler.py"
		5.2) pisos_finalistas.csv: son los 50 pisos con los que me quedo después de aplicar los filtros correspondientes de precio, habitaciones, etc.



