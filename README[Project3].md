![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: API and Web Data Scraping [Victor Triviño]


## Initial purpose

The purpose of this project is extract the same data for both API and WEB and check that both results are identical.

---

## API

The API selected has been 'https://public.opendatasoft.com/explore/dataset/atp/api/'

This API provides with all tennis results from 2001 to 2016 with different options to filter. Some filters are by tournament, by player or by round. You can put as many as they have in the documentation explained.

The data I was interested in getting was all Grand Slam winners. It does not matter which year or which tournament inside the Grand Slam.

In the Jupyter Notebook file I have done a get to obtain both the status_code and the response. 
Later on I have converted the json data into a dataframe by normalizing it two times, for the general results and for the record data.

For analysing purposes I have done many modifications using Pandas. For instance I have filtered the data as I wanted to get all winners but only from the Australian Open, which localition is Melbourne. That could have been done also in the API request but it made no difference at all.

Apart from dropping the columns which will not take part into the comparison with WEB data, an extra step has been done:
- split the column winner in Last Name; otherwise they will not have a perfect match.

Finally I have exported the data to a CSV 'API_AustralianOpen' as requested.


---

## WEB

The URL selected has been 'https://en.wikipedia.org/wiki/List_of_Grand_Slam_men%27s_singles_champions'.

This URL has a table with all the winners from 1887 until 2020 split into the 4 Grand Slams. As how the table, it has several issues to be solved previously.

I have used library Beautiful Soup for parsing the htlm and after this, finding the table under its class.

This table has been converted into a dataframe by using 'pd.read_html'.

For analysing purposes I have done many modifications using Pandas. I have filtered the data by year from 2001 to 2016, for matching with 'API_AustralianOpen' and I have only left the column 'Australian Open'-

Apart from dropping the columns which will not take part into the comparison with WEB data:
- I have used regex for replacing the text that is under '()' in the winner column
- split the column winner in Last Name;; otherwise they will not have a perfect match.

Finally I have exported the data to CSV 'WEB_AustralianOpen' as requested.


---

## Comparison

I have merged the two dataframes obtained.

I have compared them by adding an extra column called 'Match' which tells me if both columns are the sames. Which is true.

The reason for this comparison was check if both statistics matched perfectly or they have a mistake in them.

---

## Extra

Instead of getting the same data for the 'Australian Open', I could have taken a different Grand Slam.

I have change the WEB tournament selected to 'French Open' for wikipedia.

The merge result is different and so I am able for instance to check if a player won both tournaments the same year.

This is done in PR03-project-web[Victor Triviño] - extra
