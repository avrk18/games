import random
import hangman_display
import csv

player_dictionary = {}


def record_check(player):
    c = -1
    try:
        # if the csv already exists:
        file = open('Hangman_Record.csv', 'r')
        file.close()
        # if the file doesnt exist, the previous two lines will give an error, and program will jump to "except"
        file = open('Hangman_Record.csv', 'a+', newline="")
        file.seek(0)
        ereader = csv.reader(file)
        ewriter = csv.writer(file)
        count = -1
        x = -1
        # x is a variable to store the index of the player's details
        for i in ereader:
            count += 1
            if i[0] == player:
                x = count
                player_list = i
        if x != -1:
            pwd = input("Enter Password: ")
            if i[4] == pwd:
                print("Welcome back", player, '!')
                player_dictionary[player] = []
            else:
                print("Sorry! Wrong password")
                return (-1, player_list)
        else:
            # to create a new player profile
            file.seek(0, 2)
            pwd = input("Please type in a password for your profile: ")
            player_list = [player, 0, 0, 0, pwd]
            ewriter.writerow(player_list)
            print("Hello", player, '!')
            player_dictionary[player] = []
            x = count + 1
        file.close()
        c = 20
        return (x, player_list)
    except:
        pass
    if c == -1:
        # this will execute only if "try" gave error, hence, creating both a new csv and player profile
        file = open('Hangman_Record.csv', 'w', newline="")
        ewriter = csv.writer(file)
        ewriter.writerow(["Username", "Number of games", "Points", "High Score", "pswd"])  # headings of the columns
        pwd = input("Please type in a password for your profile: ")
        player_list = [player, 0, 0, 0, pwd]
        ewriter.writerow(player_list)
        print("Hello", player, '!')
        file.close()
        return (1, player_list)  # 1 is the index position of the player record


def initialize():
    global player_dictionary
    L = ["Batman", "Tenet", "Tom And Jerry", "Inception", "Shawshank Redemption", "The Notebook",
         "The Amazing Spiderman", "Iron Man", "The Incredible Hulk", "Pulp Fiction", " Forrest Gump", "The Terminal",
         "The Fault In Our Stars", "Inglourious Basterds", "Interstellar", "Mud", "The Godfather", "The Dark Knight",
         "Twelve Angry Men", "Schindler's List", "Fight Club", "The Matrix", "Goodfellas", "Parasite", "Train To Busan",
         "Minari", "Spirited Away", "Saving Private Ryan", "Whiplash", "The Intouchables", "The Prestige",
         "Taare Zameen Par", "Dil Chahta Hai", "Don", "Lagaan", "Sholay", "Bhaag Milkha Bhaag", "Jo Jeeta Wohi Sikandar",
         "Zindagi Na Milegi Dobara","A silent voice", "Nomadland", "The Pianist", "Silver Linings playbook", "before sunrise",
         "Predestination", "Kill Bill", "Baby Driver", "Dead Poets Society", "Cars"]
    play_list = []
    for i in L:#This is to make sure that the user doesn't get the same movie again
        if i not in player_dictionary[player]:
            play_list += [i]
    movie = play_list[random.randrange(len(play_list))]
    player_dictionary[player]+=[movie]#Movie added to the list of movies player has got in this turn
    mov_str = ''
    for i in movie:
        if i == ' ':
            mov_str += '/ '
        else:
            mov_str += '_ '
    return movie, mov_str


def check(ch, movie, mov_str, count):
    new_mov_str = ''
    i = 0

    if len(ch) != 1:#To check if the word or movie itself is guessed by the user and not a letter.
        if ch.lower() == movie.lower():
            return count, new_mov_str
        else:
            if ch.capitalize() in movie.split():
                while i in range(len(movie)):
                    if movie[i:i + len(ch)] == ch.capitalize():
                        for j in range(i, i + len(ch)):
                            new_mov_str += movie[j] + ' '
                        i += len(ch)
                    else:
                        new_mov_str += mov_str[2 * i] + ' '
                        i += 1

            else:
                for i in range(len(movie)):
                    new_mov_str += mov_str[2 * i] + ' '
                count += 1
    #Check for letter
    elif ch.upper() in movie or ch.lower() in movie:
        for i in range(len(movie)):
            if (movie[i] == ch.lower()) or (movie[i] == ch.upper()):
                new_mov_str += movie[i] + ' '
            else:
                new_mov_str += mov_str[2 * i] + ' '
    else:
        new_mov_str = mov_str
        count += 1

    return count, new_mov_str


def result(count):
    points = 11 - count
    if count == 11:
        print("Oh no, you ran out of moves! \n The movie was", movie)
        print("Better luck next time!")
    else:
        print("Good job! You guessed the movie", movie, "correctly! ")
        print("You have won", points, "points!")
    return (points)


def record_update(x, points):
    # extracting info from csv
    file = open('Hangman_Record.csv', 'r', newline="")
    ereader = csv.reader(file)
    L = []
    for i in ereader:
        L.append(i)
    file.close()

    # rewriting the record
    file = open('Hangman_Record.csv', 'w', newline="")
    writer = csv.writer(file)
    L[x][1] = int(L[x][1]) + 1
    L[x][2] = int(L[x][2]) + points
    if int(L[x][3]) < points:
        if int(L[x][3]) != 0:
            print("You beat your previous high score!")
        L[x][3] = points
    writer.writerows(L)
    file.close()


def record_display(player):
    print()
    file = open('Hangman_Record.csv', 'r')
    ereader = csv.reader(file)
    L_blank = []
    for i in ereader:
        L_blank.append(i)
    for i in L_blank:
        if i[0] == player:
            print("Stats:")
            print("Username:", i[0])
            print("Games played: ", i[1])
            print("Points: ", i[2])
            print("High Score:", i[3])

    file.close()


# main program

while True:
    print("Welcome to Hangman!")
    index = -1
    while index < 0:
        player = input("Enter username (if you do not already have a profile, type in a new username): ")
        index, player_list = record_check(player)
        # index here is index of the player's record in the csv

    while True:
        print()
        print("\nMenu:")
        print("1. Rules")
        print("2. Play")
        print("3. Stats")
        print("4. Exit")
        choice = input('''Enter your choice: 
        Enter 1 for Rules, 2 For playing, 3 for viewing your stats or 4 for exiting the game: ''')
        print()

        if choice == '1':
            print('''RULES:

 Hello''',player, ''', Welcome to Hangman!
.This is a fun one-player game where you have 11 chances to guess the movie generated by the system.

.The System will initially choose a movie, and show blank spaces like _ corresponding to a letter in the name of it.

.Your entry can be a letter or the entire movie, or a word.

.Type in the letter you think is present in the given movie.If it is indeed present then the system will show you where ever
it is and you can again continue, otherwise another step of the drawing is completed.

.If you think you know which movie it is, you can type the entire movie's name and find out if it is correct or not

.Be Careful! If you make too many wrong guesses then the entire drawing will be completed and you will lose.

.Try to guess the movie with as few mistakes as possible. All The best!!''')



        elif choice == '2':
            print()
            count = 0
            movie, mov_str = initialize()
            print(mov_str)

            while "_" in mov_str and count < 11:
                ch = input("Enter your guess (letter/name of movie): ")
                print()
                count, mov_str = check(ch, movie, mov_str, count)
                if "_" in mov_str:
                    hangman_display.display(count)
                if count != 11:
                    print(mov_str)
            points = result(count)
            record_update(index, points)

        elif choice == '3':
            record_display(player)


        elif choice == '4':
            break

        else:
            print("Invalid Choice")

    print("Thanks for Playing! \n")
    















