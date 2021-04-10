import time
from tkinter import *





def a(): lab.configure(print("a"))




def b(): lab.configure(print("b"))




def c(): lab.configure(print("c"))




def d(): lab.configure(print("d"))




def e(): lab.configure(print("e"))




def f(): lab.configure(print("f"))




def g(): lab.configure(print("g"))




def h(): lab.configure(print("h"))




def i(): lab.configure(print("i"))




def j(): lab.configure(print("j"))




def k(): lab.configure(print("k"))




def l(): lab.configure(print("l"))




def m(): lab.configure(print("m"))




def n(): lab.configure(print("n"))




def o(): lab.configure(print("o"))




def p(): lab.configure(print("p"))




def q(): lab.configure(print("q"))




def r(): lab.configure(print("r"))




def s(): lab.configure(print("s"))




def t(): lab.configure(print("t"))




def u(): lab.configure(print("u"))




def v(): lab.configure(print("v"))




def w(): lab.configure(print("w"))




def x(): lab.configure(print("x"))




def y(): lab.configure(print("y"))




def z(): lab.configure(print("z"))




def space(): lab.configure(print(" "))
def QU(): lab.configure(print("? "))

def END(): lab.configure(print(". "))

root = Tk()




lab = Label(root, text="keyboard")





lab.grid(row=0, column=5)





but = Button(root, text="a", command=a)
but.grid(row=1, column=1)
but = Button(root, text="b", command=b)
but.grid(row=1, column=2)
but = Button(root, text="c", command=c)
but.grid(row=1, column=3)
but = Button(root, text="d", command=d)
but.grid(row=1, column=4)
but = Button(root, text="e", command=e)
but.grid(row=1, column=5)
but = Button(root, text="f", command=f)
but.grid(row=1, column=6)
but = Button(root, text="g", command=g)
but.grid(row=1, column=7)
but = Button(root, text="h", command=h)
but.grid(row=1, column=8)
but = Button(root, text="i", command=i)
but.grid(row=1, column=9)
but = Button(root, text="j", command=j)
but.grid(row=1, column=10)
but = Button(root, text="k", command=k)
but.grid(row=2, column=1)
but = Button(root, text="l", command=l)
but.grid(row=2, column=2)
but = Button(root, text="m", command=m)
but.grid(row=2, column=3)
but = Button(root, text="n", command=n)
but.grid(row=2, column=4)
but = Button(root, text="o", command=o)
but.grid(row=2, column=5)
but = Button(root, text="p", command=p)
but.grid(row=2, column=6)
but = Button(root, text="q", command=q)
but.grid(row=2, column=7)
but = Button(root, text="r", command=r)
but.grid(row=2, column=8)
but = Button(root, text="s", command=s)
but.grid(row=2, column=9)
but = Button(root, text="t", command=t)
but.grid(row=3, column=1)
but = Button(root, text="u", command=u)
but.grid(row=3, column=2)
but = Button(root, text="v", command=v)
but.grid(row=3, column=3)
but = Button(root, text="w", command=w)
but.grid(row=3, column=4)
but = Button(root, text="x", command=x)
but.grid(row=3, column=5)
but = Button(root, text="y", command=y)
but.grid(row=3, column=6)
but = Button(root, text="z", command=z)
but.grid(row=3, column=7)
but = Button(root, text="space", command=space)
but.grid(row=4, column=5)
but = Button(root, text="?", command=QU)
but.grid(row=4, column=6)

but = Button(root, text=".", command=END)
but.grid(row=4, column=4)


root.mainloop()
