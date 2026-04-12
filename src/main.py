import flet as ft
# from datasource import PeeweeCardRepository
# from web import study_view, add_card_view, StudyViewModel, AddCardViewModel
# from datasource.database import db
# from datasource.model.peewee_models import FlashCardModel

from web.study_view import study_view, StudyViewModel
from tests.mock import MockCardRepository

def main(page: ft.Page):
    page.title = "English Flashcards"
    page.theme_mode = ft.ThemeMode.DARK

    repo = MockCardRepository()
    view_model = StudyViewModel(repo)

    def on_add():
        print("Добавить карточку")

    study_view(page, view_model, on_add)

#     db.connect()
#     db.create_tables([FlashCardModel])
#     repo = PeeweeCardRepository()

#     study_vm = StudyViewModel(repo)
#     add_vm = AddCardViewModel(repo)

#     def show_study():
#         page.clean()
#         study_view(page, study_vm, on_add_button_click)

#     def show_add():
#         page.clean()
#         add_card_view(page, add_vm, show_study)

#     def on_add_button_click():
#         show_add()

#     show_study()

if __name__ == "__main__":
    ft.run(main)