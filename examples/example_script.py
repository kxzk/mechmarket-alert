import time
import logging

from mma import MechMarketAlert

logging.basicConfig(filename="mma.log")

items = {"GMK Striker", "GMK Camping"}

mma = MechMarketAlert(items, twilio_number="+12077428434", my_number="+14245274419")

while True:
    try:
        mma.get_lucky()
        time.sleep(60)
    except Exception as e:
        logging.exception(e)
