from peewee import Model, CharField, IntegerField, FloatField, DateField
from ..database import db

class BaseModel(Model):
    class Meta:
        database = db

class FlashCardModel(BaseModel):
    front = CharField(max_length=255)
    back = CharField(max_length=255)
    topic = CharField(null=True)
    repetitions = IntegerField(default=0)
    interval = IntegerField(default=1)
    ease_factor = FloatField(default=2.5)
    last_review = DateField(null=True)