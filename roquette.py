from tkinter import *
from math import pi, sin, cos

class Roquette(object):
    def __init__(self,parent,x,y,coul):
        self.parent = parent
        self.x=x
        self.y=y
        self.r=self.parent.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,fill=coul)


    def tir(self,angle,power):
        self.t=0
        self.x=cos(angle*pi/180)*power*self.t
        self.y=-1/2*9.81*pow(t,2)+sin(angle*pi/180)*power*self.t
        self.parent.move
        print("entre x et y")

    def destroy(self):
        self.parent.delete(self.r)
        
