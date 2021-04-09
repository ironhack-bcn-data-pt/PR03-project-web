![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Guided Project: API and Web Data Scraping

## Overview

The goal of this project is to create a database from the movie rating website [FilmAffinity](https://www.filmaffinity.com/).

---

## Technical Requirements

The technical libraries used in this project are the following:

* BeautifulSoup
* Selenium

## Files

The following files were generated during this project.

* **``Filmaffinity.ipynb``** A Jupyter Notebook file that contains all the code I used to extract the information from FilmAffinity.
* **``Filmaffinity v2.ipynb``** A Jupyter Notebook file with the structure of the code that should be used to extract the entire database of FilmAffinity but not executed because it would retrieve a *429 - Too many requests* error message.
* **``pelistop.csv``** A CSV file that contains the result of the web scrapping done in ``Filmaffinity.ipynb``.

## Process

The first thing I did was to observe the structure of the website. Since in the search results the website only retrieves 999 entries, I looked for another way to extract the data. There is an option to search every movie [by topic](https://www.filmaffinity.com/es/topics.php) in which there is an option to navigate through all the movies after clicking on each one of the topics with no limit because it's sorted by pages.

The volume of the database is so high that it retrieves a *429 - Too many requests* error message, as explained in the Jupyter Notebook ``Filmaffinity v2.ipynb``, which is why I decided to analyze the top 50 most voted movies for each topic.

The steps I followed to do that are contained in the Jupyter Notebook ``Filmaffinity v2.ipynb`` and the result in the file ``pelistop.csv``.
