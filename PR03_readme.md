![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project Pipelines

*Veronica Agnolutto*
*Data_Barcelona_aug.2o*



<p align="center">
  <img width="387" height="83" src="src/protectora.jpg">
</p>

   *Choose a dog to adopt and find out the best location for her/him!*


## Overview

The goal of this project is to understand what would be the **best home**for a **dog adopted** by the kennel of Barcelona, based some characteristics of the place where it'll go to live(square mts, presence of terrace/garden...).


---

## Project structure  


* **web_scraping.ipynb** Jupyter notebook that contains the code to scrape the page of the 'protectora de Barcelona'.
* **api.ipynb** Jupyter notebook that contains the code to scrape the API of idealista.
* **home_sweet_home.ipynb** Jupyter notebook that contains the results from the web scrapping and the API investigation.
* **output** Folder that contains the cleaned datasets and the output of my data pipeline.
* **src** Images and resources.


## 1.:dog: Web scraping

* I chose the page of the **protectora de Barcelona** to find some adoptable dogs in the city.

## Objectives
* Parsing html webpages
* Extracting and organising the information
* Creating a dataframe

## Setbacks
* Extracting information from different pages
* Concatenating different dataframes


## 2.:house_with_garden: API idealista

* I chose the API of **idealista** to find some characteristics of the houses in Barcelona

## Objectives
* Using the API to retrieve information about the sqm of the flats/houses in Barcelona(square mts, presence of terrace/garden...).
* Extracting and organising the information
* Creating a dataframe

## Setbacks
* Problems with authentication (tricky stuff)
* Problems with the number of accesses --> API blocked! \o/

--> Project in PROGRESS: waiting for new credentials to use the API

## 3.:dog:+:house_with_garden: Merging dataframes

* Final analysis: Which is the best home for a dog on adoption based on its size and some characteristics of the place where it'll go to live(square mts, presence of terrace/garden...)?

## Objectives
* Merging dataframes using the dog size.
* Correcting inconsistencies.
* Extracting and organising the information
* Creating a final dataframe resuming the results

## Setbacks
* Joining dataframes
