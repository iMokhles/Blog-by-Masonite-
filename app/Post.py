"""Post Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to

class Post(Model):
    """Post Model."""
    __table__ = 'posts'

    __fillable__ = ['title', 'author_id', 'body']

    @belongs_to('author_id', 'id')
    def author(self):
        from app.User import User
        return User