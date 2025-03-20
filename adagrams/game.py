from random import randint

"""input:no parameters 
output: returns an array(list) of ten strings
each string should contain exactly one letter """
#edge cases
#letters should be randomly drawn from a pool of letters
#  

LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}

#WAVE 1
def draw_letters():
    # Step 1: create a list 
    letter_list = []
    #for loop goes through each letter in letterpool and counts the frequency of thst letter
    for letter, count in LETTER_POOL.items():
        #creates a list of that letter repeated and adds copies to letter_list
        letter_list.extend([letter] * count)  
    
    # Step 2: Draw 10 random letters
    #create empty list to store letters that are drawn
    drawn_letters = []
    # loop 10 times to draw 10 letters
    for _ in range(10):
        #pick a random index to draw from 
        random_index = randint(0, len(letter_list) - 1) 
        #removes that letter from the pool of letters 
        drawn_letters.append(letter_list.pop(random_index))  
    return drawn_letters


#WAVE2
def uses_available_letters(word, letter_bank):
    pass

#WAVE3
def score_word(word):
    pass


#WAVE4
def get_highest_word_score(word_list):
    pass