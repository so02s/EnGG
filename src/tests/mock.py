from datetime import date
from typing import List
from domain import FlashCard, Word, Lang, SMData

class MockCardRepository:
    """Заглушка репозитория для тестирования UI без реальной БД."""
    def __init__(self):
        self.cards: List[FlashCard] = []
        self._next_id = 1
        self._create_sample_cards()

    def _create_sample_cards(self):
        """Создаёт несколько тестовых карточек, все due на сегодня."""
        samples = [
            ("cat", "кот"),
            ("dog", "собака"),
            ("sun", "солнце"),
            ("moon", "луна"),
            ("apple", "яблоко"),
        ]
        for word_val, trans_val in samples:
            card = FlashCard(
                id=self._next_id,
                word=Word(value=word_val, lang=Lang.ENG),
                translation=Word(value=trans_val, lang=Lang.RU),
                sm=SMData(
                    repetitions=0,
                    interval=1,
                    ease_factor=2.5,
                    last_review=None,  # due today
                )
            )
            self.cards.append(card)
            self._next_id += 1

    def get_due(self, due_date: date) -> List[FlashCard]:
        """Возвращает карточки, которые должны быть повторены до указанной даты."""
        return [card for card in self.cards if card.is_due(due_date)]

    def update(self, card: FlashCard):
        """Обновляет карточку в хранилище (по id)."""
        for i, existing in enumerate(self.cards):
            if existing.id == card.id:
                self.cards[i] = card
                break