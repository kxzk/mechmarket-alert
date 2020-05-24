from praw import Reddit
from praw.models.reddit.submission import Submission

from typing import List


class MechMarket:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        user_agent: str,
        username: str,
        password: str,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.username = username
        self.password = password

        self.reddit = Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            username=username,
            password=password,
        )

        self.subreddit = self.reddit.subreddit("mechmarket")

    def new_posts(self, number_of_posts: int) -> List[Submission]:
        return [post for post in self.subreddit.new(limit=number_of_posts)]
