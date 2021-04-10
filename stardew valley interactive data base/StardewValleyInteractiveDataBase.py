#stardew valley interactive data base
#variables
endkey = 0 #if it equals one program stops
searchkey = ' '

keylength = ' '
thing = ' '
check = 0 #if = 1 it means item has been found
search = ' '
rowcheck = '\ '
file = open('stardewcontent.txt','r')# opens file with data
file.readline(1)# stops the presign such as $ or £ from being printed
print ('Contents:'+file.readline())# should read contents
file.close()
while endkey != 1:#program will loop
    check = 0
    file = open('stardewinfo.txt','r')
    thing = input('what do you need information on: ')#input is looked up by program
    searchkey = '$' + thing.lower() + '$'
    keylength = len(searchkey)
    for line in file:
        search = file.readline(keylength)
        if search == searchkey:
            check = 1
            while rowcheck != "/":
                rowcheck= file.readline(1)
                print(file.readline())
    if check == 0:
        print(thing+' was not found')
    search = ' '
    rowcheck = ' '
    file.close()
    endcheck = input(' if you want the program to end type [end]: ')
    if endcheck == 'end':
        endkey = 1
    
        
                
                
                
                
                
                
