easy = "\n" + '''A ___1___ is created with the def keyword.
You specify the inputs a ___1___ takes by adding ___2___ separated
by commas between the parentheses. ___1___s by default return ___3___
if you don't specify the value to return. ___2___ can be standard data types
such as string, number, dictionary, tuple, and ___4___ or can be more complicated
such as objects and lambda functions.\n'''

medium = "\n" + '''We become not a melting pot but a beautiful mosaic.
Different ___1___, different ___2___, different ___3___, different ___4___, different dreams.\n'''

hard = "\n" + '''Let the word go forth from this time and ___1___, to friend and foe alike,
that the torch has been passed to a new ___2___ of Americans, born in this century,
tempered by war, disciplined by a hard and bitter peace, proud of our ancient heritage
and unwilling to witness or permit the slow undoing of those human rights
to which this nation has always been ___3___, and to which we are ___3___ today
at home and around the world. And so, my fellow Americans: ask not what your
___4___ can do for you, ask what you can do for your ___4___\n'''

blanks = ["___1___", "___2___", "___3___", "___4___"]
easy_answers = ["function", "parameters", "none", "list"]
medium_answers = ["people", "beliefs", "yearnings", "hopes"]
hard_answers = ["place", "generation", "committed", "country"]

print("\n" + "Let's play a game!" + "\n"
 "We will be playing a fill in the blanks game today, we have three different levels")

#game_selection = input("easy, medium or hard, which would you like to play? ")
intro = "You have selected "
attempts = "You will be given 5 guesses per round!\n"
difficulties = ['easy', 'medium', 'hard']

def game_selection():
    """
    - this function will allow the user to select what level of difficulty they would like to play
    - this function takes the user input and checks to see if it matches one of the difficulties
    - if a match is found it prints the selection to the user otherwise it tells the user to choose a different selection
    """
    global choice
    choice = input("easy, medium or hard, which would you like to play? ").lower()
    while choice not in difficulties:
        print("That's not an option")
        choice = input("easy, medium or hard, which would you like to play? ").lower()
    print("\n" + intro + choice + "!" + "\n")

game_selection()

def choose_game(choice):
    """
    - This function sets the game's difficulty
    - Using the user's selection the appropriate game and answers are chosen
    - This function will inform the user of the game they have selected as well as the number of guesses they will be given
    """
    global answers
    global game
    if choice == "easy":
        print(attempts)
        print(easy)
        answers = easy_answers
        game = easy
    if choice == "medium":
        print(attempts)
        print(medium)
        answers = medium_answers
        game = medium
    if choice == "hard":
        print(attempts)
        print(hard)
        answers = hard_answers
        game = hard

choose_game(choice)

def user_fail():
    """
    - This function lets the user know that they have answered incorrectly too many times and ends the game
    """
    print("\nYou've answered incorrectly too many times! Game over!")
    exit()

def user_wins():
    """
    - This function lets the user know that they have won and then ends the game
    """
    print("Congratulations you have won!")
    exit()

updated = game

def update_txt(current, user_guess):
    """
    - This function updates the text with the correct answers that the user enters
    """
    global updated
    print("That's correct")
    updated = updated.replace(str(blanks[current]),str(user_guess))
    print(updated)

def incorrect_answers(user_guess, count, current):
    while user_guess != answers[current]:
        print("That's incorrect")
        count = count - 1
        if count == 1:
            print("This is your last remaining guess, think hard! \n")
            user_guess = input("What should be substituted in for " + str(blanks[current]) + " ? ").lower()
        elif count > 0:
            print("you have " + str(count) + " guesses remaining! \n")
            user_guess = input("What should be substituted in for " + str(blanks[current]) + " ? ").lower()
        elif count == 0:
            user_fail()

def check_answers():
    """
    - This function checks the answers of the user's guess and tracks the count of errors the user makes
    - This function takes in user input that will be used to check if they match the answers
    - This function will call different functions depending on if the user wins, loses or answers correctly
    """
    count, current = 5, 0
    user_guess = input("What should be substituted in for " + str(blanks[current]) + " ? ").lower()
    while current < 4 and count > 0:
        if user_guess != answers[current]:
            incorrect_answers(user_guess, count, current)
        elif user_guess == answers[current]:
            update_txt(current, user_guess)
            current = current + 1
            if current == 4:
                user_wins()
            user_guess = input("What should be substituted in for " + str(blanks[current]) + " ? ").lower()


check_answers()
