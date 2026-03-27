import flet as ft
from datasource import PeeweeCardRepository
from web import study_view, add_card_view, StudyViewModel, AddCardViewModel
from datasource.database import db
from datasource.model.peewee_models import FlashCardModel

def main(page: ft.Page):
    page.title = "English Flashcards"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Инициализация БД и зависимостей
    db.connect()
    db.create_tables([FlashCardModel])
    repo = PeeweeCardRepository()

    # Общие ViewModel (создаются один раз)
    study_vm = StudyViewModel(repo)
    add_vm = AddCardViewModel(repo)

    def show_study():
        page.clean()
        study_view(page, study_vm, on_add_button_click)

    def show_add():
        page.clean()
        add_card_view(page, add_vm, show_study)

    def on_add_button_click():
        show_add()

    show_study()

if __name__ == "__main__":
    ft.app(target=main)