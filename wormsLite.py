from tkinter import *
from bazooka import *
from roquette import *

class Worms(Frame):


    def create_roquette1(self):
        self.roquette1
        self.roquette1=Roquette(self.can,self.b1.x2,self.b1.y2,'red')

    def destroy_roquette1(self):
        self.roquette1.destroy()

    def __init__(self):

        # Code pour tester sommairement la classe Bazouka :
        f = Tk()
        self.can = Canvas(f,width =500, height =250, bg ='ivory')
        self.can.pack(padx =10, pady =10)
        self.b1 = Bazooka(self.can, 50, 200)
        self.b2 = Bazooka(self.can, 250, 200)

        s1 =Scale(f, label='hausse', from_=90, to=0, command=self.b1.orienter)
        s1.pack(side=LEFT, pady =5, padx =20)
        s1.set(25)                          # angle de tir initial

        s2 =Scale(f, label='hausse', from_=90, to=0, command=self.b2.orienter)
        s2.pack(side=LEFT, pady =5, padx =20)
        s2.set(25)

        self.roquette1= Roquette(self.can,125,150,'red')


        btn_tir1 = Button(f,text="tire",command=self.create_roquette1)
        btn_tir1.pack(side=LEFT,pady =14,padx =20)

        btn_tir2 = Button(f,text="tire",command=self.create_roquette1)
        btn_tir2.pack(side=RIGHT,pady =14,padx =20)

        btn_supr = Button(f,text="suprimer",command=self.destroy_roquette1)
        btn_supr.pack(side=BOTTOM,pady =14,padx =20)

        f.mainloop()


monJeux=Worms()
