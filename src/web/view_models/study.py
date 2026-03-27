# src/viewmodels/study_viewmodel.py
from datetime import date
from typing import Optional
from datasource import PeeweeCardRepository
from domain import FlashCard, Rating

class StudyViewModel:
    def __init__(self, repo: PeeweeCardRepository):
        self.repo = repo
        self.current_card: Optional[FlashCard] = None
        self._load_due_card()

    def _load_due_card(self):
        due_cards = self.repo.get_due(date.today())
        self.current_card = due_cards[0] if due_cards else None

    def has_card(self) -> bool:
        return self.current_card is not None

    def get_current_card(self) -> Optional[FlashCard]:
        return self.current_card

    def answer(self, rating: Rating):
        if self.current_card:
            self.current_card.answer(rating, date.today())
            self.repo.update(self.current_card)
            self._load_due_card()