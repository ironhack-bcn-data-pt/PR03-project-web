![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project Pipelines

*Veronica Agnolutto*
*Data_Barcelona_aug.2o*



<p align="center">
  <img width="387" height="83" src="src/protectora.jpg">
</p>

   *Choose an adoptable dog, figure out the best place for her/him to live!*


## Overview

The goal of this project is to understand what would be the **best home**for a **dog adopted** by the kennel of Barcelona, based on its square mts .


---

## Project structure  


* **web_scraping.ipynb** Jupyter notebook that contains the code to scrape the page of the 'protectora de Barcelona'.
* **api.ipynb** Jupyter notebook that contains the code to scrape the api of idealista.
* **datasets.ipynb** Jupyter notebook that contains the merged results from the web scrapping and the api investigation.
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
* Concatenating different dataframes


## 2.:house_with_garden: API idealista

* I chose the API of **idealista** to find the sqm of the flats/houses in Barcelona

## Objectives
* Using the API to retrieve information about the sqm of the flats/houses in Barcelona.
* Extracting and organising the information
* Creating a dataframe

## Setbacks
* Problems with authentication (tricky stuff)

## 3.:dog:+:house_with_garden: Merging dataframes

* Final analysis: which is the best home for an adoptable dog based on its size and the sqm of the place where it'll go to live?

## Objectives
* Merging dataframes using the dog size.
* Correcting inconsistencies.
* Extracting and organising the information
* Creating a final dataframe resuming the results

## Setbacks
* Joining dataframes
