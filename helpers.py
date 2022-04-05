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
    albums.sort(key=lambda x: (-x[1], x[0].split(' - ')[0], x[0].split(' - ')[1]))
    # (list((artist + ' - ' + title, score, link)))
    for i in albums:
        print(str(i[1]) + '/10: ' + i[0])
        # print(i[0] + ': ' + str(i[1]) + '/10. URL: ' + i[2])


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
            # print(i[0] + 'URL: ' + i[2])


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
        results = results.find_all("div", class_="albumListRow")

        for album in results:
            temp_score = album.find_all("div", class_="scoreValue")[0]
            score = int(re.findall(r'\d+', str(temp_score))[0]) / 10

            link = album.find_all("a", href=re.compile("http://open.spotify.com/album/"))
            if len(link) > 0:
                output[str(link[0]).split('"')[3]] = int(score)

        page_num += 1

    return output
