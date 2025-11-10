import flet as ft
import sqlite3

# Función para crear la base de datos y tabla si no existe
def crear_base_datos():
    conn = sqlite3.connect('torneos.db')  # Archivo .db
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_equipo TEXT NOT NULL,
            categoria TEXT,
            numero_jugadores INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Función para insertar un equipo en la base de datos
def insertar_equipo(nombre, categoria, num_jugadores):
    conn = sqlite3.connect('torneos.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO equipos (nombre_equipo, categoria, numero_jugadores)
        VALUES (?, ?, ?)
    ''', (nombre, categoria, num_jugadores))
    conn.commit()
    conn.close()

# Función principal de la app Flet
def registro_app(page: ft.Page):
    page.title = "Registro de Equipos ⚽"
    page.scroll = ft.ScrollMode.AUTO
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    

    # Crear la base de datos al iniciar
    crear_base_datos()

    # Campos del formulario
    nombre_field = ft.TextField(label="Nombre del Equipo", width=300)
    categoria_field = ft.TextField(label="Categoría", width=300)  # Ej. Infantil, Juvenil, etc.
    num_jugadores_field = ft.TextField(label="Número de Jugadores", width=300, keyboard_type=ft.KeyboardType.NUMBER)

    # Función para manejar el clic del botón
    def guardar_equipo(e):
        nombre = nombre_field.value
        categoria = categoria_field.value
        num_jugadores = int(num_jugadores_field.value) if num_jugadores_field.value else 0

        #validar datos
        if nombre:  
            insertar_equipo(nombre, categoria, num_jugadores)
            page.snack_bar = ft.SnackBar(ft.Text("Equipo registrado"))
            page.snack_bar.open = True
            # Limpiar campos
            nombre_field.value = ""
            categoria_field.value = ""
            num_jugadores_field.value = ""
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error: Ingresa al menos el nombre del equipo."))
            page.snack_bar.open = True
            page.update()

    # Botón de guardar
    guardar_btn = ft.ElevatedButton("Registrar Equipo", on_click=guardar_equipo)

    # Layout de la página
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Formulario de Registro de Equipos", size=20, weight=ft.FontWeight.BOLD),
                    nombre_field,
                    categoria_field,
                    num_jugadores_field,
                    guardar_btn,
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=20,
            ),
            padding=20,
        )
    )

# Ejecutar la app
if __name__ == "__main__":
    ft.app(target=registro_app)

