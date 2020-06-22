from typing import List, Optional, Set

from .config import reddit_config, twilio_config
from .helpers import contains_any
from .reddit import MechMarket
from .sms import SMS


class MechMarketAlert:
    def __init__(
        self,
        keywords: Set[str],
        twilio_number: str,
        my_number: str,
        alert_size: int = 10,
    ):
        self.keywords = keywords
        self.twilio_number = twilio_number
        self.my_number = my_number

        self.mech_market = MechMarket(**reddit_config)
        self.sms = SMS(**twilio_config)

        self.alert_size = alert_size
        self.sent_alerts = []

    def __check_alerts_size(self) -> None:
        if len(self.sent_alerts) > self.alert_size:
            self.sent_alerts = self.sent_alerts[-self.alert_size :]

    def get_lucky(self, number_of_posts: int = 20) -> None:
        self.__check_alerts_size()
        posts = self.mech_market.new_posts(number_of_posts)
        for post in posts:
            if (
                post.link_flair_text == "Selling"
                and contains_any(post.title, self.keywords)
                and post.title not in self.sent_alerts
            ):
                message = f"FOUND ITEM - {post.url}"
                print(message)
                self.sms.send_text(self.my_number, self.twilio_number, message)
                self.sent_alerts.append(post.title)
