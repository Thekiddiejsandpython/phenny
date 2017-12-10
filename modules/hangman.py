#!/usr/bin/python3

"""
hangman.py - when bored on #apertium IRC :P
author: Extraterrestrial Seahorse <https://github.com/Thekiddiejsandpython>
"""

import random
words = ["begiak", "apertium", "dictionary", "processing", "language", "natural", "phenny", "lexical", "analysis", "generator"]

# Phenny.say("Guess")
def hangman(phenny, input):
  word = words[random.randint(0, len(words)-1)]
  msg = "-" * len(word)
  phenny.say("Type: 'quit' to stop playing")
  while (msg != word):
    guess = input("What is your Guess: ")
    if(len(guess) > 1):
      if(guess=="quit"):
        msg=word
      elif guess == word:
        msg=word
      else:
        phenny.say("One letter at a time (Unless you write the correct answer)")
    if word.find(guess) != (-1) :
      tmp = list(msg)
      for a in range(0, len(tmp)):
        if(guess == word[a]):
          tmp[a] = word[a]
      msg = ''.join(tmp)
      phenny.say(msg)
    else:
      phenny("try again")
      phenny(msg)
  
   phenny.say("Begiak is proud :D")    

hangman.commands = ['hangman'] 
hangman.name = 'hangman'
hangman.example = '.hangman'

if __name__ == '__main__':
print(__doc__.strip())
