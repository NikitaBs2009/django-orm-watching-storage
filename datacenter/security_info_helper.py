from datetime import datetime, timezone
from django.utils.timezone import localtime


def is_visit_long(duration, minutes=60):

    seconds = minutes * minutes
    long_visit = duration.seconds>seconds
       
    return long_visit


def format_duration(duration):
    seconds = duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return  f'{hours}:{minutes}'


def get_duration(visit):
    entry_local_time = localtime(visit.entered_at)
    if visit.leaved_at==None:
        date_now = localtime(datetime.now(timezone.utc))
        delta = date_now - entry_local_time
    else:
        leaved_local_time = localtime(visit.leaved_at)
        delta = leaved_local_time - entry_local_time
    return delta