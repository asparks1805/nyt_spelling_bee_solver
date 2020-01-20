import argparse
import json

parser = argparse.ArgumentParser(description='NYT Spelling Bee solver')
parser.add_argument('-r', type=str, help='Required letter at the center of the puzzle')
parser.add_argument('-o', type=str, help='Other 6 letters around the outside of the puzzle')
args = parser.parse_args()

# Set up the puzzle
required_letter = args.r
other_letters = args.o
puzzle_letters = required_letter + other_letters
alphabet_string = 'abcdefghijklmnopqrstuvwxyz'

def fetch_dictionary():
    filename = 'words_dictionary.json'
    if filename:
        with open(filename, 'r') as f:
            dictionary = json.load(f)
    return dictionary

def get_letters_not_in_puzzle():
    MAX_CHAR = 26
      
    present = [0] * MAX_CHAR 
    for i in range(0, MAX_CHAR): 
        present[i] = 0
  
    l1 = len(alphabet_string) 
    l2 = len(puzzle_letters) 
      
    for i in range(0, l1): 
        present[ord(alphabet_string[i]) - ord('a')] = 1
          
    for i in range(0, l2): 
        if(present[ord(puzzle_letters[i]) - ord('a')] == 1 or 
           present[ord(puzzle_letters[i]) - ord('a')] == -1): 
            present[ord(puzzle_letters[i]) - ord('a')] = -1
        else: 
            present[ord(puzzle_letters[i]) - ord('a')] = 2

    letters_to_filter_out = ''

    for i in range(0, MAX_CHAR): 
        if(present[i] == 1 or present[i] == 2): 
            letters_to_filter_out = letters_to_filter_out + chr(i + ord('a'))

    return letters_to_filter_out

def words_with_required_letter():
    possible_words = {}

    for word in dictionary:
        if dictionary[word][required_letter] == 1:
            possible_words[word] = dictionary[word]
    
    return possible_words

def filter_words_with_letters_not_in_puzzle(letters_to_filter_out, possible_words):

    for word in list(possible_words):
        counter = 0

        while counter < 19:
            filter_letter = letters_to_filter_out[counter]
            if possible_words[word][filter_letter] == 1:
                possible_words.pop(word)
                break
            counter = counter + 1
            
    return possible_words


dictionary = fetch_dictionary()
letters_to_filter_out = get_letters_not_in_puzzle()
possible_words = words_with_required_letter()
answers = filter_words_with_letters_not_in_puzzle(letters_to_filter_out, possible_words)
for word in answers:
    print(word)




