import time
import logging

from mma import MechMarketAlert

logging.basicConfig(filename="mma.log")

mma = MechMarketAlert("GMK Striker", "+12087478474", "+14248884419")

while True:
    try:
        mma.get_lucky()
        time.sleep(60)
    except Exception as e:
        logging.exception(e)
