import argparse
import json
import os

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
        with open(os.path.dirname(os.path.realpath(__file__)) + '/' + filename, 'r') as f:
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

    sorted_possible_words = {}
    for k in sorted(possible_words, key=len, reverse=True):
        sorted_possible_words[k] = possible_words[k]
            
    return sorted_possible_words

def panagram(answers):
    panagram_words =[]
    p1 = puzzle_letters[0]
    p2 = puzzle_letters[1]
    p3 = puzzle_letters[2]
    p4 = puzzle_letters[3]
    p5 = puzzle_letters[4]
    p6 = puzzle_letters[5]
    p7 = puzzle_letters[6]

    for possible_panagram in answers:
        if answers[possible_panagram][p1] == 1 and answers[possible_panagram][p2] == 1 \
            and answers[possible_panagram][p3] == 1 and answers[possible_panagram][p4] == 1 \
            and answers[possible_panagram][p5] == 1 and answers[possible_panagram][p6] == 1 \
            and answers[possible_panagram][p7] == 1:
            
            panagram_words.append(possible_panagram)
        
    
            


    return panagram_words


dictionary = fetch_dictionary()
letters_to_filter_out = get_letters_not_in_puzzle()
possible_words = words_with_required_letter()
answers = filter_words_with_letters_not_in_puzzle(letters_to_filter_out, possible_words)
panagram_words = panagram(answers)

print('----------ALL ANSWERS------------')
for word in answers:
    print(word)
print('-------PANAGRAM ANSWERS----------')
for word in panagram_words:
    print(word)






