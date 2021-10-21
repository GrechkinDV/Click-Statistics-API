"""
Unit tests for stats
Test:
- Create
- list
- delete
"""
import pytest
from rest_framework.test import APIClient

from stats.tests.fixtures import click_stats_1, click_stats_2

pytestmark = pytest.mark.django_db  # pylint:disable=invalid-name


def test_create_stats():
    """
    Test stats creation
    Must success
    Must have the proper cpc cpm calculated values
    """
    client = APIClient()

    data1 = {
        "views": 10,
        "clicks": 35,
        "cost": 0.50,
    }

    response1 = client.post(
        "http://localhost:8000/api/click-statistic/",
        data1,
        format="json")

    # Check if values are as expected
    assert response1.status_code == 201
    assert response1.json()["views"] == 10
    assert response1.json()["clicks"] == 35
    assert response1.json()["cost"] == 0.50
    assert response1.json()["cpc"] == 0.0143
    assert response1.json()["cpm"] == 14.2857

    # Second check
    data2 = {
        "views": 121,
        "clicks": 175,
        "cost": 0.32,
    }

    response2 = client.post(
        "http://localhost:8000/api/click-statistic/",
        data2,
        format="json")

    # Check if values are as expected
    assert response2.status_code == 201
    assert response2.json()["views"] == 121
    assert response2.json()["clicks"] == 175
    assert response2.json()["cost"] == 0.32
    assert response2.json()["cpc"] == 0.0018
    assert response2.json()["cpm"] == 1.8286


def test_invalid_create_stats():
    """
    Test stats creation
    Must fail
    Must have inproper input values
    """
    client = APIClient()

    data1 = {
        "views": 10,
        "clicks": 0,
        "cost": 0.50,
    }

    response1 = client.post(
        "http://localhost:8000/api/click-statistic/",
        data1,
        format="json")

    # Check if values are as expected
    assert response1.status_code == 400

    data2 = {
        "clicks": 0,
        "cost": 0.50,
    }

    response2 = client.post(
        "http://localhost:8000/api/click-statistic/",
        data2,
        format="json")

    # Check if values are as expected
    assert response2.status_code == 400
    assert response2.json()["views"] == ['This field is required.']

    data3 = {
        "views": 20,
        "clicks": 10,
        "cost": 0.5055,
    }

    response3 = client.post(
        "http://localhost:8000/api/click-statistic/",
        data3,
        format="json")

    # Check if values are as expected
    assert response3.status_code == 400
    with open("file.txt", "a") as f:
        print(response3.json(), file=f)
    assert response3.json()["cost"] == \
        ['Ensure that there are no more than 2 decimal places.']


def test_list_stats(click_stats_1, click_stats_2):
    """
    Test stats list
    Must success
    Must have the proper time range
    """

    client = APIClient()
    from_date1 = "2021-10-21"
    to_date1 = "2021-10-31"

    response1 = client.get(
        f"http://localhost:8000/api/click-statistic/?from={from_date1}&to={to_date1}", format="json")

    assert response1.status_code == 200
    assert len(response1.json()) == 2

    from_date2 = "2020-10-21"
    to_date2 = "2020-10-31"

    response2 = client.get(
        f"http://localhost:8000/api/click-statistic/?from={from_date2}&to={to_date2}", format="json")

    assert response2.status_code == 200
    assert len(response2.json()) == 0


def test_invalid_list_stats():
    """
    Test stats list
    Must fail
    Must have the invalid time range
    """
    client = APIClient()

    from_date1 = "2021-10-35"
    to_date1 = "2021-10-30"

    response1 = client.get(
        f"http://localhost:8000/api/click-statistic/?from={from_date1}&to={to_date1}", format="json")

    assert response1.status_code == 400

    from_date2 = "2020-10-21"
    to_date2 = ""

    response2 = client.get(
        f"http://localhost:8000/api/click-statistic/?from={from_date2}&to={to_date2}", format="json")

    assert response2.status_code == 400


def test_delete_stats(click_stats_1):
    """
    Test stats delete
    Must succeed
    Must have proper credentials
    """

    client = APIClient()
    response1 = client.delete(
        f"http://localhost:8000/api/click-statistic/{click_stats_1['model'].id}/")

    assert response1.status_code == 204

    response2 = client.delete(
        f"http://localhost:8000/api/click-statistic/delete_all/")

    assert response2.status_code == 204


def test_invalid_delete_stats():
    """
    Test stats delete
    Must fail
    Must not have proper credentials
    """
    client = APIClient()
    response1 = client.delete(
        "http://localhost:8000/api/click-statistic/13131/")

    assert response1.status_code == 404
