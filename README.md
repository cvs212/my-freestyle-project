# Baby & Regular Name Resource App

This app serves as a resource for evaluating and researching baby names and regular names. Within this app, you can look at the latest baby name popularity rankings, meanings and statistics of names, and also randomly generate a name based on user inputs.

## Prerequisites

Requires Python 3.x. Additionally, for any functions that involve API connections to ‘Behind The Name,’ you may want to register on the site to get an API key. The app already has an API key that’s populated from a .env file. In the event the app can’t pull any API feeds from ‘Behind The Name,’ simply get an API key from the site and save it in your .env file as ‘BEHIND_THE_NAME_KEY’.

## Installation

This app makes use of the following packages:

BeautifulSoup
dotenv
Requests
Json
CSV
OS
Itertools
Random

Please download these packages through the pip install command.

## Setup

Make sure to download the two .csv files in the ‘data’ directory. The ‘data’ directory should contain the following .csv files:

babynames_boys
babynames_girls

Additionally, an API key from ‘Behind The Name’ saved as a ‘BEHIND_THE_NAME_KEY’ environment variable is needed for the 'information' function of the app. You can do this either through a .env file or in your commmand prompt. It may be more helpful to set the environment variable through your command prompt since the .env method is more prone to errors. Also be mindful of quotation marks when setting up your environment variable since quoations aren't part of the 'Behind The Name' url.

## Usage

To get a ranking of the most popular baby names by gender, enter this command: Rank. Also, specify the gender of the names in which you’re interested.

To get the meaning behind a name, enter this command: Meaning. Also, specify the name of choice.

To get more information and statistics behind a name (i.e. related names), enter this command: Information.

To receive a list of ranked names by letter, enter this command: Letter

To have the app generate a name at random, enter this command: Random.

## Testing

The automated tests are found in the ‘test’ directory.


