file = open('stardewinfo.txt', 'a+')
endkey = 0
check = ' '
while endkey != 1:#vilager list goes from 0 to 32
    vilager = ['Abigail','Alex','Caroline','Clint','Demetrius','Dwarf','Elliott','Emily','Evelyn','George','Gus','Haley','Harvey','Jas','Jodi','Kent','Krobus','Leah','Lewis','Linus','Marnie','Maru','Pam','Penny','Pierre','Robin','Sam','Sandy','Sebastian','Shane','Vincent','Willy','Wizard']
    vcheck = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    crop = input('what crop are you entering: ')
    content = open('stardewcontent.txt','a+')
    content.write(', '+crop)
    content.close
    cropkey = '$'+crop.lower()+'$'
    file.write(cropkey+'\n')
    seed = input('how much do seeds cost: ')
    file.write(' Seeds cost '+seed+'g\n')
    growth = input('how many days does it take to grow: ')
    file.write('\ Takes '+growth+' days to grow\n')
    month = input('what season is it grown in: ')
    file.write('\ Grows in '+month+'\n')
    file.write('\ Sells for;\n')
    base = input('what is base price: ')
    silver = input('what is silver price: ')
    gold= input('what is gold price: ')
    file.write('\ [Base '+base+'g][Silver '+silver+'g][Gold '+gold+'g]\n')
    file.write('\ With Tiller Profession(+10% sell price);\n')
    base = input('what is base price with Tiller Profession: ')
    silver = input('what is silver price with Tiller Profession: ')
    gold= input('what is gold price with Tiller Profession: ')
    file.write('\ [Base '+base+'g][Silver '+silver+'g][Gold '+gold+'g]\n')
    gpd = input('what is gold per day: ')
    file.write('\ Gold per day is '+gpd+"g assuming they're all base quality\n")
    vof = input('is '+crop+' a veg(v) or a fruit(f) or neither(any other key): ')
    if vof == 'v':
        file.write('\ Artisan version;\n')
        juice = input('what is Juice price: ')
        pickle = input('what is Pickle price: ')
        file.write('\ [Juice '+juice+'g][Pickled '+pickle+'g]\n')
        file.write('\ With Artisan Profession(+40% sell price);\n')
        juice = input('what is Juice price with Artisan Profession: ')
        pickle = input('what is Pickle price with Artisan Profession: ')
        file.write('\ [Juice '+juice+'g][Pickled '+pickle+'g]\n')
    elif vof == 'f':
        file.write('\ Artisan version;\n')
        wine = input('what is Wine price: ')
        swine = input('what is silver Wine price: ')
        gwine = input('what is gold Wine price: ')
        iwine = input('what is iridium Wine price: ')
        jelly = input('what is jelly price')
        file.write('\ [Base wine '+wine+'g][Silver wine '+swine+'g][Gold wine '+gwine+'g][Iridium wine '+iwine+'g][jelly '+jelly+'g]\n')
        file.write('\ With Artisan Profession(+40% sell price);\n')
        wine = input('what is Wine price with Artisan Profession: ')
        swine = input('what is silver Wine price with Artisan Profession: ')
        gwine = input('what is gold Wine price with Artisan Profession: ')
        iwine = input('what is iridium Wine price with Artisan Profession: ')
        jelly = input('what is jelly price with Artisan Profession')
        file.write('\ [Base wine '+wine+'g][Silver wine '+swine+'g][Gold wine '+gwine+'g][Iridium wine '+iwine+'g][jelly '+jelly+'g]\n')
    file.write('\ '+crop+' is loved by ')
    while check != 'done':
        check = input('who loves '+crop+': ')
        if check != 'done':
            if vcheck[int(check)] != 1:
                vcheck[int(check)] = int(1)
                file.write(vilager[int(check)]+', ')
    check = ' '
    file.write('\n')
    file.write('\ '+crop+' is liked by ')
    while check != 'done':
        check = input('who likes '+crop+': ')
        if check != 'done':
            if vcheck[int(check)] != 1:
                vcheck[int(check)] = int(1)
                file.write(vilager[int(check)]+', ')
    check = ' '
    file.write('\n')
    file.write('\ '+crop+' is neutrally accepted by ')
    while check != 'done':
        check = input('who is neutral towards '+crop+': ')
        if check != 'done':
            if vcheck[int(check)] != 1:
                vcheck[int(check)] = int(1)
                file.write(vilager[int(check)]+', ')
    check = ' '
    file.write('\n')
    file.write('\ '+crop+' is disliked by ')
    while check != 'done':
        check = input('who dislikes '+crop+': ')
        if check != 'done':
            if vcheck[int(check)] != 1:
                vcheck[int(check)] = int(1)
                file.write(vilager[int(check)]+', ')
    check = ' '
    file.write('\n')
    file.write('\ '+crop+' is hated by ')
    while check != 'done':
        check = input('who hates '+crop+': ')
        if check != 'done':
            if vcheck[int(check)] != 1:
                vcheck[int(check)] = int(1)
                file.write(vilager[int(check)]+', ')
    check = ' '
    file.write('\n')
    x = input('how many recipies is '+crop+'used for: ')
    x = int(x)
    z = 0
    while z != x:
        z += 1
        if z == x:
            file.write('/ ')
        else:
            file.write('\ ')
        dish = input('dish '+str(z)+': \n')
        file.write(crop+' is used when making '+dish+'\n')
    endcheck = input('to end the program enter [end]: ')
    if endcheck == 'end':
        endkey = 1
    
    
