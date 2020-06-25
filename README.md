# r/MechMarket Alert

> Why? Make getting (insert GMK keycaps, RAMA board, etc...) easier.

![banner](https://i.imgur.com/29A3SZS.png)

![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?style=flat-square) [![](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/) [![Build Status](https://travis-ci.org/kadekillary/mechmarket-alert.svg?branch=master)](https://travis-ci.org/kadekillary/mechmarket-alert) [![codecov](https://codecov.io/gh/kadekillary/mechmarket-alert/branch/master/graph/badge.svg)](https://codecov.io/gh/kadekillary/mechmarket-alert)

## Example Usage

```python
import time

from mma import MechMarketAlert

items = {"GMK Camping", "GMK Striker"}

mma = MechMarketAlert(items, "+12073948899", "+14244780093")

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

* Need to create the following environment variables (below are just
    examples):

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
