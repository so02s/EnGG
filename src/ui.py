import flet as ft
from web.study_view.ui_elem import CardStyle, GestureCard

def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 800

    card = CardStyle("Analytics")

    drag_card = GestureCard(card)

    page.add(drag_card)

ft.run(main)