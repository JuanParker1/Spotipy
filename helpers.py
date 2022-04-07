
def get_mode():
    print("Program options:")
    print("  1. Show the user's Fantano data")
    print("  2. Show the user's currently playing track")
    print("  3. Show the user's top artists")
    print("  1. Show the user's top tracks")
    output = int(input("Enter a mode: "))

    while True:
        if (output >= 1) and (output <= 4):
            break
        else:
            output = int(input("Invalid input - please try again: "))

    return output


def print_results(albums):
    albums_list = []
    print('Alphabetically: ')
    for i in albums:
        print(str(albums[i][0]) + '/10: ' + i)
        albums_list.append((i, albums[i][0], albums[i][1]))

    print('')
    print('')

    albums_list.sort(key=lambda x: (-x[1], x[0].split(' - ')[0], x[0].split(' - ')[1]))
    print('By score: ')
    for i in albums_list:
        print(str(i[1]) + '/10: ' + i[0])


def print_score_data(albums):
    # (list((artist + ' - ' + title, score, link)))
    num_10s = 0
    num_9s = 0
    num_8s = 0
    num_7s = 0
    num_6s = 0
    num_5s = 0
    num_4s = 0
    num_3s = 0
    num_2s = 0
    num_1s = 0
    num_0s = 0
    all_scores = 0

    for i in albums:
        all_scores += albums[i][0]
        if albums[i][0] == 10:
            num_10s += 1
        elif albums[i][0] == 9:
            num_9s += 1
        elif albums[i][0] == 8:
            num_8s += 1
        elif albums[i][0] == 7:
            num_7s += 1
        elif albums[i][0] == 6:
            num_6s += 1
        elif albums[i][0] == 5:
            num_5s += 1
        elif albums[i][0] == 4:
            num_4s += 1
        elif albums[i][0] == 3:
            num_3s += 1
        elif albums[i][0] == 2:
            num_2s += 1
        elif albums[i][0] == 1:
            num_1s += 1
        elif albums[i][0] == 0:
            num_0s += 1

    average = round(all_scores / len(albums), 2)
    print('AVERAGE SCORE: ' + str(average))

    if average >= 8:
        print("You should buy yourself a yellow flannel.")
    elif average >= 6:
        print("Not bad. Fantano insists it's a good score.")
    elif average >= 4:
        print("Not great. Maybe save a few more Death Grips albums.")
    else:
        print("Embarrassing. Red flannel.")
    print('')
    print('Number of 10/10s: ' + str(num_10s))
    print('Number of 9/10s: ' + str(num_9s))
    print('Number of 8/10s: ' + str(num_8s))
    print('Number of 7/10s: ' + str(num_7s))
    print('Number of 6/10s: ' + str(num_6s))
    print('Number of 5/10s: ' + str(num_5s))
    print('Number of 4/10s: ' + str(num_4s))
    print('Number of 3/10s: ' + str(num_3s))
    print('Number of 2/10s: ' + str(num_2s))
    print('Number of 1/10s: ' + str(num_1s))
    print('Number of 0/10s: ' + str(num_0s))

    return


def print_unscored_albums(albums):
    for i in albums:
        if i[1] < 0:
            print(i[0])


