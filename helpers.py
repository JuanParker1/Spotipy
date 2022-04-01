from pprint import pprint
# BELOW Only needed for temp_scores_2010s
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import html


def get_mode():
    print("Program options:")
    print("  1. Show the user's Fantano data")
    print("  2. Show the user's currently playing track")
    mode = int(input("Enter a mode: "))

    while True:
        if (mode >= 1) and (mode <= 2):
            break
        else:
            mode = int(input("Invalid input - please try again: "))

    return mode


def print_albums(albums):
    for i in albums:
        pprint(i[0])


def print_results(albums):
    # (list((artist + ' - ' + title, score, link)))
    for i in albums:
        print(i[0] + ': ' + str(i[1]) + '/10. URL: ' + i[2])


def print_avg_score(albums):
    # (list((artist + ' - ' + title, score, link)))
    all_scores = 0
    for i in albums:
        all_scores += i[1]
    average = all_scores / len(albums)
    print(average)

    if average >= 8:
        print("You should buy yourself a yellow flannel.")
    elif average >= 6:
        print("Not bad. Fantano says it's technically still a good score.")
    elif average >= 4:
        print("Not great. Maybe save a few more Death Grips albums.")
    else:
        print("Embarrassing. Red flannel.")

def print_unscored_albums(albums):
    for i in albums:
        if i[1] < 0:
            print(i[0])


def temp_scores_2010s():
    # Used to fill fantano_scores_2010s. Should not need to be used again.
    base = 'https://www.albumoftheyear.org/ratings/57-the-needle-drop-highest-rated/2010s/{}'
    output = {}

    for page_num in range(0, 80):
        # narrow down to part of page with score information
        url = base.format(str(page_num + 1))
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')
        results = soup.find(id="centerContent")

        titles_list = []
        scores_list = []

        # fill titles list
        meta_tags = soup.find_all('meta', attrs={'itemprop': 'name'})
        for tag in meta_tags:
            titles_list.append(html.unescape(str(tag).split('"')[1]).lower())

        # fill scores list
        temp_scores = results.find_all("div", class_="scoreValue")
        for score in temp_scores:
            scores_list.append(int(re.findall(r'\d+', str(score))[0]))

        for j in range(0, len(titles_list)):
            output[titles_list[j]] = scores_list[j]

        page_num += 1

    for key in output:
        print('"' + key + '": ' + str(int(output.get(key) / 10)) + ', ')

    return output
