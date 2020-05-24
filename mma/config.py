import os

reddit_config = {
    "client_id": os.getenv("client_id"),
    "client_secret": os.getenv("client_secret"),
    "user_agent": os.getenv("user_agent"),
    "username": os.getenv("username"),
    "password": os.getenv("password"),
}

twilio_config = {
    "account_sid": os.getenv("account_sid"),
    "auth_token": os.getenv("auth_token"),
}
