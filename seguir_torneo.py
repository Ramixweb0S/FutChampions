import flet as ft

def SeguirTorneoView(page: ft.Page):
    page.title = "Seguir Torneo"

    # Ejemplo de torneos cargados localmente (simulado)
    torneos = [
        {"nombre": "Copa Entel", "tipo": "Liga"},
        {"nombre": "Desafío Cochabamba", "tipo": "Eliminación directa"},
    ]

    lista = ft.Column(
        [
            ft.Text(f"🏆 {t['nombre']} - {t['tipo']}", size=20)
            for t in torneos
        ],
        spacing=10,
    )

    volver_btn = ft.ElevatedButton("Volver al menú", on_click=lambda e: page.go("/"))

    # Agregar todo a la página
    page.add(
        ft.Column(
            [
                ft.Text("🔍 Seguir Torneo", size=30, weight=ft.FontWeight.BOLD),
                lista,
                volver_btn,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

if __name__ == "__main__":
    ft.app(target=SeguirTorneoView, view=ft.WEB_BROWSER)
