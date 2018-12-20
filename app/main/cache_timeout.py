# cache_timeout.py

from functools import wraps
from datetime import datetime, date


def _is_period_now(begin, end, **kwargs):
    """
    Utility method. Determines if the current moment falls within the given
    time period. Works with periods that fall over two days e.g. 10pm - 6am.

    :param begin: time period begins in isoformat 'HH:MM:SS'
    :param end: time period ends in isoformat 'HH:MM:SS'
    :return: True if current moment falls between period_begins and period_ends
    """

    # This makes the function testable as you can pass in your desired 'now'
    # as a datetime.
    if 'now' in kwargs:
        now = kwargs.get('now')
    else:
        now = datetime.utcnow()

    today = date.today().isoformat()
    begins_today = datetime.fromisoformat(f'{today} {begin}')
    ends_today = datetime.fromisoformat(f'{today} {end}')

    return (begins_today > ends_today and
            (now < ends_today or now > begins_today)) \
           or (now > begins_today and now < ends_today)


def modify(timeout=0, begin='00:01:00', end='06:00:00'):
    """
    Use to wrap Flask-Caching @cache.cached decorator. Modifies the cache
    timeout during the specified period every day. At other times, the cache
    timeout will revert to whatever is default or is specified on the
    @cache.cached decorator. Example use case: set a longer timeout at night to
    save unnecessary API calls when people are asleep.

    Example::

    @cache_timeout.modify(timeout=3600, # 1 hour
                           begin='22:00:00', # 10pm
                           end='06:00:00') # 6am
    @cache.cached(timeout=60) # 1 minute
    def myFunc():
        # function body

    :param timeout: cache timeout period in seconds
    :param begin: time period begins in isoformat 'HH:MM:SS'
    :param end: time period ends in isoformat 'HH:MM:SS'
    :return: cached function with modified timeout
    """

    def decorated_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            if (_is_period_now(begin, end)):
                func.cache_timeout = timeout

            return func(*args, **kwargs)

        return wrapper

    return decorated_function
