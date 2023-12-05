import tkinter as tk
from tkinter import ttk

historial_busqueda = {
    '¿Qué es la ciberseguridad?': {'respuesta': 'La ciberseguridad es la práctica de proteger sistemas, redes y programas de ataques digitales.', 'fecha': '2023-12-01 10:00:00', 'usuario': 'Dev_Maria', 'tipo_consulta': 'Búsqueda en la web', 'ubicacion': 'Bogotá, Colombia'},
    '¿Cómo proteger mi correo electrónico?': {'respuesta': 'Puedes proteger tu correo electrónico utilizando una contraseña segura, habilitando la autenticación de dos factores, etc.', 'fecha': '2023-12-02 11:30:00', 'usuario': 'Dev_Juan', 'tipo_consulta': 'Consulta de correo electrónico', 'ubicacion': 'Medellín, Colombia'},
    '¿Qué es un ataque de fuerza bruta?': {'respuesta': 'Un ataque de fuerza bruta es un método de prueba de todas las posibles combinaciones de contraseñas hasta encontrar la correcta.', 'fecha': '2023-12-03 15:45:00', 'usuario': 'Dev_Felipe', 'tipo_consulta': 'Búsqueda en la web', 'ubicacion': 'Cali, Colombia'},
    '¿Qué es la inteligencia artificial?': {'respuesta': 'La inteligencia artificial es una rama de la informática que se centra en la creación de sistemas capaces de realizar tareas que normalmente requieren la inteligencia humana.', 'fecha': '2023-12-04 16:00:00', 'usuario': 'Dev_Luis', 'tipo_consulta': 'Búsqueda en la web', 'ubicacion': 'Barranquilla, Colombia'},
    '¿Cómo funciona el internet?': {'respuesta': 'Internet funciona mediante una serie de redes interconectadas que siguen el conjunto de protocolos de Internet (IP) para enviar y recibir datos.', 'fecha': '2023-12-05 17:30:00', 'usuario': 'Dev_Nurys', 'tipo_consulta': 'Búsqueda en la web', 'ubicacion': 'Cartagena, Colombia'}
}

def mostrar_historial():
    # Crear una nueva ventana para mostrar el historial de búsqueda
    root = tk.Tk()
    root.title("Historial de búsqueda")

    # Centrar la nueva ventana en la pantalla
    window_width = 500
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Crear un marco para el área de desplazamiento
    frame = ttk.Frame(root)
    frame.pack(fill='both', expand=True)

    # Crear un área de desplazamiento
    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side='right', fill='y')

    # Crear un widget de texto y añadirlo al área de desplazamiento
    text_widget = tk.Text(frame, yscrollcommand=scrollbar.set, wrap='word')
    text_widget.pack(side='left', fill='both', expand=True)

    # Configurar el área de desplazamiento para desplazarse con el widget de texto
    scrollbar.config(command=text_widget.yview)

    # Añadir el historial de búsqueda al widget de texto
    for pregunta, info in historial_busqueda.items():
        text_widget.insert('end', f'Usuario: 👤 {info["usuario"]}\nTipo de consulta: {info["tipo_consulta"]}\nFecha: {info["fecha"]}\nUbicación: {info["ubicacion"]}\nPregunta: {pregunta}\nRespuesta: {info["respuesta"]}\n')
        text_widget.insert('end', '-'*50 + '\n')

    # Deshabilitar la edición del widget de texto
    text_widget.config(state='disabled')

def iniciar():
    # Crear la ventana de la aplicación
    root = tk.Tk()
    root.title("Aplicación")

    # Centrar la ventana en la pantalla
    window_width = 200
    window_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Crear un botón para mostrar el historial de búsqueda
    button = ttk.Button(root, text="Mostrar historial de búsqueda", command=lambda: [mostrar_historial(), root.destroy()], style='Custom.TButton')

    # Crear un estilo personalizado para el botón
    style = ttk.Style()
    style.configure('Custom.TButton', font=('Helvetica', '16'), background='purple', foreground='white', borderwidth=5)

    button.pack(expand=True)

    # Ejecutar la aplicación
    root.mainloop()