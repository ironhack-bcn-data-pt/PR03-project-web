![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# API and Web Data Scraping


## API 

I used the https://footystats.org/api/ to get all the data that I will handle during the project part 1.

- I cleaned the columns from the Data Frame to extract the information that I am going to use during this project.
- I renamed the columns to make easy to understand the content.
- I rearrange the order of the columns.
- I extracted the name,id,games of the home team.
- I created a Data Frame to manipulate the information.
- I calculated the Number of Victory, Tie and Lose games per team.
- I created my own Data Frame
- I ordered the Data Frame by Wins. I created two new columns, the number of games played and the probability of winning and Tie per team.
- I saved all the information in a TXT file.
- I loaded TXT file.
- I anwered the follow questions:
                                -The top 5 teams with more probability of tied games in the Premier League
                                -The top 5 teams with more lost games in the Premier League.
                                - The winner of the Premier League by the number of victories.

## Web Data Scraping

I used this website to extract all the information for this project part 2 'http://sofifa.com/players?offset=0'

- I imported the tools that we are going to use in this project.
- I created a function that extract the information from the website.
- I extracted the body of the whole website code.
- I extracted from the website the name of the players and created a list that contain the names of the players.
- I extracted from the website the team and season, where the per players are at the moment and created a list that contain the team and season of the players at the moment.
- I extracted the age per player from the website and created a list that contain the age per player.
- I extracted the value per player from the website and created a list that contain the value per player.
- I extracted all the salaries from the website and  created a list that contain all the salaries per player.
- I created a dictionary with the all variables.
- I created a data frame to show the final results of the value per player in the market at the moment.
- I created a code that shows you from which position of the table you wants to see the players, for example, if you tells from 1 will shows you from the first position of the table and if you tell 30 it will start to show you the players from the 30 position forward, It will take longer than usual if you put a number over 10.
-I saved all the information in a CSV file.
- I loaded CSV file.
- I anwered the follow questions:
                                - The top 5 best salary of players
                                - The top 5 youngest most expensive players of football.
                                - The top 5 oldest footballer well paid.




