![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Guided Project: API and Web Data Scraping

## Overview

El objetivo de este proyecto era el tener que practicar lo que ha aprendido en las clases de API y Web Scraping de este curso. Para este proyecto, he tenido que escoger tanto una API para obtener datos como una página web para escrapear. Para la parte API del proyecto, debía realizar llamadas a la API elegida, obtener una respuesta, solicitar datos, convertirlos en un dataframe de Pandas y exportarlos como un archivo CSV. Para la parte de raspado web del proyecto, debía raspar el HTML de la página elegida, analizar el HTML para extraer la información necesaria y guardar los resultados en un archivo de texto (txt) si es texto o en un CSV archivo si se trata de datos tabulares.

## Parte I: API

### API escogida y el porqué de la elección

* La API con la que he decidido trabajar es [Socrata] (https://dev.socrata.com/) una API especializada en datos abiertos de gobiernos. En mi caso necesitaba trabajar con ella puesto que el dataset que deseo obtener esta así gestionada.

* La elección de este dataset se basa en la idea de utilizarla más adelante (en el proyecto final). El dataset contiene un registro de todas las ofertas de empleo público de Cataluña desde finales del 2001.

### Trabajar con la API

* Tras localizar la página web donde se encontraba la API con los datos [analisi.transparenciacatalunya.cat] (https://analisi.transparenciacatalunya.cat/Treball/Convocat-ries-de-Personal/a2hm-uzyj) procedo a leer la [documentación de la API] (https://dev.socrata.com/foundry/analisi.transparenciacatalunya.cat/a2hm-uzyj) para encontrar el método de conectar con ella y hacer un get para obtener el dataset. 

*En Code Snippets encuentro un apartado de “Python Pandas” con dos formas de acceder a los datos:
. Mediante un cliente no autenticado: lo cual me avisa que puede conllevar restricciones de acceso
. Mediante cliente autenticado: acceso sin restricciones.
Decido acceder mediante la segunda opción y para ello, me creo una cuenta para obtener una contraseña y un token.

*Accediendo a los datos mediante código sugerido para Python Pandas:
.Importo sodapy de la librería Socrata y accedo a la información con método Socrata y los siguientes parámetros: (‘url’,token,username,password)
.Utilizo el método de Socrata client.get y amplio el límite a 70000 registros. Obtengo un json llamado “results”

*Convertir json en un dataframe de Pandas: Convierto el json en un dataframe utilizando pd.json_normalize


*Problema encontrado: la documentación me sugería un método concreto de pandas “pd.DataFrame.from_records” pero el resultado era una dataframe con celdas con listas. Para evitar esto he decidido utilizar el método anteriormente comentado.

*Exportar dataframe a csv en carpeta output.

## Parte II: Web Data Scraping 

### Web escogida y el porqué de la elección

* Decido scrapear la web de [biwenger.as.com] (https://biwenger.as.com/) que proporciona el entorno para jugar a una liga fantasy de la NBA. Esta es una web donde un grupo de jugadores crear sus equipos de la nba para competir entre ellos durante la temporada. 

* El motivo de la elección es la de desarrollar un asistente de fichajes y ventas a partir de predicciones estadísticas reales aportadas por la web [FiveThirtyEight] (https://projects.fivethirtyeight.com/).

### Obtención de la url con el dataset de predicciones por jugador (RAPTOR) de la FiveThirtyEight.


The technical requirements for this project are as follows:

* You must obtain data from an API using Python.
* You must scrape and clean HTML from a web page using Python.
* The results should be two files - one containing the tabular results of your API request and the other containing the results of your web page scrape.
* Your code should be saved in a Jupyter Notebook and your results should be saved in a folder named output.
* You should include a README.md file that describes the steps you took and your thought process for obtaining data from the API and web page.

## Necessary Deliverables

The following deliverables should be pushed to your Github repo for this chapter.

* **A Jupyter Notebook (.ipynb) file** that contains the code used to work with your API and scrape your web page.
* **An output folder** containing the outputs of your API and scraping efforts.
* **A ``README.md`` file** containing a detailed explanation of your approach and code for retrieving data from the API and scraping the web page as well as your results, obstacles encountered, and lessons learned.

## Suggested Ways to Get Started

* **Find an API to work with** - a great place to start looking would be [API List](https://apilist.fun/) and [Public APIs](https://github.com/toddmotto/public-apis). If you need authorization for your chosen API, make sure to give yourself enough time for the service to review and accept your application. Have a couple back-up APIs chosen just in case!
* **Find a web page to scrape** and determine the content you would like to scrape from it - blogs and news sites are typically good candidates for scraping text content, and [Wikipedia](https://www.wikipedia.org/) is usually a good source for HTML tables (search for "list of...").
* **Break the project down into different steps** - note the steps covered in the API and web scraping lessons, try to follow them, and make adjustments as you encounter the obstacles that are inevitable due to all APIs and web pages being different.
* **Use the tools in your tool kit** - your knowledge of intermediate Python as well as some of the things you've learned in previous chapters. This is a great way to start tying everything you've learned together!
* **Work through the lessons in class** & ask questions when you need to! Think about adding relevant code to your project each night, instead of, you know... _procrastinating_.
* **Commit early, commit often**, don’t be afraid of doing something incorrectly because you can always roll back to a previous version.
* **Consult documentation and resources provided** to better understand the tools you are using and how to accomplish what you want.

## Useful Resources

* [Requests Library Documentation: Quickstart](http://docs.python-requests.org/en/master/user/quickstart/)
* [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Stack Overflow Python Requests Questions](https://stackoverflow.com/questions/tagged/python-requests)
* [StackOverflow BeautifulSoup Questions](https://stackoverflow.com/questions/tagged/beautifulsoup)

## Project Feedback + Evaluation

* __Technical Requirements__: Did you deliver a project that met all the technical requirements? Given what the class has covered so far, did you build something that was reasonably complex?

* __Creativity__: Did you add a personal spin or creative element into your project submission? Did you incorporate domain knowledge or unique perspective into your analysis.

* __Code Quality__: Did you follow code style guidance and best practices covered in class?

* __Total__: Your instructors will give you a total score on your project between:

    **Score**|**Expectations**
    -----|-----
    0|Does not meet expectations
    1|Meets expectactions, good job!
    2|Exceeds expectations, you wonderful creature, you!

This will be useful as an overall gauge of whether you met the project goals, but __the more important scores are described in the specs above__, which can help you identify where to focus your efforts for the next project!

