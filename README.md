# r/MechMarket Alert

> Why? Make getting (insert GMK keycaps, RAMA board, etc...) easier.

![banner](https://images.squarespace-cdn.com/content/v1/563c788ae4b099120ae219e2/1521460872680-FVPBLJYICSA4W4ZQ0M50/ke17ZwdGBToddI8pDm48kJRqFJ19D4P4EwsC9z3fiewUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYy7Mythp_T-mtop-vrsUOmeInPi9iDjx9w8K4ZfjXt2dkV64dCjSK7Zaaf7dwPYPO_gHf_vjqrS5WJoq1nmwotrP7cJNZlDXbgJNE9ef52e8w/RAMA-M60-A-03.658.jpg)

## Example Usage

```python
import time

from mma import MechMarketAlert

mma = MechMarketAlert("GMK Striker", "+12073948899", "+14244780093")

while True:
    try:
        mma.get_lucky()
        time.sleep(60)
    except Exception as e:
        print(e)
```

## Setup

* Create a Reddit Application - [example](https://www.storybench.org/how-to-scrape-reddit-with-python/)
* Create a Twilio Application - [example](https://www.twilio.com/docs/sms/quickstart/python)
    - Twilio free trial gives you $15
    - Each text costs about a cent

* Need to create the following environment variables:

```bash
# Reddit
export client_id=DJ-9095+DF90
export client_secret=98f9s08d00sd8f90s90df
export user_agent=mechmarket-alert
export username=reddit_account
export password=reddit_password

# Twilio
export account_sid=AD8908DGNUEKW798798
export auth_token=d8f9s008d9f8s76f7sd
```
