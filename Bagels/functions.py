from random import randint
def correct_answer():
    canswer = str(randint(100, 1001))
    return canswer

def input_answer():
    ianswer = input('>')
    return ianswer

def get_hints(ca,ia):
    '''Return the function with the hint i.e. PICO, FERMI, BAGELS'''
    if ca == ia:
        return 'You Got it!!'
    else:
        hint=[]
        for j in range(0,3):
            if ca[j] == ia[j]:
                hint.append('Pico')
            elif ia[j] in ca:
                hint.append('Fermi')
        if  len(hint) == 0:
            return 'Bagels'
        else:
            return hint.sort()