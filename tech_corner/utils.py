import datetime

from django.utils import timezone


def shortnaturaltime(value: datetime.datetime) -> str:
    """Convert a datetime value into a short, human-readable format."""
    now = timezone.now()
    delta = now - value

    if delta < datetime.timedelta(minutes=1):
        return 'just now'
    elif delta < datetime.timedelta(hours=1):
        return f'{int(delta.total_seconds() // 60)}m'
    elif delta < datetime.timedelta(days=1):
        return f'{int(delta.total_seconds() // 3600)}h'
    return f'{delta.days}d'
