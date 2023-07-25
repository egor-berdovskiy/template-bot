from tortoise import Model
from tortoise import fields
from .dataclasses import UserType

class User(Model):
    id = fields.IntField(pk=True)

    type = fields.CharField(max_length=32, default=UserType.user, validators=[UserType.validator])

    user_id = fields.BigIntField(unique=True)
    fullname = fields.CharField(max_length=64)
    username = fields.CharField(max_length=32, null=True)
    language = fields.CharField(max_length=2, default='ru')

    referral_balance = fields.FloatField(default=0)
    referral = fields.ForeignKeyField('models.User', null=True)

    register_time = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'users'

    @property
    def is_admin(self):
        return self.type == 'admin'
