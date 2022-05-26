from random import randint
def run_game():
    welcome()
    while True: #Main Game Loop   
        for i in range(0, 10):
            answer = get_hints(correct_answer(),input_answer())
            if answer == 'You Got it!!':
                print('You Got it!!')
                break
            print(get_hints(correct_answer(),input_answer()))
        
        print('Hey, You ran out of chances.')
        print('The correct answer was {ans}'.format(ans=input_answer))
        print('\nDo you want to play again?(Yes/No)')
        ques=input()
        if not ques.upper().startswith('Y'):
            break
    print('Thanks For Playing!!')



def welcome():
    print('Bagels, a deductive logic game.')
    print('By Prazwal D. Stark prazwaldstark@gmail.com\n\n')
    print('I am thinking of a 3-digit number. Try to guess what it is in at most 10 guesses.')
    print('Here are some clues:')
    print('When I say:    That Means:')
    print('PICO        -   One digit is correct but in the wrong direction.')
    print('Fermi       -   One digit is correct and is in the right position.')
    print('Bagels      -   No digit is correct.')
    print('I have thought of a number.\nHere You Go!\nYou got 10 guesses.\n\n')
    
def correct_answer():
    canswer = str(randint(100, 1001))
    return canswer

def input_answer():
    ianswer = input()
    return ianswer

def get_hints(canswer,ianswer):
    '''Return the function with the hint i.e. PICO, FERMI, BAGELS'''
    if canswer == ianswer:
        return 'You Got it!!'
    else:
        hint=[]
        for i in range(0,3):
            if canswer[i] == ianswer[i]:
                hint.append('Pico')
            elif ianswer[i] in canswer:
                hint.append('Fermi')
        if  len(hint) == 0:
            return 'Bagels'
        else:
            return ' '.join(hint.sort())



            
                