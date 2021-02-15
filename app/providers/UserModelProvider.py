"""A UserModelProvider Service Provider."""

from masonite.provider import ServiceProvider
from events import Event
from app.events import (SetIsAdminForUsers)

class UserModelProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        pass

    def boot(self, event: Event):
        """Boots services required by the container."""
        # subscribe event
        event.subscribe(SetIsAdminForUsers)
