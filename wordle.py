# modules
from random import randint
from colorama import Fore, Back, Style
from functions import getFiveLetterWord, play # this was made to make this file look less cluttered 

# file needed to import and pick a word at random
file = open('words.txt', 'r')

proper_words=[]
lines= file.readlines()
for word in lines:
    free=word.strip('\n')
    proper_words.append(free)

selector = randint(0, len(lines) - 1)
word=proper_words[selector]


file.close()

# needed variables
count=0
something=[]
red = Back.RED
reset= Style.RESET_ALL 
yellow = Back.YELLOW
green = Back.GREEN


answer = play("would you like to play?(type yes or no): ")

while answer:
    guess=getFiveLetterWord('\nGuess the five letter word: ').upper()
    count+=1
    values=[0,0,0,0,0]
    if count < 6:
        if len(guess)< 5 or len(guess)>5:
            print('Only five letter words are allowed')
            count-=1
        else:
            if guess not in proper_words:
                print('That word is not in our current dictionary please use another word!')
                count-=1
            else:
                if guess == word:
                    print(f"The Wordle for today is {word}, you guessed it right!")
                    break
                else:
                    for letter in word:
                        for char in guess:
                            something.append(char)                            
                            if char != letter:
                                check=values[len(something)-1] + 1  
                                values.insert(len(something)-1, check)
                                values.pop(len(something))
                                 

                            if len(something) == 5:
                                something.clear()
                    i=0

                    for occur in values:
                        if occur == 5:
                            index = values.index(occur,i)
                            print(red + guess[index], end='' + reset)
                            i+=1
                            
                        else:
                            index = values.index(occur,i)
                           
                            if guess[index] == word[index]:
                                print(green + guess[index], end='' + reset)
                                i+=1
                            else:
                                print(yellow + guess[index], end='' + reset)
                                i+=1                                     
    else:
        print(f'No!, the word is {word}!')
        break
            

        
