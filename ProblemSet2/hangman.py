# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            guessed = False
            break
        else:
            guessed = True
    return guessed


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: guessed_string a string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_string = ''

    for char in secret_word:
        if char not in letters_guessed:
            guessed_string += '_ '
        else:
            guessed_string += char
    return guessed_string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    not_guessed = string.ascii_lowercase
    letters_left_to_guess = ''
    for char in not_guessed:
        if char not in letters_guessed:
            letters_left_to_guess += char
    return letters_left_to_guess


def check_user_input(user_guess):
    '''
    This function returns True if user_guess is NOT a digit, punctuation, or whitespace
    :param user_guess: a string
    :return: accepted a boolean of True or False
    '''
    bad_chars = string.digits + string.punctuation + string.whitespace
    if user_guess in bad_chars:
        accepted = False
    else:
        accepted = True
    return accepted


def check_if_vowel(user_guess):
    '''
    Check if the guess is a vowel
    :param user_guess: a string with a length of 1 character
    :return: is_a_vowel boolean
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    if user_guess in vowels:
        is_a_vowel = True
    else:
        is_a_vowel = False
    return is_a_vowel


def calculate_score(current_guesses, max_allowed_guesses, secret_word):
    '''
    :param current_guesses:
    :param max_allowed_guesses:
    :param secret_word:
    :return: total_score an integer representing the users total calculated score after a game
    '''
    unique_chars = []
    for char in secret_word:
        if char not in unique_chars:
            unique_chars.append(char)

    total_score = (max_allowed_guesses - current_guesses) * len(unique_chars)
    return total_score


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    # Settings
    max_allowed_guesses = 6
    max_allowed_warnings = 2

    # Init game variables
    current_guesses = 0
    warnings = 0
    letters_guessed = []

    print('\n I am thinking of a word that is', len(secret_word), 'letters long: \n',
          get_guessed_word(secret_word, letters_guessed), '\n', 'Available Letters: \n',
          get_available_letters(letters_guessed=letters_guessed), '\n')

    while current_guesses < max_allowed_guesses:

        print('Guesses left : ', (max_allowed_guesses - current_guesses), '\n ------')

        guess = input('Guess one letter...').lower()

        if len(guess) == 1:

            if check_user_input(guess) is True:
                current_guesses += 1

                if guess in letters_guessed:

                    if warnings < max_allowed_warnings:
                        warnings += 1
                        print('Oops! You have already guessed that letter. You have',
                              max_allowed_warnings - warnings, 'warnings left')

                    else:
                        current_guesses += 1
                        print('Oops! You have already guessed that letter. You have no warnings left')

                print('Word : ', get_guessed_word(secret_word, letters_guessed), '\n',
                      'Available Letters: ', get_available_letters(letters_guessed=letters_guessed), '\n')

                if is_word_guessed(secret_word, letters_guessed) is True:
                    print(secret_word, 'is correct, you win! Your score was',
                          calculate_score(current_guesses, max_allowed_guesses, secret_word))
                    break

                if check_if_vowel(guess) is True:

                    if guess in secret_word:
                        current_guesses = current_guesses
                    else:
                        current_guesses += 1

            else:

                if warnings < max_allowed_warnings:
                    warnings += 1
                    print('Oops! that is not a valid letter. You have',
                          max_allowed_warnings - warnings, 'warnings left')
                else:
                    current_guesses += 1
        else:
            print('Guess is too long! \n')
    else:
        print('Sorry, you ran out of guesses. The word was', secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
