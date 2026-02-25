import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Estática - IAP"
    page.window_width = 280
    page.window_height = 450
    page.window_resizable = False
    page.padding = 15

    expresion = ""

    # -------- FUNCIONES --------
    def agregar_numero(e):
        nonlocal expresion
        expresion += e.control.content.value
        display.value = expresion
        page.update()

    def agregar_operador(e):
        nonlocal expresion
        expresion += e.control.content.value
        display.value = expresion
        page.update()

    def calcular(e):
        nonlocal expresion
        try:
            expresion = str(eval(expresion))
            display.value = expresion
        except:
            display.value = "Error"
            expresion = ""
        page.update()

    def limpiar(e):  # 👈 FUNCIÓN NUEVA
        nonlocal expresion
        expresion = ""
        display.value = "0"
        page.update()

    # -------- DISPLAY --------
    display = ft.Text("0", size=20)

    seccion_display = ft.Container(
        content=display,
        bgcolor=ft.Colors.BLACK12,
        height=70,
        alignment=ft.Alignment(0, 0),
        border=ft.border.all(1, ft.Colors.RED)
    )

    # -------- BOTONES NUMÉRICOS --------
    def boton_numero(texto):
        return ft.Container(
            expand=1,
            height=50,
            bgcolor="blue",
            border=ft.border.all(1, "white"),
            content=ft.Text(texto, color="white"),
            alignment=ft.Alignment(0, 0),
            on_click=agregar_numero
        )

    seccion_numeros = ft.Column(
        controls=[
            ft.Row(controls=[
                boton_numero("7"),
                boton_numero("8"),
                boton_numero("9"),
            ]),
            ft.Row(controls=[
                boton_numero("4"),
                boton_numero("5"),
                boton_numero("6"),
            ]),
            ft.Row(controls=[
                boton_numero("1"),
                boton_numero("2"),
                boton_numero("3"),
            ]),
        ],
        spacing=10
    )

    # -------- BOTONES OPERACIONES --------
    def boton_operador(texto, funcion):
        return ft.Container(
            expand=1,
            height=60,
            bgcolor="green",
            border=ft.border.all(1, "white"),
            content=ft.Text(texto, color="white"),
            alignment=ft.Alignment(0, 0),
            on_click=funcion
        )

    seccion_operaciones = ft.Row(
        controls=[
            boton_operador("+", agregar_operador),
            boton_operador("-", agregar_operador),
            boton_operador("=", calcular),
            boton_operador("C", limpiar),  # 👈 BOTÓN NUEVO
        ]
    )

    # -------- CONSTRUCCIÓN FINAL --------
    page.add(
        ft.Column(
            controls=[
                seccion_display,
                ft.Text("Números:", size=12),
                seccion_numeros,
                ft.Divider(),
                ft.Text("Operaciones:", size=12),
                seccion_operaciones
            ],
            spacing=15
        )
    )

if __name__ == "__main__":
    ft.app(target=main)