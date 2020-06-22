from typing import Generator

import pytest
from praw.models.reddit.subreddit import Subreddit

from mma.reddit import MechMarket
from mma.config import reddit_config


@pytest.fixture
def mechmarket():
    return MechMarket(**reddit_config)


def test_mech_market(mechmarket):
    assert type(mechmarket.subreddit) == Subreddit
    assert mechmarket.subreddit.url == "/r/mechmarket/"


def test_new_posts_number(mechmarket):
    posts = list(mechmarket.new_posts(10))
    assert len(posts) == 10


def test_new_posts_type(mechmarket):
    posts = mechmarket.new_posts(2)
    assert isinstance(posts, Generator)
