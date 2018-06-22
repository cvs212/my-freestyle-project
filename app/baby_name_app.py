from bs4 import BeautifulSoup
import requests
import json
import csv
import os

api_key = "ch121382676"

baby_name = "stephen"

#meaning


def name_meaning():
    user_name_meaning = input("You selected the name meaning function. Please enter the name that you'd like to find the meaning of: ")
    baby_url = f"http://www.momjunction.com/baby-names/{user_name_meaning}/"
    response = requests.get(baby_url)
    response_html = response.text
    soup = BeautifulSoup(response_html, 'html.parser')
    span_class = (soup.find_all("div", "single_baby_name_description"))
    print(span_class[0].text)
#error_message = NO DATA FOUND PLEASE TRY WITH ANY OTHER NAME
#test validation
#details

behind_the_name_url = f"https://www.behindthename.com/api/lookup.json?name={baby_name}&key={api_key}"

response_2 = requests.get(behind_the_name_url)
response_json = json.loads(response_2.text)
print("This is the language origin: " + (response_json[0]['usages'][0]['usage_full']))

#related names

behind_the_name_related_names_url = f"https://www.behindthename.com/api/related.json?name={baby_name}&usage=eng&key={api_key}"

response_3 = requests.get(behind_the_name_related_names_url)
response_json_2 = json.loads(response_3.text)
related_names = response_json_2['names']
print(f"These are the related names for {baby_name.title()}: ")
for names in related_names:
    print(names)

#famous people with similar related_names

#baby_name_famous_people = "https://www.thebump.com/b/chris-baby-name"

#response_4 = requests.get(baby_name_famous_people)
#response_4_html = response_4.text

#soup_2 = BeautifulSoup(response_4_html, 'html.parser')

#li_class = (soup_2.find_all("li", "famous-name specific-name mobile-row-item-2 desktop-row-item-3"))

#print(li_class[0].text)

#reading list of dictionaries

def read_names_from_file(filename="babynames_boys.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "data", filename)
    babynames_boys = []
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            babynames_boys.append(dict(row))
    return babynames_boys

def read_names_from_file_girl(filename="babynames_girls.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "data", filename)
    babynames_girls = []
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            babynames_girls.append(dict(row))
    return babynames_girls
#assert: len = 200

babynames_boys = read_names_from_file()

babynames_girls = read_names_from_file_girl()

def name_rankings():
    user_gender_preference = input("Please enter the gender of the baby names you'd like to see rankings for: ")
    user_rankings_range = input("Great. Now enter the number of the last ranked name you'd like to see in your list: ")
    last_index = int(user_rankings_range)
    list_babynames_boys = babynames_boys[0:last_index]
    list_babynames_girls = babynames_girls[0:last_index]
    if user_gender_preference == "Male" or user_gender_preference == "male":
        for name in list_babynames_boys:
            print("------------------------------")
            print("Name: " + name["name"] + " | 2018 Rank: " + name["2018 rank"] + " | 2017 Rank: " + name["2017 rank"])
            difference_in_ranks(name)
            per_capita(name)
            print("------------------------------")
    elif user_gender_preference == "Female" or user_gender_preference == "female":
        for name in list_babynames_girls:
            print("------------------------------")
            print("Name: " + name["name"] + " | 2018 Rank: " + name["2018 rank"] + " | 2017 Rank: " + name["2017 rank"])
            difference_in_ranks(name)
            per_capita(name)
            print("------------------------------")
    else:
        print("Your selection isn't an option in this app. Please try again.")
        name_rankings()

def difference_in_ranks(name):
    difference = int(name["2018 rank"]) - int(name["2017 rank"])
    if difference > 0:
        print("The ranking for this name increased by " + str(abs(difference)) + " spots.") #source for absolute value: https://docs.python.org/2/library/functions.html
    elif difference < 0:
        print("The ranking for this name decreased by " + str(abs(difference)) + " spots.")
    else:
        print("The ranking for this name stayed the same over the last 2 years.")

def per_capita(name):
    popularity_formatted = "{0:,}".format(int(name["popularity"]))
    percent_per_capita = int(name["popularity"]) / 1000000
    percent_per_capita_formatted = "{:.2%}".format(percent_per_capita) #source for percent formatting: https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php
    print("The population for this name is " + popularity_formatted + ", or " + percent_per_capita_formatted + ", per million babies.")


name_rankings()
name_meaning()
