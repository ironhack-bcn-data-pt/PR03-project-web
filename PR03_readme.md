![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project Pipelines

*Veronica Agnolutto*
*Data_Barcelona_aug.2o*



<p align="center">
  <img width="387" height="83" src="src/protectora.jpg">
</p>
Choose an adoptable dog, figure out the best place for her/him to live!


## Overview

The goal of this project is to understand what would be the **best home** in Barcelona based on its square mts for a **dog adopted** by the kennel of the city.


---

## Project structure  


* **web.ipynb** Jupyter notebook that contains the code to scrape the page of the 'protectora de Barcelona'.
* **api.ipynb** Jupyter notebook that contains the code to scrape the api of idealista.
* **datsets.ipynb** Jupyter notebook that contains where I merge the results from the web scrapping and the api investigation.
* **output** Folder that contains the cleaned datasets and the output of my data pipeline.
* **src** Images and resources.


## 1.:dog: Web scraping

* I chose the page of the **protectora de Barcelona** to find some adoptable dogs in the city.

## Objectives
* Parsing html webpages
* Extracting and organising the information
* Creating a dataframe

## Setbacks
* Extracting information from different URLs


## 2.:house_with_garden: API idealista

* I chose the of **idealista** to find sqm of the flats/houses in Barcelona

## Objectives
* I used the API of **idealista** to retrieve information of sqm of the flats/houses in Barcelona.
* Extracting and organising the information
* Creating a dataframe

## Setbacks
* Problems with authentication (tricky stuff)

## 3.:house_with_garden: + :dog: Merging dataframes

* Merging resulting dataframes of web scraping and API

## Objectives
* Joining dataframes using the dog size.
* Correcting inconsistencies.
* Extracting and organising the information
* Creating a final dataframe resuming the results

## Setbacks
* Joining dataframes
