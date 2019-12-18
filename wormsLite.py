from tkinter import *
from bazooka import *
from roquette import *

def create_roquette1():
    global roquette1
    roquette1=Roquette(can,b1.x2,b1.y2,'red')

def destroy_roquette1():
    roquette1.destroy()


# Code pour tester sommairement la classe Bazouka :
f = Tk()
can = Canvas(f,width =500, height =250, bg ='ivory')
can.pack(padx =10, pady =10)
b1 = Bazooka(can, 50, 200)
b2 = Bazooka(can, 250, 200)

s1 =Scale(f, label='hausse', from_=90, to=0, command=b1.orienter)
s1.pack(side=LEFT, pady =5, padx =20)
s1.set(25)                          # angle de tir initial

s2 =Scale(f, label='hausse', from_=90, to=0, command=b2.orienter)
s2.pack(side=LEFT, pady =5, padx =20)
s2.set(25)

roquette1= Roquette(can,125,150,'red')


btn_tir1 = Button(f,text="tire",command=create_roquette1)
btn_supr1 = Button(f,text="suprimer",command=destroy_roquette1)

btn_tir1.pack(side=LEFT,pady =14,padx =20)
btn_supr1.pack(side=RIGHT,pady =14,padx =20)

f.mainloop()
