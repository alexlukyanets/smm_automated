from instagrapi import Client

from config import settings


class InstaClient(Client):
    def __init__(self):
        super().__init__()
        self.login(username=settings.USERNAME, password=settings.USERNAME)

    def do_login(self, username: str, password: str) -> None:
        try:
            self.login(username=username, password=password)
        except Exception as e:
            raise ValueError(f'Failed to login: {e!r}')
