"""
Fixtures for Unit tests of stats
"""

import pytest

from stats.models import ClickStatistic

pytestmark = pytest.mark.django_db  # pylint:disable=invalid-name


@pytest.fixture
def click_stats_1():
    """ Create a dummy stats """
    infos = {
        "views": 10,
        "clicks": 35,
        "cost": 0.50,
    }
    object = ClickStatistic.objects.create_click_statistic(**infos)
    infos["model"] = object
    return infos


@pytest.fixture
def click_stats_2():
    """ Create a dummy stats """
    infos = {
        "views": 121,
        "clicks": 175,
        "cost": 0.32,
    }
    object = ClickStatistic.objects.create_click_statistic(**infos)
    infos["model"] = object
    return infos
