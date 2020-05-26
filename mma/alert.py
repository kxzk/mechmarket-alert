from .reddit import MechMarket
from .sms import SMS
from .config import reddit_config, twilio_config


class MechMarketAlert:
    def __init__(
        self, keyword: str, twilio_number: str, your_number: str, alert_size: int = 10,
    ):
        self.keyword = keyword
        self.twilio_number = twilio_number
        self.your_number = your_number

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
                and self.keyword.upper() in post.title.upper()
                and post.title not in self.sent_alerts
            ):
                message = f"FOUND - {self.keyword.upper()}: {post.url}"
                self.sms.send_text(self.your_number, self.twilio_number, message)
                self.sent_alerts.append(post.title)
