import flet as ft
import random
import os

def main(page: ft.Page):
    page.title = "Piedra, Papel o Tijera - Glow Edition"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.spacing = 20

    opciones = ["Piedra", "Papel", "Tijera"]

    # --- PANTALLA JUGADOR (MAGENTA) ---
    txt_jugador = ft.Text("¿LISTO?", size=22, weight="bold", color="white")
    pantalla_jugador = ft.Container(
        content=txt_jugador,
        width=350,
        height=90,
        alignment=ft.Alignment.CENTER,
        bgcolor="#ff00ff",
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=25, color="#ff00ff", spread_radius=2),
    )

    # --- PANTALLA COMPUTADORA (CYAN) ---
    txt_pc = ft.Text("ESPERANDO...", size=22, weight="bold", color="white")
    pantalla_pc = ft.Container(
        content=txt_pc,
        width=350,
        height=90,
        alignment=ft.Alignment.CENTER,
        bgcolor="#00ffff",
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=25, color="#00ffff", spread_radius=2),
    )

    resultado_texto = ft.Text("", size=30, weight="bold", italic=True)

    def determinar_ganador(usuario, pc):
        if usuario == pc:
            return "¡EMPATE!"
        reglas = {"Piedra": "Tijera", "Papel": "Piedra", "Tijera": "Papel"}
        return "¡GANASTE!" if reglas[usuario] == pc else "PERDISTE"

    def jugar(e):
        usuario = e.control.data
        pc = random.choice(opciones)

        txt_jugador.value = f"TÚ: {usuario.upper()}"
        txt_pc.value = f"PC: {pc.upper()}"

        r = determinar_ganador(usuario, pc)
        resultado_texto.value = r

        if r == "¡GANASTE!":
            resultado_texto.color = "#00ff00"
        elif r == "PERDISTE":
            resultado_texto.color = "#ff0055"
        else:
            resultado_texto.color = "#ffffff"

        page.update()

    def reiniciar(e):
        txt_jugador.value = "¿LISTO?"
        txt_pc.value = "ESPERANDO..."
        resultado_texto.value = ""
        page.update()

    # --- MENÚ DE SELECCIÓN ---
    menu = ft.PopupMenuButton(
        content=ft.Container(
            content=ft.Text("🎮 SELECCIONAR ARMA 🎮", size=16, weight="bold", color="white"),
            width=280,
            height=60,
            alignment=ft.Alignment.CENTER,
            border=ft.border.all(2, "white24"),
            border_radius=10,
        ),
        items=[
            ft.PopupMenuItem(content=ft.Text("🪨 Piedra"), on_click=jugar, data="Piedra"),
            ft.PopupMenuItem(content=ft.Text("📄 Papel"), on_click=jugar, data="Papel"),
            ft.PopupMenuItem(content=ft.Text("✂️ Tijera"), on_click=jugar, data="Tijera"),
        ],
    )

    page.add(
        ft.Text("PIEDRA • PAPEL • TIJERA", size=32, weight="heavy", color="#ffffff"),
        ft.Text("DUELO NEÓN", size=14, color="white60"),
        ft.Divider(height=20, color="transparent"),
        pantalla_jugador,
        ft.Text("VS", size=20, weight="bold", color="white30"),
        pantalla_pc,
        resultado_texto,
        menu,
        ft.TextButton("REINICIAR", on_click=reiniciar, style=ft.ButtonStyle(color="white60")),
    )

# 🔥 CONFIGURACIÓN PARA RENDER (WEB)
port = int(os.environ.get("PORT", 8550))
ft.app(target=main, view=ft.WEB_BROWSER, port=port)