# Generated by Django 3.1.2 on 2021-01-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201026_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='shortened_link',
            field=models.URLField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
