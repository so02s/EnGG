# src\web\study_view\page.py
import flet as ft
from domain import Rating
from .model import StudyViewModel
from .ui_elem import CardStyle, GestureCard

def create_card_widget(view_model, on_swipe_callback):
    if not view_model.has_card():
        return None
    card = view_model.get_current_card()
    card_style = CardStyle(title=f"{card.word.value}\n{card.translation.value}")
    gesture_card = GestureCard(content=card_style, on_swipe=on_swipe_callback)
    return gesture_card

def study_view(page: ft.Page, view_model: StudyViewModel, on_add_callback):
    info_text = ft.Text("", visible=False)
    add_button = ft.IconButton(icon=ft.icons.Icons.ADD, on_click=lambda e: on_add_callback())
    top_row = ft.Row([add_button], alignment=ft.MainAxisAlignment.END)

    card_area = ft.Container()

    def update_ui():
        if view_model.has_card():
            card_area.content = create_card_widget(view_model, on_answer)
            info_text.visible = False
        else:
            card_area.content = None
            info_text.value = "Поздравляем! Все карточки изучены."
            info_text.visible = True
        page.update()

    def on_answer(rating: Rating):
        view_model.answer(rating)
        update_ui()

    # Инициализация
    update_ui()

    # Компоновка страницы
    page.add(
        ft.Column(
            [top_row, card_area, info_text],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )