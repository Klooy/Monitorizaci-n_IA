import tkinter as tk
from tkinter import ttk, PhotoImage

# Historial de búsqueda preestablecido
historial_busqueda = {
    '¿Qué es la ciberseguridad?': 'La ciberseguridad es la práctica de proteger sistemas, redes y programas de ataques digitales.',
    '¿Cómo proteger mi correo electrónico?': 'Puedes proteger tu correo electrónico utilizando una contraseña segura, habilitando la autenticación de dos factores, etc.',
    '¿Qué es un ataque de fuerza bruta?': 'Un ataque de fuerza bruta es un método de prueba de todas las posibles combinaciones de contraseñas hasta encontrar la correcta.',
    '¿Qué es la inteligencia artificial?': 'La inteligencia artificial es una rama de la informática que se centra en la creación de sistemas capaces de realizar tareas que normalmente requieren la inteligencia humana.',
    '¿Cómo funciona el internet?': 'Internet funciona mediante una serie de redes interconectadas que siguen el conjunto de protocolos de Internet (IP) para enviar y recibir datos.'
}

def enviar_pregunta(event=None):
    pregunta = entry.get()
    respuesta = historial_busqueda.get(pregunta, 'Lo siento, no tengo una respuesta para esa pregunta.')
    chat.insert('end', f'Tú: {pregunta}\n')
    chat.insert('end', f'IA: {respuesta}\n\n')
    entry.delete(0, 'end')

def iniciar_chat():
    global chat, entry  # Declarar chat y entry como variables globales

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Chat IA")
    root.geometry("400x650")  # Tamaño de la ventana
    root.configure(bg='lightblue')  # Color de fondo

    # Centrar la ventana en la pantalla
    window_width = 400
    window_height = 650
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Crear el widget de chat
    chat_label = tk.Label(root, text="Rapidín IA", font=("Helvetica", 16, "bold"), bg='lightblue')
    chat_label.pack(pady=10)
    chat = tk.Text(root, bg='white', width=50, height=30)
    chat.pack(pady=10)

    # Crear un marco para la entrada de texto y el botón de envío
    frame = tk.Frame(root, bg='lightblue')
    frame.pack()

    # Crear el widget de entrada
    entry_label = tk.Label(frame, text="Consulta Rapidín", font=("Helvetica", 16, "bold"), bg='lightblue')
    entry_label.pack(pady=10)
    entry = tk.Entry(frame, bg='white', width=40)
    entry.pack(side='left', padx=10)

    # Crear el botón de envío
    send_button = tk.Button(frame, text="Enviar", command=enviar_pregunta, bg='purple', activebackground='purple', height=1, width=10, font=('Helvetica', '10'), relief='ridge', bd=5)
    send_button.pack(side='right')

    # Permitir presionar Enter para enviar la pregunta
    root.bind('<Return>', enviar_pregunta)

    # Ejecutar la interfaz de usuario
    root.mainloop()

if __name__ == "__main__":
    iniciar_chat()