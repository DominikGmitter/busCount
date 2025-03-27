import tkinter
from tkinter import messagebox
import funkcie
from tkinter import font


class Aplikacia(tkinter.Tk):
    # tkinter.Tk() - hlavné (root) okno

    def __init__(self):
        super().__init__()
        self.title("Vypocet")
        self.vytvor_gui()
        self.velkost_okna()
        self.mainloop()

    def velkost_okna(self):
        self.geometry('700x400-600+300')

    def vytvor_gui(self):
        highlightFont = font.Font(family='Helvetica', name='appHighlightFont', size=20, weight='bold')

        tkinter.Label(self, text='Zadaj pocet cestujucich: ', font=highlightFont).grid(row=0, column=0)
        self.vstup1 = tkinter.StringVar()
        tkinter.Entry(self, textvariable=self.vstup1, font=highlightFont).grid(row=0, column=1)

        tkinter.Label(self, text='Zadaj pocet kilometrov: ', font=highlightFont).grid(row=1, column=0)
        self.vstup2 = tkinter.StringVar()
        tkinter.Entry(self, textvariable=self.vstup2, font=highlightFont).grid(row=1, column=1)

        tkinter.Button(self, text='Vypocitaj', font=highlightFont, background='yellow', command=self.vysledny_riadok).grid(row=2, column=1, columnspan=1)

        tkinter.Label(self, text='Pocet prostriedkov: ', font=highlightFont).grid(row=3, column=0)
        self.vystup1 = tkinter.StringVar()
        tkinter.Label(self, textvariable=self.vystup1, font=highlightFont).grid(row=3, column=1)

        tkinter.Label(self, text='Cena: ', font=highlightFont).grid(row=4, column=0, columnspan=1)
        self.vystup2 = tkinter.StringVar()
        tkinter.Label(self, textvariable=self.vystup2, font=highlightFont).grid(row=4, column=1)

        tkinter.Button(self, text='Zavri aplikaciu', font=highlightFont, background='red', foreground='white', command=self.destroy).grid(row=5, column=1)

    def vypocitaj_bs_ms(self):
        try:
           pocet_cestujucich = int(self.vstup1.get())
        except ValueError:
            self.zobraz_chybu('Nezadal si číslo')
        else:
            try:
                prostriedky = funkcie.pocet_prostriedkov(pocet_cestujucich)
            except ValueError as chyba:
                self.zobraz_chybu(chyba)
            else:
                self.vystup1.set(prostriedky)

    def vypocitaj_cenu(self):
        global cena
        try:
            cena = float(self.vstup1.get())
        except ValueError:
            self.zobraz_chybu('Nezadal si pocet cestujucich ako číslo')
        try:
            kilometre = float(self.vstup2.get())
        except ValueError:
            self.zobraz_chybu('Nezadal si kilometre ako cislo')
        else:
            try:
                celk_cena = funkcie.celkova_cena(cena, kilometre)
            except ValueError as chyba:
                self.zobraz_chybu(chyba)
            else:
                self.vystup2.set(celk_cena)

    def vysledny_riadok(self):
        self.vypocitaj_bs_ms()
        self.vypocitaj_cenu()

    def zobraz_chybu(self, chyba):
        messagebox.showerror('Chyba', chyba)


Aplikacia()
