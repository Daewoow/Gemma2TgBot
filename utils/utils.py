from datetime import datetime
import pytz


def get_now_time():
    now = datetime.now(pytz.timezone('Europe/Moscow'))
    return now.replace(tzinfo=None)