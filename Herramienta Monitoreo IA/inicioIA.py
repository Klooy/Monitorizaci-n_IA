import tkinter as tk
from PIL import ImageTk, Image
import webbrowser
import os
import subprocess
import main_IA

def open_chat():
    subprocess.Popen(["python", "chat.py"])

# Crear la ventana principal
root = tk.Tk()
root.title("Inicio IA")
root.geometry("300x700")  # Tamaño de la ventana

# Configurar el color de fondo del menú
root.configure(bg='lightblue')

# Cargar y mostrar el logo de la IA
img = ImageTk.PhotoImage(Image.open("inteligencia-artificial.png"))
panel = tk.Label(root, image=img, bg='lightblue')
panel.pack(side="top", fill="both", expand="yes")

# Crear el botón de acción "Iniciar Chat"
chat_button = tk.Button(root, text="Iniciar Chat", command=open_chat, bg='purple', activebackground='purple', height=3, width=20, font=('Helvetica', '16'), relief='ridge', bd=5)
chat_button.pack(pady=10)

# Crear el botón de acción "Monitorizar IA"
monitor_button = tk.Button(root, text="Monitorizar IA", command=main_IA.iniciar, bg='purple', activebackground='purple', height=3, width=20, font=('Helvetica', '16'), relief='ridge', bd=5)
monitor_button.pack(pady=10)
# Crear el botón de ayuda
def open_web():
    webbrowser.open('http://www.example.com')  # Aquí puedes poner la URL de la página de ayuda que quieras abrir

help_button = tk.Button(root, text="Ayuda", command=open_web, bg='purple', activebackground='purple', height=3, width=20, font=('Helvetica', '16'), relief='ridge', bd=5)
help_button.pack(pady=10)

# Ejecutar la interfaz de usuario
root.mainloop()
