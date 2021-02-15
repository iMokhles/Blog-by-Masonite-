""" A SetIsAdminForUsers Event """
from events import Event

class SetIsAdminForUsers(Event):
    """ SetIsAdminForUsers Event Class """

    subscribe = [
        'user.signedup'
    ]

    def __init__(self):
        """ Event Class Constructor """
        pass

    def handle(self):
        """ Event Handle Method """
        user = self.argument('user')
        isAdmin = self.argument('isAdmin')

        user.is_admin = isAdmin
        user.save()
