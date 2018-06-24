# Project Planning

## Problem Statement

### Primary User

Anyone can enjoy this app, but it can be especially useful to the following audiences:
1.	Parents-to-be who are trying to decide what to name their child
2.	Users who want to see what their future child’s name would be in a fun way
3.	Users who want to find out more information behind their names or any other names

### Users Need Statement

Deciding which name to give a child is a cumbersome process whose effect is felt for a lifetime. There are countless resources and guides for baby names, but trying to research all of them can confuse parents-to-be even more. It would be great for people who are undertaking this significant decision to have a ‘one-stop-shop’ of information that simplifies the baby-name decision process.

### As-is Process

1.	Search for a list of top-ranked baby boy or baby girl names.
2.	Look for a separate page that lists the top-ranked baby boy or baby girl names from the previous year.
3.	Go to a separate page that showcases the meaning and origin behind each name.
4.	Decide which name is the best name for an upcoming child based on many sources.

### To-be Process Description

1.	User will run a script that will show a menu of program choices.
2.	Among the choices that the user can select from the menu are:
  a.	List popular baby boy or girl names from 2018 based on a user’s input and range of choice
  b.	List the rankings of a particular name from a previous year
  c.	Show famous people that share the name of a user’s choice (Edit 6.23.18: This option is no longer available.)
  d.	Give the background and meaning behind a particular name
  e.	List the related names of the name from a user’s input
  f.	Give the user a choice to have the app randomly select a name for them
3.	Results from user choices that display a list would be printed in a csv file.

## Information Requirements

1.	Desired gender of the baby if the user wants to research baby names based on gender or if the user wants to have the app randomly pick a baby name.
2.	A preferred name if the user simply wants to see the meaning behind a particular name.
3.	A letter if the user wants to research baby names based on a particular letter.

### Information Output

1.	A list of popular baby boy or girl names from 2018 and the previous year.
2.	The meaning and origin behind a name.
3.	Related names.
4.	Famous people who share a particular name. (Edit 6.23.18: This option is no longer available.)
5.	A results.csv file that outlines the list results from the user’s inputs.

## Technology Requirements

1.	I will need to use the API feed from the ‘Behind The Name’ web site. This API feed will have the origin, related names, and gender.
2.	In order to get the meanings behind each name, I will need to use the ‘BeautifulSoup’ package to web scrape information from particular sites. Two particular sites of interest are ‘Behind The Name’ and ‘Baby Center.’ A final decision on which site to use will be determined based on how easy it is to web scrape information from a particular site.

### Python Package Requirements

The main 3rd party package required for this is the ‘BeautifulSoup’ module in order to web scrape the meanings behind each baby name.
Other than that, the program will frequently use the ‘os,’ ‘requests,’ ‘json,’ ‘dotenv,’ and ‘csv’ packages.

### Hardware Requirements

This application will only run on local machines.
