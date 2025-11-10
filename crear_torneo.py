import flet as ft

def CrearTorneoView(page: ft.Page):
    page.title = "Crear Torneo"

    nombre_torneo = ft.TextField(label="Nombre del Torneo", width=300)
    tipo_torneo = ft.Dropdown(
        label="Tipo de Torneo",
        width=300,
        options=[
            ft.dropdown.Option("Liga"),
            ft.dropdown.Option("Eliminación directa"),
        ],
    )
    num_equipos = ft.TextField(label="Número de Equipos", width=300, keyboard_type=ft.KeyboardType.NUMBER)

    mensaje = ft.Text(color="green")

    def guardar_torneo(e):
        if nombre_torneo.value and tipo_torneo.value and num_equipos.value:
            mensaje.value = f"Torneo '{nombre_torneo.value}' creado con éxito ✅"
        else:
            mensaje.value = "Por favor completa todos los campos ⚠️"
        page.update()

    guardar_btn = ft.ElevatedButton("Guardar Torneo", on_click=guardar_torneo)
    volver_btn = ft.ElevatedButton("Volver al menú", on_click=lambda e: page.go("/"))

    # Agregar todo a la página
    page.add(
        ft.Column(
            [
                ft.Text("🏆 Crear Torneo", size=30, weight=ft.FontWeight.BOLD),
                nombre_torneo,
                tipo_torneo,
                num_equipos,
                ft.Row([guardar_btn, volver_btn], alignment=ft.MainAxisAlignment.CENTER),
                mensaje,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

if __name__ == "__main__":
    ft.app(target=CrearTorneoView, view=ft.WEB_BROWSER)
