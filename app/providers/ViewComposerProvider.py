"""A ViewComposerProvider Service Provider."""

from masonite.provider import ServiceProvider
from masonite.view import View
from masonite.helpers import config

class ViewComposerProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        pass

    def boot(self, view: View):
        view.share(
            {
                "len": len,
            }
        )
