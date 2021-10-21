from decimal import DivisionByZero
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.core.validators import DecimalValidator

from rest_framework.serializers import ValidationError


class ClickStatisticManager(BaseUserManager):
    """ Manager for click statistic """
    use_in_migrations = True

    def create_click_statistic(
            self,
            views,
            clicks,
            cost):
        """
        Create ClickStatistic object
        """
        # Check that fields are set
        try:
            cpc = round(cost / clicks, 4)
            cpm = round(cost / clicks * 1000, 4)
        except DivisionByZero:
            raise ValidationError(f"The number of clicks can't be 0!", 400)

        for key, value in {
            "views": views,
            "clicks": clicks,
            "cost": cost,
        }.items():
            if not value:
                raise ValidationError(f"The {key} must be set", 400)

        obj = ClickStatistic.objects.create(
            views=views,
            clicks=clicks,
            cost=cost,
            cpc=cpc,
            cpm=cpm,
        )

        return obj


class ClickStatistic(models.Model):
    """
    Model for statistics of clicks
    param date: date of action
    type date: DateTime
    param views: amount of views
    type views: integer
    param clicks: amount of clicks
    type clicks: integer
    param cost: cost of a click
    type cost: decimal field representing ruble currency 
    param cpc: cost per click
    type cpc: decimal field representing ruble currency 
    param cpm: cost per thousand
    type cpm: decimal field representing ruble currency 
    """

    date = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField()
    clicks = models.PositiveIntegerField()
    cost = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[DecimalValidator(max_digits=8, decimal_places=2)])
    cpc = models.DecimalField(max_digits=6, decimal_places=4)
    cpm = models.DecimalField(max_digits=6, decimal_places=4)

    class Meta:
        ordering = ["date"]

    objects = ClickStatisticManager()
