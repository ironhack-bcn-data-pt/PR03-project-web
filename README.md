![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Guided Project: API and Web Data Scraping

## Overview

In this project I tried to recover some data from both a website that shows some statistics for all the matchups in Hearthstone, a popular card game for PC and also check all the tournaments avaiable that qualify for bigger european tournaments. To obtain this I mixed some scrapping, with API usage + selenium. 

For those who want to understand a bit more about Hearthstone https://playhearthstone.com/en-us/new-to-hearthstone/

## Steps I took & thought process

1 - For the data scraping on Metastats was straigh forward, I accessed the webpage, checked the HTML, tried to do a request call on the url and the information I got was as I wanted to received to I converted it to a soup and just search for values and store them in a matrix , which I later convert into a Pandas Dataframe. 

2 - For Battlefy tournaments was far more complicated. First I realized that if I wanted to obtain groups of tournaments I should find the API for the search engine. With the network tab openened I went into the tournament search engine and observed the messages till I found 1 suspicious package json file. The Url revealed to me the structure I had to define. 

3- The Issue I faced then was that the json file didn-t contain all the tournaments between those dates, but contain a attribute with the next tournament so I just kept iterating quering into the url updating the startdate with the next_tournament_date up until this last one was superior to end date. This way I could obtain all tournaments and then filter all those who hadn't "Madrid Qualifier" on their name.

4- When you access the stats tab you see some json files being received , 1 of them contains all the data about all matches played in the tournament, that's what I wanted to obtain but one of the parameters "stage" I had no way to obtain it. So I had to play more around. Then I realized that the url I was in after clicking the stats tab contained that parameter aswell. So I knew what I had to do, access every tournament url, and then using selenium click on the stats tab so the url updates and I can obtain the stage_id to be able to use the API to obtain all results for all tournaments.

5- I faced sine Issues while trying to acomplish the selenium click, first of all this website doesn't show the stats tab if Chrome isn't maximiez, and therefore was crashing, so I had to add that option to the driver. After that still didn't worked, I assumed it was due to the component not being clickable yet so I set up a waiting till it was ready. Then it worked but the url didn't get updated, so I setup a sleep to wait for it. Then it worked and I could access all the matches for all the tournaments, store them into a custom class I created and then create separate dataframes for every one of them.

6-Export the data.


## Possible improvements

-The decklist are grouped by class and since there are classes which arquetypes can have wildly different matchups, having all of them merged doesn't seem proper for best data analysis.

-A tournament grouper class would be useful in order to posterior analysis of groups of tournaments which summarized all the data contained in those tournaments.



