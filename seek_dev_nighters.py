from pytz import timezone
from datetime import datetime
import requests

API_URL = 'https://devman.org/api/challenges/solution_attempts/'


def get_local_datetime(timestamp, str_time_zone):
    my_time_zone = timezone(str_time_zone)
    loc_dt = my_time_zone.localize(datetime.fromtimestamp(timestamp))
    return loc_dt


def is_owl_time(loc_dt):
    if loc_dt is None:
        return False
    midnight = datetime(loc_dt.year, loc_dt.month, loc_dt.day, 0, 0, 0)
    time = datetime(loc_dt.year, loc_dt.month, loc_dt.day, loc_dt.hour, loc_dt.minute, loc_dt.second)
    six_am = datetime(loc_dt.year, loc_dt.month, loc_dt.day, 6, 0, 0)
    if midnight < time < six_am:
        return True
    return False


def load_attempts():
    page, pages = (1, 1)
    while page < pages+1:
        params = {
            'page': page
        }
        json_response = requests.get(API_URL, params=params).json()
        pages = json_response['number_of_pages']
        for record in json_response['records']:
            if record['timestamp'] is None:
                continue
            yield record
        page += 1


def get_midnighter(record):
    str_timestamp = record['timestamp']
    time_zone = record['timezone']
    loc_dt = get_local_datetime(float(str_timestamp), time_zone)
    if is_owl_time(loc_dt):
        return record['username']
    return None


def get_midnighters():
    midnighters = set(
        get_midnighter(record) for record in load_attempts()
    )
    midnighters.discard(None)
    return midnighters


if __name__ == '__main__':
    owls = get_midnighters()
    print("DEVMAN'S owls list:")
    for num, owl in enumerate(owls, start=1):
        print('{}. {}'.format(num, owl))