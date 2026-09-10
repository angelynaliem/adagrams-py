from random import randint

def draw_letters():

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

    # Turn the dictionary's keys into a list to enable randint
    alphabet_keys_list = list(alphabet_dictionary.keys())
    # print(alphabet_keys_list)

    # Create a helper function to pick a random letter.  
    def pick_a_random_letter():
        random_alphabet_index = randint(0, len(alphabet_keys_list) - 1)
        random_letter = alphabet_keys_list[random_alphabet_index]
        return random_letter

    # Iterate through the dictionary until the length of the hand reaches 10
    while len(hand) < 10:

        # Pick a random letter
        one_letter = pick_a_random_letter()

        # Access the dictionary
        for key, value in alphabet_dictionary.items():

            # If the key matches the random letter and the value of the letter is more than 0 and hand has not reached 10 letters, add that letter to hand and deduct the value by 1
            if key == one_letter and value > 0 and len(hand) < 10:
                hand.append(key)
                alphabet_dictionary[key] -= 1

            # Otherwise, start over
            else:
                continue

    return hand
                
    # print(f"This is the hand: {hand}")
    # print(f"This is the remaining letters and quantity in the dictionary: {alphabet_dictionary}")

def uses_available_letters(word, letter_bank):

    # upper_case_word = word.upper()
    # print(upper_case_word)

    copy_letter_bank = []
    for letter in letter_bank:
        lower_letter = letter.lower()
        copy_letter_bank.append(lower_letter)

    # print(copy_letter_bank)

    lower_case_word = word.lower()

    word_in_letter_bank = True

    for letter in lower_case_word:
        if letter in copy_letter_bank:
            copy_letter_bank.remove(letter)
        else:
            word_in_letter_bank = False

    return word_in_letter_bank


def score_word(word):
    # Returns an integer which is the total score of the word
    # If the length of the word is 7-10, it gets additional 8 points
    # Each letter has its own number of points

    word_list = list(word.upper())
    word_uppercase = word.upper()
    total_points = 0
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

    if len(word) > 6 and len(word) < 11:
        total_points += 8

    print(f"This is the word {word}")
    print(f"This is the total points {total_points}")
    

    # Iterate through the dictionary (key: letter, value: point), if a key is in the word_list, update the total points.
    for i in range(len(word_list)):
        for key, value in points_dictionary.items():
            
            if key == word_list[i]:
                total_points += value

    
            
    return total_points

def get_highest_word_score(word_list):
    pass