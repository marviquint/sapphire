# Generated by Django 4.1.7 on 2023-04-03 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_users_is_active_users_is_staff_users_last_login_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='users',
            table='users_table',
        ),
    ]
