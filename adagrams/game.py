from random import randint

def draw_letters():
    """
    Returns a list of 10 strings/letters
    Randomly choose from a list of alphabet pool where each letter has a different quantity
    """

    # Set a new dictionary that holds the letters and their corresponding quantity.
    alphabet_dictionary = {
        "A" : 9,
        "B" : 2,
        "C" : 2,
        "D" : 4,
        "E" : 12,
        "F" : 2,
        "G" : 3,
        "H" : 2,
        "I" : 9,
        "J" : 1,
        "K" : 1,
        "L" : 4,
        "M" : 2,
        "N" : 6,
        "O" : 8,
        "P" : 2,
        "Q" : 1,
        "R" : 6,
        "S" : 4,
        "T" : 6,
        "U" : 4,
        "V" : 2,
        "W" : 2,
        "X" : 1,
        "Y" : 2,
        "Z" : 1,
    }

    # Returns an array which is a list. Create a variable with an empty list where we will store the 10 letters.
    hand = []

    # Create a list to enable randint that takes into account the quantity of each letter
    alphabet_pool = []

    for letter, quantity in alphabet_dictionary.items():
        for i in range(quantity):
            alphabet_pool.append(letter)

    # Then pick a random letter from that pool if the player hasn't reached 10 letters. Remove that letter once a player takes the letter.
    while len(hand) != 10:
        letter_index = randint(0, len(alphabet_pool) - 1)
        letter = alphabet_pool[letter_index]
        hand.append(letter)     
        alphabet_pool.remove(letter)

    return hand

def uses_available_letters(word, letter_bank):
    """
    Returns a boolean to check if the player is able to make a word from the player's letter bank
    Word is a string
    Letter_bank is a list of strings/letters
    """

    # Create a copy of the letter_bank to stick to lower/upper case
    copy_letter_bank = []
    for letter in letter_bank:
        lower_letter = letter.lower()
        copy_letter_bank.append(lower_letter)

    lower_case_word = word.lower()

    # Initiatlize the boolean variable to keep track of the status
    word_in_letter_bank = True

    # Iterate through the word then check if each letter is in the letter_bank. Remove that letter once used.
    for letter in lower_case_word:
        if letter in copy_letter_bank:
            copy_letter_bank.remove(letter)
        else:
            word_in_letter_bank = False

    return word_in_letter_bank


def score_word(word):
    """
    Returns an integer which is the total score of the word
    If the length of the word is 7-10, it gets additional 8 points
    Each letter has its own number of points
    Takes in a string which is the word
    """

    # Stick to one upper/lower case so the word matches when compared
    word_list = list(word.upper())

    # Keep track of the total points variable
    total_points = 0

    # Create the dictionary of the alphabet and the point per letter
    points_dictionary = {
        "A" : 1,
        "E" : 1,
        "I" : 1,
        "O" : 1,
        "U" : 1,
        "L" : 1,
        "N" : 1,
        "R" : 1,
        "S" : 1,
        "T" : 1,
        "D" : 2,
        "G" : 2,
        "B" : 3,
        "C" : 3,
        "M" : 3,
        "P" : 3,
        "F" : 4,
        "H" : 4,
        "V" : 4,
        "W" : 4,
        "Y" : 4,
        "K" : 5,
        "J" : 8,
        "X" : 8,
        "Q" : 10,
        "Z" : 10
    }

    # If the word has 7-10 letters, add the bonus points
    if len(word) > 6 and len(word) < 11:
        total_points += 8

    # Iterate through the dictionary (key: letter, value: point), if a key is in the word_list, update the total points.
    for i in range(len(word_list)):
        for key, value in points_dictionary.items():
            
            if key == word_list[i]:
                total_points += value
            
    return total_points

def get_highest_word_score(word_list):
    """
    Returns a tuple which is the highest point word and the highest point
    Takes in a list of strings/words
    """

    # Keep track of the winning word and the total point
    winning_word = ""
    winning_total_point = 0

    # Iterate through the list of words
    for word in word_list:

        new_winning_total_point = score_word(word)

        # If the total point of the word we're iterating is bigger than the current one we have, replace it and that becomes the new inner
        if winning_total_point < new_winning_total_point:
            winning_total_point = new_winning_total_point
            winning_word = word

        # But if it's a tie, the first one with 10 letters in the word wins, unless it's not 10 letters and it has the shortest length, then that word wins.
        elif winning_total_point == new_winning_total_point:
            if len(word) == 10 and len(winning_word) != 10:
                winning_word = word
                winning_total_point = new_winning_total_point
            
            elif len(winning_word) != 10 and len(word) < len(winning_word):
                winning_word = word
                winning_total_point = new_winning_total_point

    return (winning_word, winning_total_point)
