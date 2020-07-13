from fastapi_admin.models import User as AbstractUser
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class User(AbstractUser):
    """Модель Пользователя."""

    id = fields.IntField(pk=True)
    is_active = fields.BooleanField(default=True, description="Is Active")
    is_superuser = fields.BooleanField(default=False, description="Is SuperUser")
    avatar = fields.CharField(max_length=200, default="")
    intro = fields.TextField(default="")
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}#{self.username}"

    class Meta:
        table = "users"


User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
