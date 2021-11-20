![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Guided Project: API and Web Data Scraping

## Overview

For this project I used google sheets api to retrieve information from a google document of mine.
The document contains a list of boardgames I own, with some information about them.
I followed the google api tutorial (https://developers.google.com/sheets/api/quickstart/python):
 - allowing google sheets api in my account
 - creating and user with token access
 - installing specific python libraries for google sheets provided by google itself

Once i got access to my google document, i noticed the format was a bit unconvential, so i had to do several transformations to create the desired dataframe.

Once i had my df ready, i thought about what information could be scrapped from the internet. I decided to retrieve 3 things:
- An image from the game
- A link to buy the game
- A written review of the game

I achieved that using internal apis and webscrapping.

For the image i used boardgamegeek.com internal api to retrieve the game_id, and the i used format strings to retrieve a collection of images stored in this web.

For the link i used boardgamegeek internal api to retrieve the game_id, and the i used format strings to retrieve the first item from the boardgame market.

For the review I used regex and scrapping methods from BeautifulSoup library, to search reviews on misutmeeple.com.

I store the results from the google api on collection.csv, and the results from review scrapping on reseñas.csv.

With all the information collected i created a boardgame recommender which takes some inputs from the user and chooses a game that matches the criteria (and shows all the information retrieved that is available: image, link to buy, and review).

# URL presentation

https://slides.com/gerarddomenechdomingo/project-03/


