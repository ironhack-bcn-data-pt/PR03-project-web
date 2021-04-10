![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Guided Project: API and Web Data Scraping

## Overview

El objetivo de este proyecto es el scrapeo del broker online DEGIRO. La plataforma DEGIRO es la que mejores comisiones tiene del mercado, pero la información disponible de sus productos es muy pobre y la interfaz poco amigable.

El objetivo del proyecto es el scrapeo de todos los productos financieros que ofrece de DEGIRO : acciones, bonos, fondos de inversión y etfs. En este proyecto nos centraremos en cruzar los etfs de DEGIRO con los de la web justETF para obtener toda la información finaciera pertinente a estos productos. Todos los productos financieros cuentan con un identificador único llamado ISIN, que es lo que se usará para cruzar la información entre plataformas. 

---

## DEGIRO

El scrapeo de DEGIRO se ha hecho mediante la API interna que utiliza el broker para solicitar la información de sus productos a su servidor. Esta API retorna un JSON con toda la información disponible. En la URL se especifica el tipo de producto, el numero de cuenta del usuario y un codigo identificador de la sesión iniciada. Cabe mencionar que este último se ha de introducir manualmente por el usuario cada vez que se ejecuta el programa, ya que cambia con cada login.

Además, aunque realmente no es necesario, el user-agent que se utiliza en cada request se selecciona de manera aleatoria de una lista de 1000 de un archivo de texto. También se especifica en el header un referer según que tipo de producto se scrapee. Por último, también se especifican otra serie de request headers que la web de DEGIRO pide. 

La información extraida se trata con la libreria BeautifulSoup, se parsea y se convierte en un DataFrame que se exporta como un csv. Se han creado 4 archivos csv: stocks.csv, bonds.csv, etfs.csv y funds.csv. Los archivos NO han sido limpiados.

## JustETFs

Para el scrapeo de la web JustETFs se ha utilizado Selenium para simular la acción de un usuario sobre un navegador. Se han seleccionado todos los campos que han parecido mas relevantes sobre los ETFs y que muestre 100 resultados por página. La información se ha vuelto a parsear mediante la libreria BeautifulSoup, y de la misma manera que antes, se ha convertido en un DataFrame y exportado como un csv llamado justETFs.csv

Los datos seleccionados son solo una muestra de los que la web ofrece, hay al menos 15 más que se pueden seleccionar si el usuario así lo cree necesario. Como antes, tampoco se han limpiado los datos exportados.

## Cruce de Datos

Para realizar el cruce de datos de los ETFs de DEGIRO con la información de la web de justETF lo primero que se ha hecho es limpiar los valores vacios de justETF y sustituirlos por NaNs. Seguidamente se convierten los datos numéricos que se encuentran en strings a número. Del total de etfs de DEGIRO se han eliminado todas las que tengan su ISIN duplicado, y se han cruzado con los de justETF, mediante un inner join. 

## Cosas a mejorar

Tuve muchos problemas con la ejecución de comandos que se realizaban antes de que la página terminase de cargar. Los tiempos de espera en Selenium se han hecho mediante la función time.sleep(), lo que es matar moscas a cañonazos. Las funciones previstas en Selenium para esto de Explicit Wait y de Implicit Wait, no fui capaz de aplicarlas de manera exitosa. Conceptualmente no termino de entender que es lo que hacen.

