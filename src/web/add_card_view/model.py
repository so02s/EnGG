from domain import FlashCard, Word, Lang, SMData
from datasource import PeeweeCardRepository

class AddCardViewModel:
    def __init__(self, repo: PeeweeCardRepository):
        self.repo = repo
        self.word_value = ""
        self.translation_value = ""
        self.topic = ""

    def add_card(self) -> bool:
        if not self.word_value.strip() or not self.translation_value.strip():
            return False

        card = FlashCard(
            word=Word(value=self.word_value.strip(), lang=Lang.ENG),
            translation=Word(value=self.translation_value.strip(), lang=Lang.RU),
            topic=self.topic.strip() or None,
            sm=SMData()
        )
        self.repo.add(card)
        return True