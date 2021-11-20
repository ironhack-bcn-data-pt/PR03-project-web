![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: API and Web Data Scraping
*[Carlos Romero]*	

*[DATA PT SEP 2021, Ironhack Barcelona 2021-11-20]*

## Content
- [Overview](#overview)
- [Parte I: API](#parte-i:-api)
- [Parte II: Web Data Scraping](#parte-ii:-web-data-scraping)
- [Links](#links)

## Overview

El objetivo de este proyecto era el tener que practicar lo que ha aprendido en las clases de API y Web Scraping de este curso. Para este proyecto, he tenido que escoger tanto una API para obtener datos como una página web para escrapear. Para la parte API del proyecto, debía realizar llamadas a la API elegida, obtener una respuesta, solicitar datos, convertirlos en un dataframe de Pandas y exportarlos como un archivo CSV. Para la parte de raspado web del proyecto, debía raspar el HTML de la página elegida, analizar el HTML para extraer la información necesaria y guardar los resultados en un archivo de texto (txt) si es texto o en un CSV archivo si se trata de datos tabulares.

## Parte I: API

### API escogida y el porqué de la elección

* La API con la que he decidido trabajar es [Socrata] (https://dev.socrata.com/) una API especializada en datos abiertos de gobiernos. En mi caso necesitaba trabajar con ella puesto que el dataset que deseo obtener esta así gestionada.

* La elección de este dataset se basa en la idea de utilizarla más adelante (en el proyecto final). El dataset contiene un registro de todas las ofertas de empleo público de Cataluña desde finales del 2001.

### Trabajar con la API

* Tras localizar la página web donde se encontraba la API con los datos [analisi.transparenciacatalunya.cat] (https://analisi.transparenciacatalunya.cat/Treball/Convocat-ries-de-Personal/a2hm-uzyj) procedo a leer la [documentación de la API] (https://dev.socrata.com/foundry/analisi.transparenciacatalunya.cat/a2hm-uzyj) para encontrar el método de conectar con ella y hacer un get para obtener el dataset. 

* En Code Snippets encuentro un apartado de “Python Pandas” con dos formas de acceder a los datos:
- Mediante un cliente no autenticado: lo cual me avisa que puede conllevar restricciones de acceso
- Mediante cliente autenticado: acceso sin restricciones.
Decido acceder mediante la segunda opción y para ello, me creo una cuenta para obtener una contraseña y un token.

* Accediendo a los datos mediante código sugerido para Python Pandas:
- Importo sodapy de la librería Socrata y accedo a la información con método Socrata y los siguientes parámetros: (‘url’,token,username,password)
- Utilizo el método de Socrata client.get y amplio el límite a 70000 registros. Obtengo un json llamado “results”

* Convertir json en un dataframe de Pandas: Convierto el json en un dataframe utilizando pd.json_normalize


* Problema encontrado: la documentación me sugería un método concreto de pandas “pd.DataFrame.from_records” pero el resultado era una dataframe con celdas con listas. Para evitar esto he decidido utilizar el método anteriormente comentado.

* Exportar dataframe a csv en carpeta output.

## Parte II: Web Data Scraping 

### Web escogida y el porqué de la elección

* Decido scrapear la web de [biwenger.as.com] (https://biwenger.as.com/) que proporciona el entorno para jugar a una liga fantasy de la NBA. Esta es una web donde un grupo de jugadores crear sus equipos de la nba para competir entre ellos durante la temporada. 

* El motivo de la elección es la de desarrollar un asistente de fichajes y ventas a partir de predicciones estadísticas reales aportadas por la web [FiveThirtyEight] (https://projects.fivethirtyeight.com/).

### Obtención de la url con el dataset de predicciones por jugador (RAPTOR) de la FiveThirtyEight.


* En la página web FiveThirtyEight.com descubro unas métricas que calculan la proyección de cada jugador de la NBA y que se actualiza cada día en función de su rendimiento. A estos algoritmos los llaman [RAPTOR] (https://fivethirtyeight.com/features/introducing-raptor-our-new-metric-for-the-modern-nba/). Como referencia de valor de predicción decido extraer el valor de tres métricas diferentes y hacer la media. Las métricas seleccionads son las siguientes:
- war_reg_season: “Wins Above Replacement for regular season”
- raptor_total: “Points above average per 100 possessions added by player on both offense and defense, using both box and on-off components “
- predator_total: “Predictive points above average per 100 possessions added by player on both offense and defense”

* Para disponer de los datos la página web me enlzae a un repositorio de github público donde puedo extraer diariamente la información mediante csv. Escribo la llamada y lo transformo en un dataframe llamado df_prediccion

### Escrapear para importar datos de mi equipo y mercado

* Preparar conexión con selenium: sigo los pasos que nos enseñaron en clase para poder conectarme a la página web mediante selenium. He escogido esta librería porque la [web a escrapear] (https://biwenger.as.com/) solicita al usuario la realización de acciones con el ratón.

* Hacer login para entrar en mi cuenta: necesito loguearme para acceder a la información de mi cuenta. Se ha decidido hacer visible el username (mi email) y no visible los passwords (en ficheros txts separados).

* Ordenar acciones que la web solicita para acceder a la información. En este caso las acciones a programas son las siguientes.
- Aceptar cookies
- Navegar hasta la sección donde se encuentra la información (/team y /market).
- Hacer scroll y esperar para acceder sin problemas.
- Seleccionar formato tabular para escrapear más fácilmente.

* Escrapear: 
- Para información de mi equipo se ordena un for loop que me vaya generando diccionarios para cada jugador con su posición, su nombre y su valor. Estos diccionarios se almacenan en una lista.
- Para información del mercado se ordena un for loop que me vaya generando diccionarios para cada jugador con su posición, su nombre, su estado físico y su valor. Estos diccionarios se almacenan en una lista.

* Transformar a dataframes: Transformo las listas de diccionarios obtenidas en dataframes de nombre: df_equipo y df_mercado.

### Analisis de la información extraida
- Relaciono las dataframes de biwinger con la df_predicción mediante método merge.
- Manipulo los dataframes resultantes para incluir un campo de confianza de la predicción. La confianza en la predicción se basa en los minutos jugados por cada jugador en proporción a los minutos máximos que éste podría haber jugado. Se hace este cálculo porque las predicciones se basan en el rendimiento de cada jugador durante los minutos jugados y, por tanto, cuanto más minutos haya jugado más fiable será la predicción.
- Ordeno cada dataframe según el siguiente criterio: dataframe de mis jugadores: de menor a mayor valor de proyección. Dataframe del mercado: de mayor a menor valor de proyección.
- Visualizo y exporto en un csv los dataframe finales llamados: rank_jugadores_vendibles y rank_jugadores_fichables


## Links
* [Repository](https://github.com/ironhack-bcn-data-pt/PR03-project-web/pull/21)
* [Slides in html](https://drive.google.com/file/d/11GF9rY45Dw5JZid8D9XjCogDO4tyTOAD/view?usp=sharing)
* [Slide in pdf](https://drive.google.com/file/d/11QNCC8VOb4Af3GMiBiNnpzjgJ8NOJIVS/view)
