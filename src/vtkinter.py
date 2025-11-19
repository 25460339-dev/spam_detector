import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "¡Has presionado el botón!")
ventna = tk.Tk()
ventna.title("Ventana principal")

label = tk.Label(ventna, text="¡Hola, Mundo!")
label.pack(pady=10)

boton = tk.Button(ventna, text="preciona aqui", command=mostrar_mensaje)
boton.pack(pady=10)
ventna.mainloop()