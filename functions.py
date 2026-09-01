
def getFiveLetterWord(prompt):
    while True:
        userInput=input(prompt)
        if userInput != '':
            try:
                check=eval(userInput)
            except NameError:
                if len(userInput) > 5 or len(userInput)< 5:
                    print('The word must be five letters long!')
                else:
                    return userInput
            except SyntaxError:
                print('What did you even type?? Type a word for goodness sake!')
            else:
                print('Type a word not a number!')
        else:
            print('Empty Space Detected, type a five letter word!')
            

def play(question):
    while True:
        answer=input(question)
        if answer !='':
            try:
                check = eval(answer)
            except SyntaxError:
                print('What did you even type?? Type a word for goodness sake!')
            except NameError:
                if answer[0].lower() == 'y' or answer.lower() == 'yes':
                    print('Very well we shall start.')
                    return True
                elif answer[0].lower() == 'n' or answer.lower() == 'no':
                    print('very well. Have a good day!')
                    return False
                else:
                    print('Type yes or no...')
            else:
                print('Type a word not a number!')
        else:
            print('Empty Space Detected, type yes or no!')


