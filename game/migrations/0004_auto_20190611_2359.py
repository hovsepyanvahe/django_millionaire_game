# Generated by Django 2.2 on 2019-06-11 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20190611_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='weight',
            field=models.CharField(choices=[(5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20)], max_length=2),
        ),
    ]
