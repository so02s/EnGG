from typing import Optional, List
from datetime import date

from peewee import fn
from .interface import FlashCardRepository
from ..mapper.flashcard_mapper import FlashCardMapper
from ..model.peewee_models import FlashCardModel
from domain import FlashCard

class PeeweeCardRepository(FlashCardRepository):
    def __init__(self, model=None, mapper=None):
        """
        :param model: класс ORM-модели (по умолчанию FlashCardModel)
        :param mapper: экземпляр маппера (по умолчанию FlashCardMapper())
        """
        self.model = model or FlashCardModel
        self.mapper = mapper or FlashCardMapper()

    def add(self, card: FlashCard) -> FlashCard:
        """
        Сохраняет новую карточку и возвращает её с заполненным id
        """
        data = self.mapper.to_model(card)
        with self.model._meta.database.atomic():
            instance = self.model.create(**data)
            card.id = instance.id
        return card

    def get_by_id(self, id: int) -> Optional[FlashCard]:
        """
        Возвращает карточку по id
        """
        try:
            instance = self.model.get_by_id(id)
        except self.model.DoesNotExist:
            return None
        return self.mapper.to_domain(instance)

    def get_due(self, today: date) -> List[FlashCard]:
        """
        Возвращает карточки, которые нужно повторить сегодня
        """
        due_models = self.model.select().where(
            (self.model.last_review.is_null()) |
            (fn.date(self.model.last_review, "+' || self.model.interval || ' days") <= today)
        )
        return [self.mapper.to_domain(m) for m in due_models]

    def update(self, card: FlashCard) -> None:
        """
        Обновляет существующую карточку
        """
        data = self.mapper.to_model(card)
        with self.model._meta.database.atomic():
            self.model.update(data).where(self.model.id == card.id).execute()

    def delete(self, id: int) -> None:
        """
        Удаляет карточку по id
        """
        with self.model._meta.database.atomic():
            self.model.delete_by_id(id)