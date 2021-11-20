![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

## Overview
El objetivo de este estudio es el obtener datos relevantes a partir del codigo postal de un habitante de españa.

## Webs y Apis utilizadas

* https://api.idescat.cat : Para la pagina web de estadistica de cataluña. https://www.idescat.cat/
* https://api.zippopotam.us: Para obtener informacion de los codigos postales de cataluña y su latitud y longitud
* https://www.agenciatributaria.es/AEAT: Para obtener datos de renta per capita

## Datos obtenidos
- Fuente. idescat.    
    - datos_cat.csv: 
            - id: numero identificativo de la poblacion. Numero unico determinado por el INE
            - municipio: Nombre del municipio, numero de 6 digitos
            - cp: Codigo postal, numero de 5 digitos 
            - Superficie km: Superficie del municipio en Km (Dato de **2020**)
            - hab/km2: Densidad de habitantes por kilometro cuadrado (Dato de **2020**)
            - poblacion: Cantidad de habitantes del municipio (Dato de **2020**)
            - % estudos primarios: % de personas con estudios primarios o inferiores (Dato de **2019**)
            - % primera etapa secundaria: % de personas con estudios de primera etapa de secundaria (Dato de **2019**)
            - % segunda etapa secundaria: % de personas con estudios de segunta etapa de secundaria (Dato de **2019**)
            - % estudios superiores:% de personas con estudios superiores (Dato de **2019**)
            - % Poblacion desocupada: Poblacion activa/ poblacion desocupada del municipio (Dato de **2011**)
            - Pib por habitante: Producto interior bruto por habitante (Dato de **2019**)
            - Renta familiar disponible: Renta familiar disponible por habitante del municipio (Dato de **2018**)
- Fuente agencia tributaria:
     - renta_cp_spain.csv:
            - Nombre: Nombre del municipio
            - renta_media_disponible: Renta per capita media disponible por habitante (Dato de **2019**)
            - cp: Codigo postal
            
## Futuras mejoras
- datos__cat.csv: 
    - Problema en la obtencion de Poblacion desocupada, PIB por habitante y renta familiar en poblaciones pequeñas: Limpieza de df
- renta_cp_spain:
    - Obtener datos de mas municipios