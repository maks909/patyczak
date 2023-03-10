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
        oblicz_y = wsp1.y2 + y
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

class DuszekPatyczak(Duszek):
    def __init__(self, gra):
        Duszek.__init__(self, gra)
        self.obrazki_lewa = [
            PhotoImage(file="patyczak-L1.gif"),
            PhotoImage(file="patyczak-L2.gif"),
            PhotoImage(file="patyczak-L3.gif")
        ]
        self.obrazki_prawa = [
            PhotoImage(file="patyczak-P1.gif"),
            PhotoImage(file="patyczak-P2.gif"),
            PhotoImage(file="patyczak-P3.gif")
        ]
        self.image = gra.płotno.create_image(50, 440, image=self.obrazki_lewa[0], anchor='nw')
        self.x = -2
        self.y = 0
        self.bieżący_obrazek = 0
        self.bieżący_obrazek_dodaj = 1
        self.licznik_skoków = 0
        self.ostatni_czas = time.time()
        self.współrzędne = Coords()
        gra.płotno.bind_all('<KeyPress-Left>', self.obrót_w_lewo)
        gra.płotno.bind_all('<KeyPress-Right>', self.obrót_w_prawo)
        gra.płotno.bind_all('<space>', self.skok)

    def obrót_w_lewo(self, zdarzenie):
        if self.y == 0:
            self.x = -2
    
    def obrót_w_prawo(self, zdarzenie):
        if self.y == 0:
            self.x = 2
    
    def skok(self, zdarzenie):
        if self.y == 0:
            self.y = -4
            self.licznik_skoków = 0

    def animuj(self):
        if self.x != 0 and self.y == 0:
            if time.time() - self.ostatni_czas > 0.1:
                self.ostatni_czas = time.time()
                self.bieżący_obrazek += self.bieżący_obrazek_dodaj
                if self.bieżący_obrazek >= 2:
                    self.bieżący_obrazek_dodaj = -1
                if self.bieżący_obrazek <= 0:
                    self.bieżący_obrazek_dodaj = 1
        if self.x < 0:
            if self.y != 0:
                self.gra.płotno.itemconfig(self.image, image=self.obrazki_lewa[2])
            else:
                self.gra.płotno.itemconfig(self.image, image=self.obrazki_lewa[self.bieżący_obrazek])
        if self.x > 0:
            if self.y != 0:
                self.gra.płotno.itemconfig(self.image, image=self.obrazki_prawa[2])
            else:
                self.gra.płotno.itemconfig(self.image, image=self.obrazki_prawa[self.bieżący_obrazek])    

    def coords(self):
        xy = self.gra.płotno.coords(self.image)
        self.współrzędne.x1 = xy[0]
        self.współrzędne.y1 = xy[1]
        self.współrzędne.x2 = xy[0] + 27
        self.współrzędne.y2 = xy[1] + 30
        return self.współrzędne 

    def move(self):
        self.animuj() 
        if self.y < 0:
            self.licznik_skoków += 1
            if self.licznik_skoków > 20:
                self.y = 4
        if self.y > 0:
            self.licznik_skoków -= 1
        wsp = self.coords()
        lewa = True
        prawa = True
        góra = True
        dół = True
        spadanie = True
        if self.y > 0 and wsp.y2 >= self.gra.wysokość_płotna:
            self.y = 0
            dół = False
        elif self.y < 0 and wsp.y1 <= 0:
            self.y = 0
            góra = False
        if self.x > 0 and wsp.x2 >= self.gra.szerokość_płotna:
            self.x = 0
            prawa = False
        elif self.x < 0 and wsp.x1 <= 0:
            self.x = 0 
            lewa = False
        for duszek in self.gra.duszki:
            if duszek == self:
                continue
            duszek_wsp = duszek.coords()
            if góra and self.y < 0 and kolizja_góra(wsp, duszek_wsp):
                self.y = -self.y
                góra = False
            if dół and self.y > 0 and kolizja_dól(self.y, wsp, duszek_wsp):
                self.y = duszek_wsp.y1 - wsp.y2
                if self.y < 0:
                    self.y = 0
                dół = False
                góra = False
            if (dół) and (spadanie) and (self.y == 0) \
                    and (wsp.y2 < self.gra.wysokość_płotna) \
                    and (kolizja_dól(1, wsp, duszek_wsp)):
                spadanie = False
            if lewa and self.x < 0 and kolizja_lewa(wsp, duszek_wsp):
                self.x = 0
                lewa = False
            if prawa and self.x > 0 and kolizja_prawa(wsp, duszek_wsp):
                self.x = 0
                prawa = False
        if spadanie and dół and self.y == 0 and wsp.y2 < self.gra.wysokość_płotna:
            self.y = 4
        self.gra.płotno.move(self.image, self.x, self.y)

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
sf = DuszekPatyczak(g)
g.duszki.append(sf)
g.pętla_główna()