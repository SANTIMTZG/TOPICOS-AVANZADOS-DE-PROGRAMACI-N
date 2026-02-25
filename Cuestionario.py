import flet as ft


def main(page: ft.Page):
    page.title = "Formulario"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#e6e1cc"
    page.padding = 50
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    def campo(label):
        return ft.TextField(
            hint_text=label,
            border=ft.InputBorder.OUTLINE,
            border_width=2,
            border_color="black",
            bgcolor="white",
            color="black",
            hint_style=ft.TextStyle(color="black"),
            height=70,
            text_size=18,
            expand=True,
        )

    # Campos
    nombre = campo("Nombre")

    numero_control = ft.TextField(
        hint_text="Numero de control",
        keyboard_type=ft.KeyboardType.NUMBER,
        border=ft.InputBorder.OUTLINE,
        border_width=2,
        border_color="black",
        bgcolor="white",
        color="black",
        height=70,
        text_size=18,
        expand=True,
    )

    email = campo("Email")

    carreras_lista = [
        "Contador Público",
        "Ingeniería Civil",
        "Ingeniería Electrónica",
        "Ingeniería en Gestión Empresarial",
        "Ingeniería en Sistemas",
        "Ingeniería Industrial",
        "Maestría en Ingeniería Administrativa",
    ]

    carrera = ft.Dropdown(
        hint_text="Carrera",
        options=[ft.dropdown.Option(c) for c in carreras_lista],
        border_color="black",
        border_width=2,
        bgcolor="white",
        color="black",
        height=70,
        text_size=18,
        expand=True,
    )

    semestre = ft.TextField(
        hint_text="Semestre",
        keyboard_type=ft.KeyboardType.NUMBER,
        border=ft.InputBorder.OUTLINE,
        border_width=2,
        border_color="black",
        bgcolor="white",
        color="black",
        height=70,
        text_size=18,
        expand=True,
    )

    genero = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Text("Género:", size=18),
                ft.Radio(value="Masculino", label="Masculino"),
                ft.Radio(value="Femenino", label="Femenino"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=40,
        )
    )

    #Diálogos

    dialogo = ft.AlertDialog(
        modal=True,
        title=ft.Text(""),
        content=ft.Text(""),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: cerrar_dialogo())
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.overlay.append(dialogo)

    def cerrar_dialogo():
        dialogo.open = False
        page.update()

    def mostrar_dialogo(titulo, mensaje):
        dialogo.title.value = titulo
        dialogo.content.value = mensaje
        dialogo.open = True
        page.update()

    # Validación

    def limpiar_errores():
        for campo in [nombre, numero_control, email, semestre]:
            campo.error_text = None
            campo.border_color = "black"
        carrera.border_color = "black"

    def marcar_error(control, mensaje):
        control.error_text = mensaje
        control.border_color = "red"

    def validar(e):
        limpiar_errores()

        # Validacion, ventanas

        if not nombre.value:
            marcar_error(nombre, "Campo obligatorio")
            mostrar_dialogo("Error", "Todos los campos son obligatorios.")
            return

        if not numero_control.value:
            marcar_error(numero_control, "Campo obligatorio")
            mostrar_dialogo("Error", "Todos los campos son obligatorios.")
            return

        if not email.value:
            marcar_error(email, "Campo obligatorio")
            mostrar_dialogo("Error", "Todos los campos son obligatorios.")
            return

        if not carrera.value:
            carrera.border_color = "red"
            mostrar_dialogo("Error", "Todos los campos son obligatorios.")
            return

        if not semestre.value:
            marcar_error(semestre, "Campo obligatorio")
            mostrar_dialogo("Error", "Todos los campos son obligatorios.")
            return

        if not genero.value:
            mostrar_dialogo("Error", "Todos los campos son obligatorios.")
            return

        if numero_control.value and not numero_control.value.isdigit():
            marcar_error(numero_control, "Solo números")
            mostrar_dialogo("Error", "El Número de Control solo debe contener números.")
            return

        if semestre.value and not semestre.value.isdigit():
            marcar_error(semestre, "Solo números")
            mostrar_dialogo("Error", "El Semestre solo debe contener números.")
            return

        # Si todo está bien
        mensaje = (
            f"Nombre: {nombre.value}\n"
            f"Número de control: {numero_control.value}\n"
            f"Email: {email.value}\n"
            f"Carrera: {carrera.value}\n"
            f"Semestre: {semestre.value}\n"
            f"Género: {genero.value}"
        )

        mostrar_dialogo("Datos registrados correctamente", mensaje)

    enviar = ft.ElevatedButton(
        "Enviar",
        height=70,
        width=float("inf"),
        on_click=validar,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=0),
            bgcolor="#9e9e9e",
            color="black",
        ),
    )

    page.add(
        ft.Column(
            [
                nombre,
                numero_control,
                email,
                ft.Row(
                    [carrera, semestre],
                    spacing=30,
                ),
                genero,
                enviar,
            ],
            spacing=35,
            expand=True,
        )
    )


ft.run(main)