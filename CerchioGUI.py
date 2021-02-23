import tkinter as tk

from Cerchio import *


class CerchioGUI(tk.Frame):

    def __init__(self, master=None, raggio=0):  # master è il widget genitore
        # inizializzazione del frame
        super().__init__(master)
        # creazione di un oggetto cerchio
        self.circle = Cerchio(raggio)
        self.grid()  # layout a griglia
        # titolo del frame
        self.__title_frame = "Cerchio"
        self.master.title(self.__title_frame)
        # etichetta raggio
        self.lbl_raggio = tk.Label(self, text="Raggio")
        self.lbl_raggio.grid(row=0, column=0, pady=5, sticky=tk.E)
        # campo raggio
        self.vRaggio = tk.DoubleVar()  # variabile da abbinare al campo
        self.txt_raggio = tk.Entry(self, textvariable=self.vRaggio, state=tk.DISABLED, width=8, justify=tk.RIGHT)
        self.txt_raggio.grid(row=0, column=1, pady=5, sticky=tk.W)
        # slider per nuovo raggio
        self.sld_nuovo_raggio = tk.Scale(self, from_=0, to=200, orient=tk.HORIZONTAL,
                                         command=self.__nuovo_raggio)
        self.sld_nuovo_raggio.grid(row=0, column=2, pady=5, sticky=tk.W)
        # etichetta diametro
        self.lbl_diametro = tk.Label(self, text="Diametro")
        self.lbl_diametro.grid(row=1, column=0, pady=5, sticky=tk.E)
        # campo diametro
        self.vDiametro = tk.DoubleVar()  # variabile da abbinare al campo
        self.txt_diametro = tk.Entry(self, textvariable=self.vDiametro, state=tk.DISABLED, width=8, justify=tk.RIGHT)
        self.txt_diametro.grid(row=1, column=1, pady=5, sticky=tk.W)
        # etichetta circonferenza
        self.lbl_circonferenza = tk.Label(self, text="Circonferenza")
        self.lbl_circonferenza.grid(row=1, column=2, pady=5, sticky=tk.E)
        # campo circonferenza
        self.vCirconferenza = tk.DoubleVar()  # variabile da abbinare al campo
        self.txt_circonferenza = tk.Entry(self, textvariable=self.vCirconferenza, state=tk.DISABLED, width=8,
                                          justify=tk.RIGHT)
        self.txt_circonferenza.grid(row=1, column=3, pady=5, sticky=tk.W)
        # etichetta area
        self.lbl_area = tk.Label(self, text="Area")
        self.lbl_area.grid(row=1, column=4, pady=5, sticky=tk.E)
        # campo area
        self.vArea = tk.DoubleVar()  # variabile da abbinare al campo
        self.txt_area = tk.Entry(self, textvariable=self.vArea, state=tk.DISABLED, width=8, justify=tk.RIGHT)
        self.txt_area.grid(row=1, column=5, pady=5, sticky=tk.W)
        # canvas
        self.canvas = tk.Canvas(self, width=500, height=500, bg='white')
        self.canvas.grid(row=3, column=0, columnspan=20)
        # aggiorna valori
        self.aggiornaGUI()

        # loop di attesa eventi
        self.mainloop()

    def aggiornaGUI(self):
        self.vRaggio.set(round(self.circle.raggio, 2))
        self.vDiametro.set(round(self.circle.diametro, 2))
        self.vCirconferenza.set(round(self.circle.circonferenza, 2))
        self.vArea.set(round(self.circle.area, 2))
        self.canvas.delete("all")
        self.__circle_drawing = self.canvas.create_oval(10, 10, 10 + self.circle.diametro, 10 + self.circle.diametro,
                                                        fill="blue")

    def __nuovo_raggio(self,  value):
        self.circle.raggio = float ( value)
        self.aggiornaGUI()


if __name__ == '__main__':
    def main():
        f = CerchioGUI(tk.Tk(), 10)


    main()
