from tkinter import *
import random
import time

class gra:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Pan Patyczak pędzi do wyjścia")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.płotno =  Canvas(self.tk, width=500, height=500, highlightthickness=0)
        self.płotno.pack()
        self.tk.update()
        self.wysokość_płotna = 500
        self.szerokość_płotna = 500
        self.tło = PhotoImage(file="tło.gif")
        self.tło2 = PhotoImage(file="tło2.gif")
        self.tło3 = PhotoImage(file="tło_stół_z_lampą.gif")
        self.tło4 = PhotoImage(file="tło_półka_z_książkami.gif")
        self.tło5 = PhotoImage(file="tło_okno.gif")
        self.sze = self.tło.width()
        self.wys = self.tło.height()
        rysować_tło = False
        numer_tła = 0
        for x in range(0,5):
            for y in range(0,5):
                if rysować_tło == True:   
                    self.płotno.create_image(x * self.sze, y * self.wys, image=self.tło, anchor='nw')
                    rysować_tło = False
                else:
                    if numer_tła <= 3:
                        self.płotno.create_image(x * self.sze, y * self.wys, image=self.tło2, anchor='nw')
                        rysować_tło = True
                        numer_tła += 1
                    elif numer_tła <= 7:
                        self.płotno.create_image(x * self.sze, y * self.wys, image=self.tło5, anchor='nw')
                        numer_tła += 1
                    elif numer_tła <= 10:
                        self.płotno.create_image(x * self.sze, y * self.wys, image=self.tło4, anchor='nw')
                        numer_tła += 1
                    elif numer_tła <= 13:
                        self.płotno.create_image(x * self.sze, y * self.wys, image=self.tło3, anchor='nw')
                        rysować_tło = True
                    else: 
                        numer_tła = 0        
        self.duszki = []
        self.biegnie = True

    def pętla_główna(self):
        while 1:
            if self.biegnie == True:
                for duszek in self.duszki:
                    duszek.move()
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01)

class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def na_osi_x(wsp1, wsp2):
    if (wsp1.x1 > wsp2.x1 and wsp1.x1 < wsp2.x2) \
            or (wsp1.x2 > wsp2.x1 and wsp1.x2 < wsp2.x2) \
            or (wsp2.x1 > wsp1.x1 and wsp2.x1 < wsp1.x2) \
            or (wsp2.x2 > wsp1.x1 and wsp2.x2 < wsp1.x2):
        return True
    else:
        return False

def na_osi_y(wsp1, wsp2):
    if (wsp1.y1 > wsp2.y1 and wsp1.y1 < wsp2.y2) \
            or (wsp1.y2 > wsp2.y1 and wsp1.y2 < wsp2.y2) \
            or (wsp2.y1 > wsp1.y1 and wsp2.y1 < wsp1.y2) \
            or (wsp2.y2 > wsp1.y1 and wsp2.y2 < wsp1.y2):
        return True
    else:
        return False

def kolizja_lewa(wsp1, wsp2):
    if na_osi_y(wsp1, wsp2):
        if wsp1.x1 <= wsp2.x2 and wsp1.x1 >= wsp2.x1:
            return True
    return False

def kolizja_prawa(wsp1, wsp2):
    if na_osi_y(wsp1, wsp2):
        if wsp1.x2 >= wsp2.x1 and wsp1.x2 <= wsp2.x2:
            return True
    return False

def kolizja_góra(wsp1, wsp2):
    if na_osi_x(wsp1, wsp2):
        if wsp1.y1 <= wsp2.y2 and wsp1.y1 >= wsp2.y1:
            return True
    return False

def kolizja_dól(y, wsp1, wsp2):
    if na_osi_x(wsp1, wsp2):
        oblicz_y = wsp1 + y
        if oblicz_y >= wsp2.y1 and oblicz_y <= wsp2.y2:
            return True
    return False

class Duszek:
    def __init__(self, gra):
        self.gra = gra
        self.koniecGry = False
        self.współrzędne = None
    def move(self):
        pass
    def coords(self):
        return self.współrzędne

class DuszekPlatforma(Duszek):
    def __init__(self, gra, obrazek, x, y, szerokość, wysokość):
        Duszek.__init__(self, gra)
        self.obrazek = obrazek
        self.image = gra.płotno.create_image(x, y, image=self.obrazek, anchor='nw')
        self.współrzędne = Coords(x, y, x + szerokość, y + wysokość)

g = gra()
platforma1 = DuszekPlatforma(g, PhotoImage(file="platforma1.gif"), 0, 480, 100, 10)
platforma2 = DuszekPlatforma(g, PhotoImage(file="platforma1.gif"), 150, 440, 100, 10)
platforma3 = DuszekPlatforma(g, PhotoImage(file="platforma1.gif"), 300, 400, 100, 10)
platforma4 = DuszekPlatforma(g, PhotoImage(file="platforma1.gif"), 300, 160, 100, 10)
platforma5 = DuszekPlatforma(g, PhotoImage(file="platforma2.gif"), 175, 350, 66, 10)
platforma6 = DuszekPlatforma(g, PhotoImage(file="platforma2.gif"), 50, 300, 66, 10)
platforma7 = DuszekPlatforma(g, PhotoImage(file="platforma2.gif"), 170, 120, 66, 10)
platforma8 = DuszekPlatforma(g, PhotoImage(file="platforma2.gif"), 45, 60, 66, 10)
platforma9 = DuszekPlatforma(g, PhotoImage(file="platforma3.gif"), 170, 250, 32, 10)
platforma10 = DuszekPlatforma(g, PhotoImage(file="platforma3.gif"), 230, 200, 32, 10)
g.duszki.append(platforma1)
g.duszki.append(platforma2)
g.duszki.append(platforma3)
g.duszki.append(platforma4)
g.duszki.append(platforma5)
g.duszki.append(platforma6)
g.duszki.append(platforma7)
g.duszki.append(platforma8)
g.duszki.append(platforma9)
g.duszki.append(platforma10)
g.pętla_główna()