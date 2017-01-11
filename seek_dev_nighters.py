from pytz import timezone
from datetime import datetime, timedelta


def get_local_datetime(timestamp, str_time_zone):
    my_time_zone = timezone(str_time_zone)
    loc_dt = my_time_zone.localize(datetime.fromtimestamp(timestamp))
    return loc_dt


def is_owl_time(local_datetime):
    if 0 <= local_datetime.hour < 6:
        return True
    return False


def load_attempts():
    pages = 1
    for page in range(pages):
        # FIXME подключить загрузку данных из API
        yield {
            'username': 'bob',
            'timestamp': 0,
            'timezone': 'Europe/Moscow',
        }

def get_midnighters():
    pass

if __name__ == '__main__':
  pass
