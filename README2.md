# API and Web Data Scraping Project


## Project Goal

The goal is to use the API at The Movie Data Base (TMDb.org) to search for Billy Wilder, a prolific awarded director and writer, in order to find all his movies which he worked in as a director, writer or producer. TMDb will give us such important facts like the year he started to work in a movie and his filmography. With these data we can start scraping the website Oscars.org, to find out when he was awarded and in which category. 

### API

First of all, we need to create an account at TMDb.org to get the API key. It's an easy process, quite fast reply, by the way. There are two versions for the API, v3 and v4. I chose the v3 in order to find more suport posts to get help and to work with the API key instead of the token for v4.


### Oscars Academy Awards

This is the offcial website released by the Oscars Academy where you can find all the awards categories and people who was nominated since the very beginning of the ceremonies in 1929. The search for awards is set up by decades, and each decade, obviously, contains a period of ten years. But the website is structured in a way that it is not productive to scrape, since the all the data for nominations is in a list, with the same class name for everything and it's all very nested and complicated.


### Wikipedia

As suggested by Paula, it would be less complicated to search for the Oscars in Wikipedia. There is a table for all the awards, but it has irregular rows. I've been trying to extract what I want, but making a DF with that information is too hard. Or at least, I don't find the right way.

## The project is not ended, my hope is to add the results soon and make the csv. 
