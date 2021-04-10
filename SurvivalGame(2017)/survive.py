#important things to do, add a health system add hunger system
import time
import random
from random import *   
ab = [#ab = abilites and/or tools
    ['pic',50],         #0
    ['axe',50],         #1   
    ['shovel',50],      #2
    ['hoe',0],          #3
    ['knife',0],        #4
    ['seedgather',5]    #5
    ]
tool = [
    ['furnace',0],      #0
    ['wood picaxe',1],      #1
    ['stone picaxe',0],     #2
    ['copper picaxe',0],    #3
    ['iron picaxe',0],      #4
    ['wood axe',1],      #5
    ['stone axe',0],     #6
    ['copper axe',0],    #7
    ['iron axe',0],      #8
    ['wood shovel',1],   #9
    ['stone shovel',0],  #10
    ['copper shovel',0], #11
    ['iron shovel',0],   #12
    ['wood hoe',0],      #13
    ['stone hoe',0],     #14
    ['copper hoe',0],    #15
    ['iron hoe',0],      #16
    ['wood knife',0],    #17
    ['stone knife',0],   #18
    ['copper knife',0],  #19
    ['ironknife',0],    #20
    ['campfire',0]      #21
    ]
    
x = 0
exp = 0
req = 10
y = 0

iv = [
    ['wood',0],     #iv[0][1] to change the value 
    ['stone',0],    #1
    ['hay',0],      #2
    ['hay seeds',0], #3
    ['meat',0],     #4
    ['coal',0],     #5
    ['iron ore',0],  #6
    ['iron bar',0],  #7
    ['copper ore',0],#8
    ['copper bar',0],#9
    ['cooked meat',0],#10
    ]

commands = {
    'g ' : 'gather',
    'm ' : 'mine',
    'i ' : 'inventory',
    'a ' : 'abilitys and tool power',
    'e ' : 'exp requiredfor next level',
    's ' : 'smelt',
    'c ' : 'craft ',
    't ' : 'tools',
    'cf': 'cook food',
    }
print("type '?' for help")

while True:
    command = input(">").split()
    if len(command) == 0:
        continue

    if len(command) > 0:
        verb = command[0].lower()
    if len(command) > 1:
        item = command[1].lower()
    if verb == "?":
        for key in commands:
            print(key + " : " + commands[key])
        print("\n")

    
    elif verb == 'g':
        x = randint(0,ab[1][1])
        print('you got',x,'pieces of wood')
        iv[0][1] += x
        x = randint(0,(round(ab[0][1]/2)))
        iv[1][1] += x
        print('you got',x,'pieces of stone')
        x = randint(0,ab[5][1])
        print('you got',x,'hayseeds')
        exp += x
        iv[3][1] += round(x/4)
        while exp > req:
            ab[5][1] += 5
            req += (10*(round(ab[5][1]/5)))
            print('your seedgathering skill is now level',round(ab[5][1]/5),'you can now get up to',ab[5][1],'seeds')
    
    elif verb == 'i':
        print(iv[0][0],'=',iv[0][1])#prints first item in list
        print(iv[1][0],'=',iv[1][1])
        print(iv[2][0],'=',iv[2][1])
        print(iv[3][0],'=',iv[3][1])
        print(iv[4][0],'=',iv[4][1])
        print(iv[5][0],'=',iv[5][1])
        print(iv[8][0],'=',iv[8][1])
        print(iv[9][0],'=',iv[9][1])
        print(iv[6][0],'=',iv[6][1])
        print(iv[7][0],'=',iv[7][1])
        while exp > req:
            ab[5][1] += 5
            req += (10*(round(ab[5][1]/5)))
            print('your seedgathering skill is now level',round(ab[5][1]/5),'you can now get up to',ab[5][1],'seeds')
    elif verb == 'a':
        print(ab[0][0],'=',ab[0][1])#prints first item in list
        print(ab[1][0],'=',ab[1][1])
        print(ab[2][0],'=',ab[2][1])
        print(ab[3][0],'=',ab[3][1])
        print(ab[4][0],'=',ab[4][1])
        print(ab[5][0],'=',ab[5][1])
        while exp > req:
            ab[5][1] += 5
            req += (10*(round(ab[5][1]/5)))
            print('your seedgathering skill is now level',round(ab[5][1]/5),'you can now get up to',ab[5][1],'seeds')
    elif verb == 'test':
        iv[0][1] = 1000
        iv[1][1] = 1000
    elif verb == 'e':
        print('you need',(req-exp),'exp to level up your seed gathering skill')
    elif verb == 'm':
        x = randint(0,ab[0][1])
        iv[1][1] += x
        print('you got',x,'pieces of stone')
        x = randint(0,(ab[0][1]-25))
        iv[5][1] += x
        print('you got',x,'pieces of coal')
        x = randint(0,(round(ab[0][1]-50)))
        iv[8][1] += x
        print('you got',x,'pieces of copper ore')
        y = ab[0][1] - 100
        if y < 0:
            y = 0
        x = randint(0,(round(y)))
        iv[6][1] += x
        print('you got',x,'pieces of iron ore')
    elif verb == 'c':
            if (iv[0][1]>150) and (tool[1][1]==0):
                print('you can craft a wooden pickaxe, craft by typing cwp')
            elif (iv[1][1]>100) and (iv[0][1] >50) and(tool[2][1]==0) and (tool[1][1]==1):       
                print('you can upgrade your wooden pickaxe to a stone pickaxe, craft by typing csp')
            elif (iv[9][1]>100) and (iv[0][1] >50) and(tool[3][1]==0)and (tool[2][1]==1):       
                print('you can upgrade your stone pickaxe to a copper pickaxe, craft by typing ccp')
            elif (iv[7][1]>100) and (iv[0][1] >50) and(tool[4][1]==0)and (tool[3][1]==1):       
                print('you can upgrade your copper pickaxe to a iron pickaxe, craft by typing cip')
            if (iv[0][1]>150) and (tool[5][1]==0):
                print('you can craft a wooden axe, craft by typing cwa')
            elif (iv[1][1]>100) and (iv[0][1] >50) and(tool[6][1]==0) and (tool[5][1]==1):       
                print('you can upgrade your wooden axe to a stone axe, craft by typing csa')
            elif (iv[9][1]>100) and (iv[0][1] >50) and(tool[7][1]==0)and (tool[6][1]==1):       
                print('you can upgrade your stone axe to a copper axe, craft by typing cca')
            elif (iv[7][1]>100) and (iv[0][1] >50) and(tool[8][1]==0)and (tool[7][1]==1):       
                print('you can upgrade your copper axe to a iron axe, craft by typing cia')
            if (iv[0][1]>150) and (tool[9][1]==0):
                print('you can craft a wooden shovel, craft by typing cws')
            elif (iv[1][1]>100) and (iv[0][1] >50) and(tool[10][1]==0)and (tool[9][1]==1):       
                print('you can upgrade your wooden shovel to a stone shovel, craft by typing css')
            elif (iv[9][1]>100) and (iv[0][1] >50) and(tool[11][1]==0)and (tool[10][1]==1):       
                print('you can upgrade your stone shovel to a copper shovel, craft by typing ccs')
            elif (iv[7][1]>100) and (iv[0][1] >50) and(tool[12][1]==0)and (tool[11][1]==1):       
                print('you can upgrade your copper shovel to a iron shovel, craft by typing cis')
            if (iv[0][1]>150) and (tool[13][1]==0):
                print('you can craft a wooden hoe, craft by typing cwh')
            elif (iv[1][1]>100) and (iv[0][1] >50) and(tool[14][1]==0)and (tool[13][1]==1):       
                print('you can upgrade your wooden hoe to a stone hoe, craft by typing csh')
            elif (iv[9][1]>100) and (iv[0][1] >50) and(tool[15][1]==0)and (tool[14][1]==1):       
                print('you can upgrade your stone hoe to a copper hoe, craft by typing cch')
            elif (iv[7][1]>100) and (iv[0][1] >50) and(tool[16][1]==0)and (tool[15][1]==1):       
                print('you can upgrade your copper hoe to a iron hoe, craft by typing cih')
            if (iv[0][1]>150) and (tool[17][1]==0):
                print('you can craft a wooden knife, craft by typing cwk')
            elif (iv[1][1]>100) and (iv[0][1] >50) and(tool[18][1]==0)and (tool[17][1]==1):       
                print('you can upgrade your wooden knife to a stone knife, craft by typing csk')
            elif (iv[9][1]>100) and (iv[0][1] >50) and(tool[19][1]==0)and (tool[18][1]==1):       
                print('you can upgrade your stone knife to a copper knife, craft by typing cck')
            elif (iv[7][1]>100) and (iv[0][1] >50) and(tool[20][1]==0)and (tool[19][1]==1):       
                print('you can upgrade your copper knife to a iron knife, craft by typing cik')
            if (iv[1][1] > 500)and(iv[0][1] > 10) and (tool[0][1] == 0):
                print('you can craft a furnace, craft by typing cf')
            if (iv[0][1] >= 20) and (tool[21][1] == 0):
                print('you can craft a campfire, craft by typing ccf')            
    elif (verb == 'cwp')and(iv[0][1]>150) and (tool[1][1]==0):
        print('you crafted a wooden pickaxe')
        tool[1][1] = 1
        iv[0][1] += -150
        ab[0][1] += 50
    elif (verb == 'csp')and (iv[1][1]>100) and (iv[0][1] >50) and(tool[2][1]==0)and(tool[1][1]==1):
        print('you upgraded your wooden pickaxe to a stone pickaxe')
        tool[2][1] = 1
        iv[0][1] += -50
        iv[1][1] += -100
        ab[0][1] += 50
    elif (verb == 'ccp')and (iv[9][1]>100) and (iv[0][1] >50) and(tool[3][1]==0)and(tool[2][1]==1):
        print('you upgraded your stone pickaxe to a copper pickaxe')
        tool[2][1] = 1
        iv[0][1] += -50
        iv[9][1] += -100
        ab[0][1] += 50
    elif (verb == 'cip')and (iv[7][1]>100) and (iv[0][1] >50) and(tool[4][1]==0)and(tool[3][1]==1):
        print('you upgraded your copper pickaxe to a iron pickaxe')
        tool[2][1] = 1
        iv[0][1] += -50
        iv[7][1] += -100
        ab[0][1] += 50
    elif (verb == 'cwa')and(iv[0][1]>150) and (tool[5][1]==0):
        print('you crafted a wooden axe')
        tool[5][1] = 1
        iv[0][1] += -150
        ab[1][1] += 50
    elif (verb == 'csa')and (iv[1][1]>100) and (iv[0][1] >50) and(tool[6][1]==0)and(tool[5][1]==1):
        print('you upgraded your wooden axe to a stone axe')
        tool[6][1] = 1
        iv[0][1] += -50
        iv[1][1] += -100
        ab[1][1] += 50
    elif (verb == 'cca')and (iv[9][1]>100) and (iv[0][1] >50) and(tool[7][1]==0)and(tool[6][1]==1):
        print('you upgraded your stone axe to a copper axe')
        tool[7][1] = 1
        iv[0][1] += -50
        iv[9][1] += -100
        ab[1][1] += 50
    elif (verb == 'cia')and (iv[7][1]>100) and (iv[0][1] >50) and(tool[8][1]==0)and(tool[7][1]==1):
        print('you upgraded your copper axe to a iron axe')
        tool[8][1] = 1
        iv[0][1] += -50
        iv[7][1] += -100
        ab[1][1] += 50
    elif (verb == 'cws')and(iv[0][1]>150) and (tool[9][1]==0):
        print('you crafted a wooden shovel')
        tool[9][1] = 1
        iv[0][1] += -150
        ab[2][1] += 50
    elif (verb == 'css')and (iv[1][1]>100) and (iv[0][1] >50) and(tool[10][1]==0)and(tool[9][1]==1):
        print('you upgraded your wooden shovel to a stone shovel')
        tool[10][1] = 1
        iv[0][1] += -50
        iv[1][1] += -100
        ab[2][1] += 50
    elif (verb == 'ccs')and (iv[9][1]>100) and (iv[0][1] >50) and(tool[11][1]==0)and(tool[10][1]==1):
        print('you upgraded your stone shovel to a copper shovel')
        tool[11][1] = 1
        iv[0][1] += -50
        iv[9][1] += -100
        ab[2][1] += 50
    elif (verb == 'cis')and (iv[7][1]>100) and (iv[0][1] >50) and(tool[12][1]==0)and(tool[11][1]==1):
        print('you upgraded your copper shovel to a iron shovel')
        tool[12][1] = 1
        iv[0][1] += -50
        iv[7][1] += -100
        ab[2][1] += 50
    elif (verb == 'cwh')and(iv[0][1]>150) and (tool[13][1]==0):
        print('you crafted a wooden hoe')
        tool[13][1] = 1
        iv[0][1] += -150
        ab[2][1] += 50
    elif (verb == 'csh')and (iv[1][1]>100) and (iv[0][1] >50) and(tool[14][1]==0)and(tool[13][1]==1):
        print('you upgraded your wooden hoe to a stone hoe')
        tool[14][1] = 1
        iv[0][1] += -50
        iv[1][1] += -100
        ab[2][1] += 50
    elif (verb == 'cch')and (iv[9][1]>100) and (iv[0][1] >50) and(tool[15][1]==0)and(tool[14][1]==1):
        print('you upgraded your stone hoe to a copper hoe')
        tool[15][1] = 1
        iv[0][1] += -50
        iv[9][1] += -100
        ab[2][1] += 50
    elif (verb == 'cih')and (iv[7][1]>100) and (iv[0][1] >50) and(tool[16][1]==0)and(tool[15][1]==1):
        print('you upgraded your copper hoe to a iron hoe')
        tool[16][1] = 1
        iv[0][1] += -50
        iv[7][1] += -100
        ab[2][1] += 50
    elif (verb == 'cwk')and(iv[0][1]>150) and (tool[17][1]==0):
        print('you crafted a wooden knife')
        tool[17][1] = 1
        iv[0][1] += -150
        ab[2][1] += 50
    elif (verb == 'csk')and (iv[1][1]>100) and (iv[0][1] >50) and(tool[18][1]==0)and(tool[17][1]==1):
        print('you upgraded your wooden knife to a stone knife')
        tool[18][1] = 1
        iv[0][1] += -50
        iv[1][1] += -100
        ab[2][1] += 50
    elif (verb == 'cck')and (iv[9][1]>100) and (iv[0][1] >50) and(tool[19][1]==0)and(tool[18][1]==1):
        print('you upgraded your stone knife to a copper knife')
        tool[19][1] = 1
        iv[0][1] += -50
        iv[9][1] += -100
        ab[2][1] += 50
    elif (verb == 'cik')and (iv[7][1]>100) and (iv[0][1] >50) and(tool[20][1]==0)and(tool[19][1]==1):
        print('you upgraded your copper knife to a iron knife')
        tool[20][1] = 1
        iv[0][1] += -50
        iv[7][1] += -100
        ab[2][1] += 50
    elif (verb =='cf') and (iv[1][1]>500) and (iv[0][1] > 10) and (tool[0][1]==0):
        tool[0][1] = 1
        print('you crafted a furnace')
    elif (verb == 'ccf') and (tool[21][1] == 0)and (iv[0][1] >= 20):
        print('you crafted a campfire')
        tool[21][1] = 1
    elif (verb == 's') and (tool[0][1] == 1):
        if (iv[8][1]>= 5)and (iv[5][1] >=1):
            print('you can smelt your copperore into bars, smelt by typing cb')
        if (iv[6][1]>= 5)and (iv[5][1] >=2):
            print('you can smelt your ironore into bars, smelt by typing ib')
    elif (verb == 'cb')and(iv[8][1]>= 5)and (iv[5][1] >=1):
        time.sleep(0.33)
        print('.')
        time.sleep(0.33)
        print('..')
        time.sleep(0.33)
        print('...')
        print('you crafted a copper bar')
        iv[9][1]+=1
        iv[8][1]+=-5
        iv[5][1]+=-1
    elif (verb == 'ib')and(iv[6][1]>= 5)and (iv[5][1] >=2):
        time.sleep(0.33)
        print('.')
        time.sleep(0.33)
        print('..')
        time.sleep(0.33)
        print('...')
        time.sleep(0.33)
        print('.')
        time.sleep(0.33)
        print('..')
        time.sleep(0.33)
        print('...')
        print('you crafted a iron bar')
        iv[7][1]+=1
        iv[6][1]+=-5
        iv[5][1]+=-2
    elif verb == 'cf' and tool[21][1] == 1:
        time.sleep(0.33)
        print('.')
        time.sleep(0.33)
        print('..')
        time.sleep(0.33)
        print('...')
        print ('you cooked',iv[4][1],"piece's of meat")
        iv[10][1]+=iv[4][1]
        iv[4][1] = 0

