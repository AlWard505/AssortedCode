import random
from random import *

body = 1
head = 1
tail = 1
leg = 4
antenna = 2
eye = 2
overall = 11
while overall != 0:
    enter = input('press enter to role')
    role = randint(1, 6)
    print('you rolled',role)
    
    if role == 6:
        if body != 0:
            body = body - 1
            overall = overall - 1
            print('you got a body')
        else:
            print('you allready have a body')
    elif role == 5:
        if body == 0:
            if head != 0:
                head = head - 1
                overall = overall - 1
                print('you got a head')
            else:
                print ('you already have a head')
        else:
            print('you need a body')
    elif role == 4:
        if body == 0:
            if tail != 0:
                tail = tail - 1
                overall = overall - 1
                print('you got a tail')
            else:
                print ('you already have a head')
        else:
            print('you need a body')
    elif role == 3:
        if body == 0:
            if leg != 0:
                leg = leg - 1
                overall = overall - 1
                print('you got a leg')
            else:
                print ('you already have 4 legs')
        else:
            print('you need a body')
    elif role == 2:
        if body == 0:
            if head == 0:
                if antenna != 0:
                    antenna = antenna - 1
                    overall = overall - 1
                    print('you got antenna')
                else:
                    print(' you already have 2 antenna')
                
            else:
                print ('you need a head')
        else:
            print('you need a body')
    elif role == 1:
        if body == 0:
            if head == 0:
                if eye != 0:
                    eye = eye - 1
                    overall = overall - 1
                    print('you got an eye')
                else:
                    print(' you already have 2 eyes')
                
            else:
                print ('you need a head')
        else:
            print('you need a body')
print('you win')
         
