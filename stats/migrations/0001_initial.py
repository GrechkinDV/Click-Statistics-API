# Generated by Django 3.2.8 on 2021-10-21 12:57

import django.core.validators
from django.db import migrations, models
import stats.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClickStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('views', models.PositiveIntegerField()),
                ('clicks', models.PositiveIntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=8)])),
                ('cpc', models.DecimalField(decimal_places=4, max_digits=6)),
                ('cpm', models.DecimalField(decimal_places=4, max_digits=6)),
            ],
            options={
                'ordering': ['date'],
            },
            managers=[
                ('objects', stats.models.ClickStatisticManager()),
            ],
        ),
    ]
