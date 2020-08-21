<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Rocket launches
*Lola López Gilabert*

*Data Analytics Part Time Course | Barcelona June 2020*

## Content
- [Project Description](#project-description)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
This project obtains data from the future launches information from Space Launch Now site.
The API gives information about the launch window, the launch name, the rocket provider, etc.
From the website, I have obtained the description of the launch. In some cases there is a description of the payload inside the rocket, in other cases if there is no information about the payload yet.

## Workflow
The steps followed to complete the project were:
1) Import all the libraries needed
2) Use the API to get the information about the next launches:
- Specify the status of the launch: GO and TBD (to be defined) are the ones we are interested in
- Loop over the different pages in the API to get all the data
- Transform the data into a Data Frame and export it to a CSV file
3) Scrap the website to obtain the description of the payload for each launch:
- From the API data obtained, there is one column which is called *slug* that contains a URL which is the one to be used for each rocket launch
- Obtain a list with all the URLs
- Create a class that contains the functions to use: to generate a random user-agent, to scrape the website, to check if there is any error in the request's response, to print the output
- Define the parser to get the information of the launch name and its description
- Execute the previous functions and convert the data obtained into a Data Frame
- Export the data to a CSV file
4) Open both files, merge and export them into a new csv file
5) Analysis of the future launches. It includes a world map with the locations of the launch pads

## Organization
The repository is organised in the following way:
- README.md: this file
- output folder: it contains the csv files with the exported data from the API and the web as well as the fina output file after merging the initial files
- pictures folder: it contains the images used inside the notebook
- main.ipynb: juypter notebook containing the code in python
- main.slides.html: presentation slides

## Links
[SpaceLaunchNow](https://spacelaunchnow.me/) 
[Slides] main.slides.html   
