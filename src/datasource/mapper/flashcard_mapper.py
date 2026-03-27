from ..model.peewee_models import FlashCardModel
from domain import FlashCard, Word, Lang, SMData

class FlashCardMapper:
    @staticmethod
    def to_domain(model: FlashCardModel) -> FlashCard:
        return FlashCard(
            id=model.id,
            word=Word(value=model.front, lang=Lang.ENG),
            translation=Word(value=model.back, lang=Lang.RU),
            topic=model.topic,
            sm=SMData(
                repetitions=model.repetitions,
                interval=model.interval,
                ease_factor=model.ease_factor,
                last_review=model.last_review,
            )
        )

    @staticmethod
    def to_model(card: FlashCard) -> dict:
        return {
            'front': card.word.value,
            'back': card.translation.value,
            'topic': card.topic,
            'repetitions': card.sm.repetitions,
            'interval': card.sm.interval,
            'ease_factor': card.sm.ease_factor,
            'last_review': card.sm.last_review,
        }