# Generated by Django 5.0.6 on 2024-07-18 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carinventory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarInventory',
        ),
    ]
