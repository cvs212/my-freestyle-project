from bs4 import BeautifulSoup
import requests
import json
import csv
import os

api_key = "ch121382676"

baby_name = "stephen"

#meaning

baby_url = f"http://www.momjunction.com/baby-names/{baby_name}/"

response = requests.get(baby_url)
response_html = response.text

soup = BeautifulSoup(response_html, 'html.parser')

span_class = (soup.find_all("div", "single_baby_name_description"))

print(span_class[0].text)
#error_message = NO DATA FOUND PLEASE TRY WITH ANY OTHER NAME

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
#assert: len = 200

babynames_boys = read_names_from_file()

def difference_in_ranks():
    difference = int(names["2018 rank"]) - int(names["2017 rank"])
    print(difference)

for names in babynames_boys:
    difference_in_ranks()
