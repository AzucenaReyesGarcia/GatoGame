import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class boton:
    def __init__(self, master, fila, columna, juego):
        self.boton = ttk.Button(master, text='', width=5, command=lambda: juego.empezar_el_juego(fila, columna))
        self.boton.grid (row=fila, column=columna)

    def actualizar_estado(self, texto):
        self.boton.config(text=texto)

class juego:
    def __init__(self, master):
        self.master = master
        self.turno = 'O'
        self.tablero = [[''for _ in range(3)]for _ in range(3)]
        self.botones = [[boton(master, i, j, self)for j in range(3)]for i in range(3)] 

    def empezar_el_juego(self, fila, columna):
        if self.tablero[fila][columna] == '':
            self.tablero[fila][columna] = self.turno
            self.botones[fila][columna].actualizar_estado(self.turno)
            if self.verificar_ganador():
                messagebox.showinfo(message=f"El ganador es {self.turno}", title="Hay ganador")
                self.reiniciar()
            elif all(columna != '' for fila in self.tablero for columna in fila):
                messagebox.showinfo(message="¡Empate", title="Perdedores")
                self.reiniciar()
            else:
                self.turno = 'O' if self.turno == 'X' else 'X'

    def verificar_ganador(self):
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != '':
                return True
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != '':
                return True
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != '':
            return True
        return False

    def reiniciar(self):
        self.turno = 'X'
        self.tablero = [[''for _ in range(3)]for _ in range(3)]
        for fila in self.botones:
            for boton in fila:
                boton.actualizar_estado('')

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Juego del gato")
    juego = juego(root)
    root.mainloop()