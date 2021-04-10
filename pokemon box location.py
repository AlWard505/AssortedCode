import math
while True:
    pokid = int(input('enter id of pokémon: '))
    y=1
    box = 1.1
    box = pokid / 30
    box = math.ceil(box)
    print ('box',box)
    place= pokid-(math.ceil(pokid/30)*30)+30
    x = place
    while x > 6:
        x += -6
        y+=1
    print (x,y)
    
