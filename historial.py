import flet as ft

def HistorialView(page: ft.Page):
    page.title = "Historial de Torneos"

    historial = [
        {"nombre": "WORLD CUP", "ganador": "BRASIL"},
        {"nombre": "Copa Libertadores", "ganador": "River Plate"},
    ]

    lista = ft.Column(
        [
            ft.Text(f"🏆 {h['nombre']} - Ganador: {h['ganador']}", size=20)
            for h in historial
        ],
        spacing=10,
    )

    volver_btn = ft.ElevatedButton("Volver al menú", on_click=lambda e: page.go("/"))

    # Agregar todo a la página
    page.add(
        ft.Column(
            [
                ft.Text("📜 Historial de Torneos", size=30, weight=ft.FontWeight.BOLD),
                lista,
                volver_btn,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

if __name__ == "__main__":
    ft.app(target=HistorialView, view=ft.WEB_BROWSER)
