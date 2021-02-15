"""User Model."""

from masoniteorm.models import Model


class User(Model):
    """User Model."""

    __fillable__ = ["name", "email", "password", "is_admin"]

    __auth__ = "email"
