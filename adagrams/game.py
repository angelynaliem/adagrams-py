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

    # print(f"This is the word {word}")
    # print(f"This is the total points {total_points}")
    

    # Iterate through the dictionary (key: letter, value: point), if a key is in the word_list, update the total points.
    for i in range(len(word_list)):
        for key, value in points_dictionary.items():
            
            if key == word_list[i]:
                total_points += value

    
            
    return total_points

def get_highest_word_score(word_list):

    # dictionary_word_and_its_point = {}
    # winning_word = word_list[0]
    # winning_total_point = score_word(word_list[0])
    winning_word = ""
    winning_total_point = 0
    # dictionary_highest_scores = {}
    # final_winner = []
    # final_winner_tuple = ()
    # shortest_word = None 
    # shortest_length = 0
    # lowest_point = 0
    # list_winning_words = []
    # list_winning_words_length = []
    

    # for i in range(1, len(word_list)):
    for word in word_list:

        # Code that I got with Kage's help
        # new_winning_total_point = score_word(word_list[i])
        # if new_winning_total_point > winning_total_point:
        #     winning_total_point = new_winning_total_point
        #     winning_word = word_list[i]

        # elif winning_total_point == new_winning_total_point:
        #     if len(word_list[i]) == 10 and len(word_list[i]) != len(winning_word):
        #         winning_word = word_list[i]
        #         winning_total_point = score_word(word_list[i])
        #     if len(winning_word) < 10 and len(word_list[i]) < len(winning_word):
        #         winning_word = word_list[i]
        #         winning_total_point = score_word(word_list[i])

        #Code that doesn't work
        # new_winning_total_point = score_word(word_list[i])
        new_winning_total_point = score_word(word)

        if winning_total_point < new_winning_total_point:
            winning_total_point = new_winning_total_point
            # winning_word = word_list[i]
            winning_word = word

        elif winning_total_point == new_winning_total_point:
            # if len(word_list[i]) == 10 and len(winning_word) != 10: #why not just use len(winning_word)
            if len(word) == 10 and len(winning_word) != 10:
                # winning_word = word_list[i]
                winning_word = word
                winning_total_point = new_winning_total_point

            # elif len(winning_word) != 10 and len(word_list[i]) < len(winning_word): #why elif/if, why can't use !=/<
            # elif len(winning_word) != 10 and len(word) < len(winning_word):
            elif len(winning_word) != 10 and len(word) < len(winning_word):
                # winning_word = word_list[i]
                winning_word = word
                winning_total_point = new_winning_total_point

    return (winning_word, winning_total_point)

    # for word in word_list:
        #     total_point_per_word = score_word(word)
        #     dictionary_word_and_its_point[word] = total_point_per_word

    # Get the highest scores dictionary 
    # for key, value in dictionary_word_and_its_point.items():
    #     if value > winning_total_point:
    #         winning_total_point = value
    #         dictionary_highest_scores = {
    #             key : value
    #             }
    #     elif value == winning_total_point:
    #         dictionary_highest_scores[key] = value

    # dictionary_highest_scores_tuple = tuple(dictionary_highest_scores.items())

    # Iterate through the tuple to compare and find the shortest word or the word with 10 letters, or if the length and points are the same, then return whichever comes first
    # for i in range(len(dictionary_highest_scores_tuple)):
    #     current_length_word = len(dictionary_highest_scores_tuple[i][0])
    #     current_key = dictionary_highest_scores_tuple[i][0]
    #     current_value = dictionary_highest_scores_tuple[i][1]

    # #     # list_winning_words.append(key)
    # #     # list_winning_words_length.append(len(key))
    #     for j in range(i):
    #         previous_length_word = len(dictionary_highest_scores_tuple[j][0])
    #         previous_key = dictionary_highest_scores_tuple[j][0]
    #         previous_value = dictionary_highest_scores_tuple[j][1]

    #         # If there is only one tuple in the tuple
    #         if len(dictionary_highest_scores_tuple) == 2:
    #             # final_winner.append(current_key)
    #             # final_winner.append(current_value)
    #             # final_winner_tuple = tuple(final_winner)
    #             final_winner_tuple = (current_key, current_value)

    #         # This conditional is to get the first winner in the list
    #         elif current_length_word < previous_length_word:
    #             # final_winner.append(current_key)
    #             # final_winner.append(current_value)
    #             # final_winner_tuple = tuple(final_winner)
    #             final_winner_tuple = (current_key, current_value)

    #         # This conditional is to make the first word that has 10 letters win
    #         elif current_length_word == 10:
    #             # final_winner.append(current_key)
    #             # final_winner.append(current_value)
    #             # final_winner_tuple = tuple(final_winner)
    #             final_winner_tuple = (current_key, current_value)

            # This conditional is to get the first word if the total points and the length of the words is the same
            # elif len(dictionary_highest_scores_tuple) > 2 and len(key)
                
            # This conditional is to get the word with the shortest length
            # if len(key) > len(dictionary_highest_scores_tuple[i+1][0]) and len(key) < 10:
                #     final_winner.append(key)
                #     final_winner.append(value)
                #     final_winner_tuple = tuple(final_winner)
                    
                
                # if len(key) < 10:
                #     if value > lowest_point:
                #         lowest_point = value
                #         final_winner.append(key)
                #         final_winner.append(value)
                #         final_winner_tuple = tuple(final_winner)
            
                

    # print(f"This is all the winning words: {list_winning_words}")
    # print(f"This is all the winning words length: {list_winning_words_length}")

        # If there is only one tuple in the tuple
        # if len(dictionary_highest_scores_tuple) == 2:
        #     final_winner.append(current_key)
        #     final_winner.append(current_value)
        #     final_winner_tuple = tuple(final_winner)

        
        # # This conditional is to get the first word that has 10 letters
        # elif len(dictionary_highest_scores_tuple) > 2 and len(key) == 10:
        #     final_winner.append(current_key)
        #     final_winner.append(current_value)
        #     final_winner_tuple = tuple(final_winner)

    return final_winner_tuple

        # This conditional is to get the first word if the total points and the length of the words is the same
        # elif len(dictionary_highest_scores_tuple) > 2 and len(key)

        # This conditional is to get the word with the shortest length
        # if len(key) > len(dictionary_highest_scores_tuple[i+1][0]) and len(key) < 10:
        #     final_winner.append(key)
        #     final_winner.append(value)
        #     final_winner_tuple = tuple(final_winner)
    

        # if len(key) < 10:
        #     if value > lowest_point:
        #         lowest_point = value
        #         final_winner.append(key)
        #         final_winner.append(value)
        #         final_winner_tuple = tuple(final_winner)

    # return final_winner_tuple


        
