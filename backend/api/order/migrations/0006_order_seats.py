# Generated by Django 3.1.7 on 2023-06-14 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20230613_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='seats',
            field=models.ManyToManyField(blank=True, null=True, related_name='seatbook', to='order.seats'),
        ),
    ]