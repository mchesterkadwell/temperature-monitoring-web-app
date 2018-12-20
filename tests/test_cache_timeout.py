from datetime import datetime

import pytest

from app.main import cache_timeout


def test_night_period_over_midnight_is_now():
    result = cache_timeout._is_period_now('22:00:00', '06:00:00',
                                          now=datetime(2018, 12, 19,
                                                      22, 5, 00, 0))
    assert result == True


def test_day_period_is_now():
    result = cache_timeout._is_period_now('07:00:00', '13:00:00',
                                          now=datetime(2018, 12, 19,
                                                      10, 5, 00, 0))
    assert result == True


def test_night_period_over_midnight_is_not_now():
    result = cache_timeout._is_period_now('22:00:00', '06:00:00',
                                          now=datetime(2018, 12, 19,
                                                      14, 5, 00, 0))
    assert result == False


def test_day_period_is_before_now():
    result = cache_timeout._is_period_now('07:00:00', '13:00:00',
                                          now=datetime(2018, 12, 19,
                                                      14, 5, 00, 0))
    assert result == False


def test_day_period_is_after_now():
    result = cache_timeout._is_period_now('07:00:00', '13:00:00',
                                          now=datetime(2018, 12, 19,
                                                      6, 5, 00, 0))
    assert result == False


def test_period_begins_non_iso_format():
    with pytest.raises(ValueError):
        cache_timeout._is_period_now('070000', '13:00:00',
                                     now=datetime(2018, 12, 19,
                                                 6, 5, 00, 0))
