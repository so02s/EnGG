from abc import ABC, abstractmethod
from domain.model.flashcard import FlashCard, Word, Rating
from datetime import date
from typing import Optional, List

class FlashcardUseCase(ABC):
    @abstractmethod
    def create(word: Word, translation: Word, topic: Optional[str], example: Optional[str]) -> FlashCard:
        pass

    @abstractmethod
    def update(card: FlashCard) -> FlashCard:
        pass

    @abstractmethod
    def delete(cardId: int) -> None:
        pass

    @abstractmethod
    def getDueCards(today: date) -> List[FlashCard]:
        pass
    
    @abstractmethod
    def answerCard(cardId: int, rating: Rating, today: date) -> FlashCard:
        pass