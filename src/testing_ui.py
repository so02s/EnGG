import flet as ft
# from domain import Rating, FlashCard, Word, Lang, SMData

# UI components
# TODO Стили

def create_top_row(remaining: int, on_add_click) -> ft.Row:
    add_button = ft.IconButton(icon=ft.icons.Icons.ADD, on_click=on_add_click)
    remaining_text = ft.Text(str(remaining), size=12, color=ft.Colors.GREY_600)
    return ft.Row(
        [remaining_text, add_button],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )



def main(page: ft.Page):

    def handle_pan_update(e: ft.DragUpdateEvent[ft.GestureDetector]):
        e.control.top = max(0.0, e.control.top + e.local_delta.y)
        e.control.left = max(0.0, e.control.left + e.local_delta.x)
        e.control.update()

    page.add(
        ft.Stack(
            width=1000,
            height=500,
            controls=[
                ft.GestureDetector(
                    mouse_cursor=ft.MouseCursor.MOVE,
                    drag_interval=10,
                    on_vertical_drag_update=handle_pan_update,
                    left=100,
                    top=100,
                    content=ft.Container(bgcolor=ft.Colors.BLUE, width=50, height=50),
                ),
            ],
        )
    )


# CARD_BG_COLOR = ft.Colors.GREEN_300
# cards = [
#     FlashCard(
#         word=Word("apple", Lang.ENG),
#         translation=Word("яблоко", Lang.RU),
#         topic="food",
#         sm=SMData()
#     ),
#     FlashCard(
#         word=Word("dog", Lang.ENG),
#         translation=Word("собака", Lang.RU),
#         topic="animals",
#         sm=SMData()
#     ),
# ]

# class MockStudyViewModel:
#     def __init__(self):
#         self.cards = cards
#         self.index = 0

#     def has_card(self):
#         return self.index < len(self.cards)

#     def get_current_card(self):
#         return self.cards[self.index] if self.has_card() else None

#     def answer(self, rating: Rating):
#         if self.has_card():
#             self.cards[self.index].answer(rating)
#             self.index += 1

#     def get_remaining_count(self):
#         return max(0, len(self.cards) - self.index)




# @ft.control("study_card")
# class StudyCard(ft.Control):
#     def __init__(self, view_model: MockStudyViewModel, on_answer):
#         super().__init__()
#         self.vm = view_model
#         self.on_answer = on_answer
#         self.drag_start_x = 0
#         self.drag_offset = 0
#         self.flipped = False

#         # Текстовые элементы
#         self.front_text = ft.Text(size=24)
#         self.back_text = ft.Text(size=18, color=ft.Colors.GREY_600, visible=False)
#         self.example_text = ft.Text(size=14, color=ft.Colors.GREY_500, visible=False)

#         # Контейнер карточки
#         self.card_container = ft.Container(
#             content=ft.Column(
#                 [self.front_text, self.back_text, self.example_text],
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#             ),
#             alignment=ft.alignment.Alignment.CENTER,
#             width=300,
#             height=250,
#             bgcolor=CARD_BG_COLOR,
#             border_radius=10,
#             ink=True,
#         )

#         # Жесты
#         self.gesture = ft.GestureDetector(
#             content=self.card_container,
#             on_pan_start=self.on_pan_start,
#             on_pan_update=self.on_pan_update,
#             on_pan_end=self.on_pan_end,
#             on_tap=self.on_tap,
#         )

#     def build(self):
#         return self.gesture

#     def on_pan_start(self, e):
#         self.drag_start_x = e.local_x
#         self.drag_offset = 0

#     def on_pan_update(self, e):
#         # Накопляем смещение (delta_x — изменение с последнего вызова)
#         self.drag_offset += e.delta_x
#         # Сдвигаем карточку пропорционально смещению (масштабируем для плавности)
#         self.card_container.offset = ft.transform.Offset(self.drag_offset / 300, 0)
#         self.card_container.update()

#     def on_pan_end(self, e):
#         if self.drag_offset > 50:
#             self.on_answer(Rating.GOOD)
#         elif self.drag_offset < -50:
#             self.on_answer(Rating.BAD)
#         else:
#             # Возвращаем карточку на место
#             self.card_container.offset = ft.transform.Offset(0, 0)
#             self.card_container.update()
#         self.drag_offset = 0

#     def on_tap(self, e):
#         self.flip_card()

#     def flip_card(self):
#         if self.vm.has_card():
#             self.flipped = not self.flipped
#             self.front_text.visible = not self.flipped
#             self.back_text.visible = self.flipped
#             self.example_text.visible = self.flipped and bool(self.example_text.value)
#             self.update()

#     def update_card(self, card):
#         """Обновляет содержимое карточки и сбрасывает состояние переворота."""
#         self.front_text.value = card.word.value
#         self.back_text.value = card.translation.value
#         self.example_text.value = card.example or ""
#         self.flipped = False
#         self.front_text.visible = True
#         self.back_text.visible = False
#         self.example_text.visible = False
#         self.card_container.offset = ft.Offset(0, 0)
#         self.update()


# def main(page: ft.Page):
#     page.title = "UI Test - Flashcards"
#     page.theme_mode = ft.ThemeMode.DARK
#     page.padding = 20
#     page.window.width = 400
#     page.window.height = 800
#     page.window.resizable = False

#     # Вспомогательные элементы
#     remaining_text = ft.Text("-", size=12, color=ft.Colors.GREY_600)
#     add_button = ft.IconButton(icon=ft.icons.Icons.ADD, on_click=lambda e: print("Add card"))
#     top_row = ft.Row([remaining_text, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
#     info_text = ft.Text("Testing", visible=True)

#     mock_vm = MockStudyViewModel()

#     # Создаём карточку с колбэком
#     def on_answer(rating: Rating):
#         mock_vm.answer(rating)
#         update_ui()

#     card = StudyCard(mock_vm, on_answer)

#     def update_ui():
#         if mock_vm.has_card():
#             card.update_card(mock_vm.get_current_card())
#             remaining_text.value = f"Осталось: {mock_vm.get_remaining_count()}"
#             remaining_text.visible = True
#             info_text.visible = False
#         else:
#             info_text.value = "Поздравляем! Все карточки изучены."
#             info_text.visible = True
#             remaining_text.visible = False
#         page.update()

#     # Первоначальное обновление UI
#     update_ui()

#     page.add(
#         ft.Column(
#             [top_row, card, info_text],
#             alignment=ft.MainAxisAlignment.CENTER,
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#             expand=True
#         )
#     )

if __name__ == "__main__":
    ft.run(main)