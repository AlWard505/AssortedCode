inputs = [1,1,2.5,2.5,5,5]
x = 0
t =[]

while x != 63:
    comb = []
    p=-1
    no = 0
    weight = 0
    x+=1
    r = 0
    y = bin(x)
    y = y.replace("0b","")
    length = len(y)
    while length != 6:
        y ="0"+y
        length = len(y)
    
    while p != 5:
        p+=1
        
        if y[p] == '1':
            
            weight += inputs[p]
            comb.append(inputs[p])
    i = len(t)
    while r != i:
        r+=1
        n = r-1
        if weight == t[n]:
            no = 1
    if no != 1:
        t.append(weight)
        

o = len(t)
u = 0
while u != o:
    u+=1
    if t[u-1] == str:
        t[u-1] = t[u-1].strip()

t.sort()

print(t)



