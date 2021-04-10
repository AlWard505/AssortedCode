f = open('test.txt','r')
f.readline(1)
q = 0
print (f.readline())
l = input('what are you looking for: ')
x= '$'+ l + ' '
c=0
z= len(x)
y = ('s')
for line in f:
     y = f.readline(z)
     if y == x:
          f.readline()
          f.readline(1)
          o =(f.readline())
          c = 1
          q = q+1
if q != 0:
if c == 0:
     print(l, "wasn't found")

     
