from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from twilio.rest.api.v2010.account.message import MessageInstance


class SMS:
    def __init__(self, account_sid: str, auth_token: str):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(self.account_sid, self.auth_token)

    def send_text(
        self, to_number: str, from_number: str, message: str
    ) -> MessageInstance:
        try:
            message = self.client.messages.create(
                to=to_number, from_=from_number, body=message
            )
            return message
        except TwilioRestException as e:
            print(e)
