import flet as ft
from ..view_models.study import StudyViewModel
from domain import Rating

def study_view(page: ft.Page, view_model: StudyViewModel, on_add_callback):
    front_text = ft.Text(size=24)
    back_text = ft.Text(size=18, color=ft.Colors.GREY_600, visible=False)

    card_container = ft.Container(
        content=ft.Column([front_text, back_text], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.Alignment.CENTER,
        width=300,
        height=200,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        ink=True,
        on_click=lambda e: flip_card()
    )

    btn_again = ft.ElevatedButton("Снова", on_click=lambda e: on_answer(Rating.BAD))
    btn_good = ft.ElevatedButton("Хорошо", on_click=lambda e: on_answer(Rating.NEUTRAL))
    btn_easy = ft.ElevatedButton("Легко", on_click=lambda e: on_answer(Rating.GOOD))
    row_buttons = ft.Row([btn_again, btn_good, btn_easy], alignment=ft.MainAxisAlignment.CENTER)

    # Кнопка добавления новой карточки
    add_button = ft.IconButton(icon=ft.icons.Icons.ADD, on_click=lambda e: on_add_callback())
    top_row = ft.Row([add_button], alignment=ft.MainAxisAlignment.END)

    info_text = ft.Text("", visible=False)

    def flip_card():
        if view_model.has_card():
            front_text.visible = not front_text.visible
            back_text.visible = not back_text.visible
            page.update()

    def update_ui():
        if view_model.has_card():
            card = view_model.get_current_card()
            front_text.value = card.word.value
            back_text.value = card.translation.value
            front_text.visible = True
            back_text.visible = False
            info_text.visible = False
            row_buttons.visible = True
        else:
            info_text.value = "Поздравляем! Все карточки изучены."
            info_text.visible = True
            row_buttons.visible = False
        page.update()

    def on_answer(rating: Rating):
        view_model.answer(rating)
        update_ui()

    # Инициализация UI
    update_ui()
    page.add(
        ft.Column(
            [top_row, card_container, row_buttons, info_text],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )