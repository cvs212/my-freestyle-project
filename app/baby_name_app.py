from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import json
import csv
import os
import itertools
import random

#inspiration for menu design from the inventory management project
menu = """
    ---------------------------------------------------------
                BABY & REGULAR NAME RESOURCE APP
    ---------------------------------------------------------
    Hello and welcome to the Baby & Regular Name Resource app!
    You have the option to choose from a variety of functions
    that'll help you narrow down a baby name or simply look up
    more information about a particular name. Please look at
    the below menu and select the function that you want to
    explore.

    User Input     | Description
    ----------------------------
    'Rank'         | This will give you the rankings of the
                     most popular baby names in 2018. You
                     can choose the rankings based on gender.
    'Meaning'      | You can see the meaning of a name of your
                     choice.
    'Information'  | This option will allow you to view the
                     related names and origin of a name of
                     your choice.
    'Letter'       | You can view baby name rankings and other
                     helpful information by letter.
    'Random'       | Choose this option if you want the app
                     to help you choose a name randomly.

    Please enter your choice in the line below:
    """


def name_meaning():
    user_name_meaning = input("You selected the name meaning function. Please enter the name that you'd like to find the meaning of: ")
    baby_url = f"http://www.momjunction.com/baby-names/{user_name_meaning}/"
    response = requests.get(baby_url)
    response_html = response.text
    soup = BeautifulSoup(response_html, 'html.parser')
    span_class = (soup.find_all("div", "single_baby_name_description"))
    print("-----------------------------------------------------------------")
    print(span_class[0].text)
    print("-----------------------------------------------------------------")

def name_letter():
    user_name_letter = input("You selected the Names by Letter function. Please enter the letter by which you want to look up name information: ")
    if user_name_letter.isalpha() == False or len(user_name_letter) > 1: #source for checking whether an input is a letter: https://stackoverflow.com/questions/18667410/how-can-i-check-if-a-string-only-contains-letters-in-python
        print("The input that you entered isn't valid. Please try again.")
        quit("Stopping the program. Feel free to start over.")
    user_name_letter_gender = input("Cool. Now enter the gender of names that you're interested in ('Male' or 'Female'): ")
    if user_name_letter_gender == "Male" or user_name_letter_gender == "male":
        matching_names = [names for names in babynames_boys if names["name"][0] == user_name_letter]
        filename = "babynames_" + user_name_letter + "_" + user_name_letter_gender + ".csv"
        for names in matching_names:
            print("------------------------------")
            print("Name: " + names["name"] + " | 2018 Rank: " + names["2018 rank"] + " | 2017 Rank: " + names["2017 rank"])
            difference_in_ranks(names)
            per_capita(names)
            print("------------------------------")
            filepath_2 = os.path.join(os.path.dirname(__file__), "data", filename)
            with open(filepath_2, "w") as csv_file: #source: notes from the inventory management project
                writer = csv.DictWriter(csv_file, fieldnames=["2018 rank", "name", "2017 rank", "popularity", "gender", "syllables"])
                writer.writeheader()
                for names in matching_names:
                    writer.writerow(names)
    elif user_name_letter_gender == "Female" or user_name_letter_gender == "female":
        matching_names = [names for names in babynames_girls if names["name"][0] == user_name_letter]
        filename = "babynames_" + user_name_letter + "_" + user_name_letter_gender + ".csv"
        for names in matching_names:
            print("------------------------------")
            print("Name: " + names["name"] + " | 2018 Rank: " + names["2018 rank"] + " | 2017 Rank: " + names["2017 rank"])
            difference_in_ranks(names)
            per_capita(names)
            print("------------------------------")
            filepath_2 = os.path.join(os.path.dirname(__file__), "data", filename)
            with open(filepath_2, "w") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=["2018 rank", "name", "2017 rank", "popularity", "gender", "syllables"])
                writer.writeheader()
                for names in matching_names:
                    writer.writerow(names)
    else:
        print("You seemed to have made an error with the last input. Feel free to try again")
        name_letter()

def name_random(): #source for helpful tips on random choice: https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
    user_input_random = input("You selected the Random Name Generator. Please enter the gender of the name you'd like ('Male', 'Female', or 'Either'): ")
    if user_input_random == "Male" or user_input_random == "male":
        random_name_male = random.choice(babynames_boys)
        print("------------------------------------------------------------")
        print("The name that the app generated for you is: " + random_name_male["name"])
        print("------------------------------------------------------------")
    elif user_input_random == "Female" or user_input_random == "female":
        random_name_female = random.choice(babynames_girls)
        print("------------------------------------------------------------")
        print("The name that the app generated for you is: " + random_name_female["name"])
        print("------------------------------------------------------------")
    elif user_input_random == "Either" or user_input_random == "either":
        all_names = []
        all_names.append(babynames_boys)
        all_names.append(babynames_girls)
        random_all_names = random.choice(all_names)
        random_all_names_2 = random_all_names[0]
        print("------------------------------------------------------------")
        print("The name that the app generated for you is: " + random_all_names_2["name"])
        print("------------------------------------------------------------")
    else:
        print("------------------------------------------------------------")
        print("Your input isn't a valid request. Please try again.")
        print("------------------------------------------------------------")

def name_information():
    user_input_related_names = input("You selected the Name Information function. Please enter the name that you'd like to see more information for: ")
    load_dotenv()
    api_key = os.environ.get("BEHIND_THE_NAME_KEY") or "Looks like you don't have an API Key from Behind The Name. Please set an environent variable called 'BEHIND_THE_NAME_KEY'." #source: your demo on local environment variables
    behind_the_name_related_names_url = f"https://www.behindthename.com/api/related.json?name={user_input_related_names}&usage=eng&key={api_key}"
    response_3 = requests.get(behind_the_name_related_names_url)
    response_json_2 = json.loads(response_3.text)
    if "error" in response_3.text: #source: your demo on validation errors in class
        print("The name you requested isn't in the system. Please try again.")
        print(behind_the_name_related_names_url)
        quit("Stopping the program. Feel free to start over.")
    related_names = response_json_2['names']
    print(f"These are the related names for {user_input_related_names.title()}: ")
    for names in related_names:
        print(str(related_names.index(names) + 1) + ". " + names)
    behind_the_name_origin_url = f"https://www.behindthename.com/api/lookup.json?name={user_input_related_names}&key={api_key}"
    response_2 = requests.get(behind_the_name_origin_url)
    response_json = json.loads(response_2.text)
    print(f"This is the language origin for {user_input_related_names.title()}: " + (response_json[0]['usages'][0]['usage_full']))

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

babynames_boys = read_names_from_file()

babynames_girls = read_names_from_file_girl()

def name_rankings():
    user_gender_preference = input("Please enter the gender of the baby names you'd like to see rankings for: ")
    if user_gender_preference == "Male" or user_gender_preference == "male":
        user_rankings_range = input("Great. Now enter the number of the last ranked name you'd like to see in your list: ")
        last_index = int(user_rankings_range)
        list_babynames_boys = babynames_boys[0:last_index] #source for index pull: https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python
        for name in list_babynames_boys:
            print("------------------------------")
            print("Name: " + name["name"] + " | 2018 Rank: " + name["2018 rank"] + " | 2017 Rank: " + name["2017 rank"])
            difference_in_ranks(name)
            per_capita(name)
            print("------------------------------")
    elif user_gender_preference == "Female" or user_gender_preference == "female":
        user_rankings_range = input("Great. Now enter the number of the last ranked name you'd like to see in your list: ")
        last_index = int(user_rankings_range)
        list_babynames_girls = babynames_girls[0:last_index]
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

def run():
    user_menu_choice = input(menu)
    if user_menu_choice == 'Rank' or user_menu_choice == 'rank':
        name_rankings()
    elif user_menu_choice == 'Meaning' or user_menu_choice == 'meaning':
        name_meaning()
    elif user_menu_choice == 'Information' or user_menu_choice == 'information':
        name_information()
    elif user_menu_choice == 'Letter' or user_menu_choice == 'letter':
        name_letter()
    elif user_menu_choice == 'Random' or user_menu_choice == 'random':
        name_random()
    else:
        print("Looks like the option you entered isn't valid. Please try again.")
        run()

if __name__ == "__main__":
    run()
