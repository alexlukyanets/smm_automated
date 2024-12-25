from instagrapi.types import Media

from config import settings
from logger import logger

from core.insta_client.client import InstaClient

COUNT_POSTS: int = 3


async def leave_comments():
    client: InstaClient = InstaClient()
    user: User = client.user_info_by_username(settings.COMMENT_USERNAME)
    user_id: str = user.pk

    posts: list[Media] = client.user_medias(user_id, amount=COUNT_POSTS)
    for post in posts:
        client.media_comment(post.id, 'Nice one!')
    logger.info(f'User: {user}')
