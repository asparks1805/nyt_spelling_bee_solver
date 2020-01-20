Welcome to nyt_spelling_bee_solver
=====================
This is a Python project to obtain all of the possible answers to the daily NY Times Spelling Bee game.

**Current Version: v0.10**

## Table of content

- [Overview](#overview)
- [Set up](#set-up)
- [References/sources](#references)
- [To do list](#to-do-list)
- [Other notes](#other-notes)

# Overview
This is a solver for all of the possible answers to the daily 
[NY Times Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee) game. The game consists of 
a "center" letter that is required to be used in any words and 6 "outside" letters that can also be used.

I pulled a [dictionary file](https://github.com/dwyl/english-words) off of Github and modified it to make the 
spelling bee processing go more quickly. First, I removed all words with fewer than 4 characters (per the NYT 
rules). Next, I added an alphabet array to each word and flagged whether the character was present in the word
or not. Then I removed all words that use more than 7 letters of the alphabet (as the game limits you to 7 
unique letters).

The alphabet array is used to quickly identify the letters that are not in the daily puzzle.

# Set up
Just run it. No pip installs or other set up required.

# References
- Dictionary file: https://github.com/dwyl/english-words 

# To do list
- Error handling

# Other notes
- None