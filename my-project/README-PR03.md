<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# API and Web Data Scraping
*[Kseniya Voronkova]*

*[Data Analytics Part Time Course, Barcelona September 2021]*

## Content
- [Project Description](#project-description)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description

The goal of this project is to practice what we have learned in the APIs and Web Scraping chapter of our program. 
For the API portion of the project I have chosen a Twitter API to obtain and analyse data from. 
For the web scraping part I have chosen a page of Nomenclator from Ajuntamento to Barcelona in order to discover the origin of the name of any street in the city. 


## Workflow
The steps followed to complete the project were:
##### API
1. Create and configure the authentication credentials in order to be able to make a call to the Twitter API.
2. Authenticate with Twitter. 
3. Collect data from the Streaming API, using 'tweepy' package.
4. Create a 'MyStreamListener' object that inherits from a general 'Stream' class included with 'tweepy'. It opens a new file in   which to store tweets and takes authentication credentials as arguments.
5. Filter tweets  by calling the 'filter' method.
6. Load and explore the Twitter data


##### Web Scraping
1. Download  a csv file with the codes of streets of Barcelona from an OpenData service from Ajuntamento de Barcelona.
2. Convert the CSV file to a pandas DataFrame
3. Scrap the Nomenclator website to obtain information about the history of names of streets of Barcelona:
- Building a URL using the codes obtained from the file 
- Using BeautifulSoup get the information on the street's name description, appriving date,former name and district
- Create a new DataFrame from the info obtained
- Concatenate two DataFrames
4. Save the data from the DataFrame into a CSV file

## Organization
The repository contains:
- README-PR03.md
- twitter_api.ipynb
- web_scraping.ipynb
- data folder: contains tweets.txt file with the collected tweets and the CARRERER.csv file downloaded from the OpenData service from Ayuntamenro de Barcelona.
- output folder: contains the csv file with the exported data from the web 
- twitter_api.slides.html: presentation slides
- web_scraping.slides.html:presentation slides

## Links
[OpenDataBCN](https://opendata-ajuntament.barcelona.cat/es/) 
[Nomenclator](http://www.bcn.cat/nomenclator/castella/welcome.htm) 