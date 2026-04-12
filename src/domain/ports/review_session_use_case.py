from abc import ABC, abstractmethod


class ReviewSessionUseCase(ABC):
    def startSession(today: date) -> ReviewSession:
        pass

    def answer(currentCard: FlashCard, rating: Rating) -> NextCard:
        pass