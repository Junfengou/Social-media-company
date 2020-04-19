from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'

    # Don't touch this.
    # This is from signal.py, it part of the system where it generate a profile for new user upon creating a new account
    def ready(self):
        import account.signal