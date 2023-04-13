# -*- coding: utf-8 -*- 
from tkinter import *
from PIL import ImageTk,Image


class Piskvorky:
    
    def __init__(self):
        return
    
    def menu(self):
        self.okno = Tk()
        self.okno.geometry("700x700")
        
        filename = PhotoImage(file ="pozadi.png")
        background_label = Label(self.okno, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.okno.title("Piškvorky")
        self.pocet = 0
        self.start = Button(self.okno, text="Hrát", command= lambda: [self.okno.destroy(),uga.hra_menu()], font=("Arial", 35))
        self.napoveda = Button(self.okno, text="Nápověda", command= uga.nanapoveda, font=("Arial", 35))
        self.konec = Button(self.okno, text="Konec", command=self.okno.destroy, font=("Arial", 35))
        
        self.menulista = Menu(self.okno, tearoff = 0)
        self.menulista.add_command(label="Nápověda", command=uga.menapoveda)
        self.menulista.add_command(label="O aplikaci", command=uga.oaplikaci)
        self.okno.config(menu=self.menulista)
        
        self.start.place(x=280, y=100)
        self.napoveda.place(x=220, y=270)
        self.konec.place(x=260, y=450)
        
        
        self.okno.mainloop()
        
    def moznost1(self):
        self.cislo_moznost = 1
        
    def moznost2(self):
        self.cislo_moznost = 2
        
    def moznost3(self):
        self.cislo_moznost = 3
        
        
    def hra_menu(self):
        self.okenko = Tk()
        self.okenko.geometry("700x700")
        self.okenko.title("Piškvorky")
        
        bg = PhotoImage(file="pozadi.png")
        my_label = Label(self.okenko, image=bg)
        
        self.hra_hrac = Button(self.okenko, text="Hrát ve 2", command= lambda: [uga.hra(),self.okenko.destroy(), uga.moznost1()], font=("Arial", 50))
        self.hra_ca = Button(self.okenko, text="Hrát na čas", command= lambda: [uga.hra_cas(),self.okenko.destroy(), uga.moznost2()], font=("Arial", 50))

        
        self.otaznik1 = Button(self.okenko, text="?", command=uga.napodva, font=("Arial", 50))
        self.otaznik2 = Button(self.okenko, text="?", command=uga.napocas, font=("Arial", 50))
        
        my_label.place(x=0,y=0,relwidth=1,relheight=1)
        
        self.hra_hrac.place(x=160, y=170)
        self.hra_ca.place(x=130, y=400)
        
        self.otaznik1.place(x=498, y=170)
        self.otaznik2.place(x=540, y=400)
        
        self.okenko.mainloop()
    
    def napodva(self):
        messagebox.showinfo("Hrát ve 2","V tomto modu proti sobě hrají 2 hráči")
    def napocas(self):
        messagebox.showinfo("Hrát ve 2 s časem","V tomto modu proti sobě hrají 2 hráči, ale čas na 1 kolo zahrání je 5 sekund")
        
    
    def hra_cas(self):
        self.sekundy = 5
        self.plocha = Tk()
        self.plocha.geometry("1400x930")
        self.plocha.title("Piškvorky")
        x = 16
        y = 16
        self.metrix_list = [[0 for i in range(y)] for j in range(x)]
        radky = 16
        sloupce = 16
        self.grid = []
        self.grid = [[Button(self.plocha, text = "", command = lambda a=i, b=j: uga.show_cas(a, b), width = 3, height = 1, font=("Arial", 20)) for j in range(sloupce)] for i in range(radky)]
        [[self.grid[i][j].grid(row = i, column = j) for j in range(sloupce)] for i in range(radky)]
        self.vypln = Label(self.plocha, text="       ")
        self.vypln.grid(row= 1,column=17)
        self.hrac = Label(self.plocha, text="Hráč č.1 je na řadě", font=("Arial",35))
        self.cas = Label(self.plocha, text=self.sekundy, font=("Arial",35))
        self.cas.after(1000, uga.hra_cas_update)
        self.cas.grid(row=4,column=18)
        self.hrac.grid(row =2, column=18)
        
        
    def hra_cas_update(self):
        self.cas.config(text=self.sekundy)
        self.sekundy = self.sekundy - 1
        self.cas.config(text=self.sekundy)
        if self.sekundy == 0:
            if self.pocet % 2 == 0:
                self.vysledek = 2
                uga.vyhra()
                
            elif self.pocet % 2 ==1:
                self.vysledek = 1
                uga.vyhra()
        self.cas.after(1000, uga.hra_cas_update)
                
    
    def hra(self):
        self.plocha = Tk()
        self.plocha.geometry("1400x930")
        self.plocha.title("Piškvorky")
        x = 16
        y = 16
        self.metrix_list = [[0 for i in range(y)] for j in range(x)]
        radky = 16
        sloupce = 16
        self.grid = []
        self.grid = [[Button(self.plocha, text = "", command = lambda a=i, b=j: uga.show(a, b), width = 3, height = 1, font=("Arial", 20)) for j in range(sloupce)] for i in range(radky)]
        [[self.grid[i][j].grid(row = i, column = j) for j in range(sloupce)] for i in range(radky)]
        self.vypln = Label(self.plocha, text="       ")
        self.vypln.grid(row= 1,column=17)
        self.hrac = Label(self.plocha, text="Hráč č.1 je na řadě", font=("Arial",35))
        self.hrac.grid(row =2, column=18)
    
    def show(self, i, j):
        self.pocet += 1
        if (self.pocet % 2 == 0):
            self.metrix_list[i][j] = 2
            self.grid[i][j].config(text ="X", state = DISABLED, bg="red", fg="black")
            self.hrac.config(text="Hráč č.1 je na řadě", bg="blue")
            
        else:
            self.metrix_list[i][j] = 1
            self.grid[i][j].config(text ="O", state = DISABLED, bg="blue", fg="black")
            self.hrac.config(text="Hráč č.2 je na řadě", bg="red")
        
        uga.kontrola()
        
    def show_cas(self, i, j):
        self.pocet += 1
        if (self.pocet % 2 == 0):
            self.metrix_list[i][j] = 2
            self.grid[i][j].config(text ="X", state = DISABLED, bg="red", fg="black")
            self.hrac.config(text="Hráč č.1 je na řadě", bg="blue")
            
        else:
            self.metrix_list[i][j] = 1
            self.grid[i][j].config(text ="O", state = DISABLED, bg="blue", fg="black")
            self.hrac.config(text="Hráč č.2 je na řadě", bg="red")
        self.sekundy = 6
        
        uga.kontrola()
    
    def kontrola(self):
        for i in range(16):
            for j in range(12):
                if ((self.metrix_list[i][j] == 1) or (self.metrix_list[i][j] == 2)):
                    if ((self.metrix_list[i][j] == self.metrix_list[i][j+1]) and (self.metrix_list[i][j] == self.metrix_list[i][j+2]) and (self.metrix_list[i][j] == self.metrix_list[i][j+3]) and (self.metrix_list[i][j] == self.metrix_list[i][j+4])):
                        if self.pocet % 2 == 0:
                            self.vysledek = 2
                            uga.vyhra()
                            break
                        elif self.pocet % 2 ==1:
                            self.vysledek = 1
                            uga.vyhra()
                            break
        
        for i in range(12):
            for j in range(16):
                if ((self.metrix_list[i][j] == 1) or (self.metrix_list[i][j] == 2)):
                    if ((self.metrix_list[i][j] == self.metrix_list[i+1][j]) and (self.metrix_list[i][j] == self.metrix_list[i+2][j]) and (self.metrix_list[i][j] == self.metrix_list[i+3][j]) and (self.metrix_list[i][j] == self.metrix_list[i+4][j])):
                        if self.pocet % 2 == 0:
                            self.vysledek = 2
                            uga.vyhra()
                            break
                        elif self.pocet % 2 ==1:
                            self.vysledek = 1
                            uga.vyhra()
                            break
        
        for i in range(12):
            for j in range(12):
                if ((self.metrix_list[i][j] == 1) or (self.metrix_list[i][j] == 2)):
                    if ((self.metrix_list[i][j] == self.metrix_list[i+1][j+1]) and (self.metrix_list[i][j] == self.metrix_list[i+2][j+2]) and (self.metrix_list[i][j] == self.metrix_list[i+3][j+3]) and (self.metrix_list[i][j] == self.metrix_list[i+4][j+4])):
                        if self.pocet % 2 == 0:
                            self.vysledek = 2
                            uga.vyhra()
                            break
                        elif self.pocet % 2 ==1:
                            self.vysledek = 1
                            uga.vyhra()
                            break
        
        for i in range(12):
            for j in range(12):
                if ((self.metrix_list[i][j+4] == 1) or (self.metrix_list[i][j+4] == 2)):
                    if ((self.metrix_list[i][j+4] == self.metrix_list[i+1][j+3]) and (self.metrix_list[i][j+4] == self.metrix_list[i+2][j+2]) and (self.metrix_list[i][j+4] == self.metrix_list[i+3][j+1]) and (self.metrix_list[i][j+4] == self.metrix_list[i+4][j])):
                        if self.pocet % 2 == 0:
                            self.vysledek = 2
                            uga.vyhra()
                            break
                        elif self.pocet % 2 ==1:
                            self.vysledek = 1
                            uga.vyhra()
                            break
                    
                    
    def vyhra(self):
        self.plocha.destroy()            
        self.vyh_obraz = Tk()
        self.vyh_obraz.geometry("700x500")
        self.vyh_obraz.title("Piškvorky")
        
        a = Label(self.vyh_obraz, bg="blue")
        a.place(x=0, y=0, heigh =700, width=700)
        
        if self.vysledek == 1:
            a = Label(self.vyh_obraz, bg="blue")
            a.place(x=0, y=0, heigh =700, width=700)
            vyhtext = Label(self.vyh_obraz, text="Hráč č.1 vyhrál", font=("Arial", 35))
            vyhtext.place(x=180, y=20)
        elif self.vysledek == 2:
            a = Label(self.vyh_obraz, bg="red")
            a.place(x=0, y=0, heigh =700, width=700)
            vyhtext = Label(self.vyh_obraz, text="Hráč č.2 vyhrál", font=("Arial", 35))
            vyhtext.place(x=180, y=20)
        tla1 = Button(self.vyh_obraz, text="Konec", command= self.vyh_obraz.destroy, font=("Arial", 35))
        tla2 = Button(self.vyh_obraz, text="Hlavní nabídka", command= lambda: [self.vyh_obraz.destroy(), uga.menu()], font=("Arial", 35))
        tla1.place(x = 430, y = 100)
        tla2.place(x = 30, y = 300)
        if self.cislo_moznost == 1:
            tla = Button(self.vyh_obraz, text="Hrát znovu", command= lambda: [uga.hra(), self.vyh_obraz.destroy()], font=("Arial", 35))
            tla.place(x=30, y =100)
        elif self.cislo_moznost == 2:
            tla = Button(self.vyh_obraz, text="Hrát znovu", command= lambda: [uga.hra_cas(), self.vyh_obraz.destroy()], font=("Arial", 35))
            tla.place(x=30, y =100)
        elif self.cislo_moznost == 3:
            tla = Button(self.vyh_obraz, text="Hrát znovu", command= lambda: [uga.hra_pocitac() ,self.vyh_obraz.destroy()], font=("Arial", 35))
            tla.place(x=30, y =100)
                    
    def nanapoveda(self):
        messagebox.showinfo("Nápověda", "Hra je pro dva hráče, kteří se po každém kliknutí střídají. Hra se ovládá klikáním levého tlačítka myši na již neobsazené políčka. Cílem hry je mít pět svých znaků postavených bez přerušení před Vaším oponentem třemi způsoby: \n1.způsob - v řádku \n2.způsob - vertikálně(nadsebou, podsebou) \n3.způsob - diagonálně \n")

    def menapoveda(self):
        messagebox.showinfo("Nápověda", "Hra je pro dva hráče, kteří se po každém kliknutí střídají. Hra se ovládá klikáním levého tlačítka myši na již neobsazené políčka. Cílem hry je mít pět svých znaků postavených bez přerušení před Vaším oponentem třemi způsoby: \n1.způsob - v řádku \n2.způsob - vertikálně(nadsebou, podsebou) \n3.způsob - diagonálně \n")
        
    def oaplikaci(self):
        messagebox.showinfo("O aplikaci", "Tento program je moje ročníková práce, založená na hře piškvorky. Toto je skoro hotová verze. Pro více informací, nebo pokud máte nějaké návrhy pište na e-mail: 57418skultety@sstebrno.eu")


uga = Piskvorky()
uga.menu()