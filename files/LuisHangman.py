from random import randint


WORD_LIST = {
    'rand_word_1': 'linguistic',    #This is the word list that I changed
    'rand_word_2': 'amphipneustic',
    'rand_word_3': 'hypocrite',
    'rand_word_4': 'orkney',
    'rand_word_5': 'depression',
    'rand_word_6': 'convoluted',
    'rand_word_7': 'create',
    'rand_word_8': 'shadow',
    'rand_word_9': 'preendorsing',
    'rand_word_10': 'convenient'
}


HANGMAN = (      #HANGMAN will print when the user either gets a guess wrong or when a user gets it right
    """
    x-------x
    """,
    """
    x-------x
    |
    |
    |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    GAME OVER
    """
)


MAX = len(HANGMAN) - 1
num = randint(1, 10)
num_string = str(num)
words = 'rand_word_{}'.format(num_string)
WORD_TO_GUESS = WORD_LIST[words] #This sets the word equal to the word list that is chosen at random
HIDDEN = ['_'] * len(WORD_TO_GUESS)
LETTERS_GUESSED = []


def begin_game():
    hang_size = 0 #the size grows with user input and will print the different types o
    print "\tHANGMAN!" #prints the pic of the hangman that goes with the user input
    word_arr = list(WORD_TO_GUESS) #

    while hang_size < MAX:
        print str(HIDDEN)
        user_guess = raw_input('Guess a letter dude: ')

        if user_guess in LETTERS_GUESSED:
            print 'You already guessed that.. PAY ATTENTION!'
            user_guess = raw_input('Guess a letter dude: ')

        if user_guess in word_arr:
            print "Yeah yeah.. We're all impressed.. It's in the word woohoo.."

            for num in range(len(word_arr)):
                if user_guess == word_arr[num]:
                    HIDDEN[num] = user_guess
                    if HIDDEN.count('_') == 0:
                        print 'You win! Finally you did something right!'
                        quit()

        else:#this command always prints the following information and new hangman
            print "{}.. Really? That's the best you can do.. Not in my word..".format(user_guess)
            hang_size += 1
            print HANGMAN[hang_size]


begin_game() 