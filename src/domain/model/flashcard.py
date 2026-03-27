from dataclasses import dataclass
from typing import Optional
from enum import IntEnum
from datetime import date, timedelta

class Lang(IntEnum):
    RU = 1
    ENG = 2

class Rating(IntEnum):
    BAD = 0
    NEUTRAL = 1
    GOOD = 2

@dataclass
class Word:
    value: str
    lang: Lang = Lang.RU

@dataclass
class SMData:
    """
    Метод рассчета для запоминания
    """
    repetitions: int = 0
    interval: int = 1
    ease_factor: float = 2.5
    last_review: Optional[date] = None

    @property
    def calculated_next_review(self):
        if self.last_review:
            return self.last_review + timedelta(days=self.interval)
        return None
    
    def bad(self) -> None:
        self.repetitions = 0
        self.interval = 1
        self.ease_factor = max(1.3, self.ease_factor - 0.2)
    
    def neutral(self) -> None:
        self._correct_answer()
    
    def good(self) -> None:
        self._correct_answer()
        self.ease_factor = max(1.3, self.ease_factor + 0.1)
    
    def _correct_answer(self) -> None:
        if self.repetitions == 0:
            self.interval = 1
        elif self.repetitions == 1:
            self.interval = 6
        else:
            self.interval = round(self.interval * self.ease_factor)
        self.repetitions += 1

@dataclass
class FlashCard:
    """
    Модель карточки для хранения слов
    """
    id: Optional[int] = None
    word: Optional[Word] = None
    translation: Optional[Word] = None
    topic: Optional[str] = None
    sm: SMData = SMData()

    def answer(self, rating: Rating, today: Optional[date] = None) -> None:
        """
        Ответ на карточку пересчитывает её значения по SM-2
        """
        today = date.today() if today is None else today

        if rating == Rating.BAD:
            self.sm.bad()
        elif rating == Rating.NEUTRAL:
            self.sm.neutral()
        else:
            self.sm.good()

        self.sm.last_review = today

    def is_due(self, today: Optional[date] = None) -> bool:
        """
        Подошло ли время проверки карточки
        """
        if self.sm.last_review is None:
            return True
        today = date.today() if today is None else today
        return self.sm.calculated_next_review <= today