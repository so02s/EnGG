from abc import ABC, abstractmethod
from datetime import date
from typing import Optional, List
from domain import FlashCard

class FlashCardRepository(ABC):
    @abstractmethod
    def add(self, card: FlashCard) -> FlashCard:
        """Добавить новую карточку, вернуть с заполненным id"""
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[FlashCard]:
        """Вытащить карточку по id"""
        pass

    @abstractmethod
    def get_due(self, today: date) -> List[FlashCard]:
        """Вернуть все карточки, которые нужно повторить сегодня"""
        pass

    @abstractmethod
    def update(self, card: FlashCard) -> None:
        """Обновить существующую карточку"""
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        """Удалить карточку по id"""
        pass