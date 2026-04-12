import flet as ft
from .model import AddCardViewModel

def add_card_view(page: ft.Page, view_model: AddCardViewModel, on_back_callback):
    """Экран добавления новой карточки."""
    # Поля ввода
    front_field = ft.TextField(label="Слово (англ.)", width=300)
    back_field = ft.TextField(label="Перевод (рус.)", width=300)
    topic_field = ft.TextField(label="Тема (опционально)", width=300)

    status_text = ft.Text("", color=ft.Colors.GREEN)

    def on_add_click(e):
        view_model.word_value = front_field.value
        view_model.translation_value = back_field.value
        view_model.topic = topic_field.value
        if view_model.add_card():
            status_text.value = "Карточка добавлена!"
            status_text.color = ft.Colors.GREEN
            # Очищаем поля
            front_field.value = ""
            back_field.value = ""
            topic_field.value = ""
        else:
            status_text.value = "Ошибка: заполните слово и перевод"
            status_text.color = ft.Colors.RED
        page.update()

    def on_back_click(e):
        on_back_callback()

    add_btn = ft.ElevatedButton("Добавить", on_click=on_add_click)
    back_btn = ft.ElevatedButton("Назад", on_click=on_back_click)

    page.clean()
    page.add(
        ft.Column(
            [
                ft.Text("Добавить новую карточку", size=24),
                front_field,
                back_field,
                topic_field,
                ft.Row([add_btn, back_btn], alignment=ft.MainAxisAlignment.CENTER),
                status_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )