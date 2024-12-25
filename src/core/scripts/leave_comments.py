from instagrapi.types import Media, User

from config import settings
from logger import logger

from core.insta_client import InstaClient

COUNT_POSTS: int = 3


async def leave_comments():
    client: InstaClient = InstaClient()
    user: User = client.user_info_by_username(settings.COMMENT_USERNAME)
    if not (posts := client.user_medias(user.pk, amount=COUNT_POSTS)):
        for post in posts:
            client.media_comment(post.id, 'Nice one!')
    logger.info(f'User: {user}')
