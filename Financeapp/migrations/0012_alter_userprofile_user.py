# Generated by Django 4.2.3 on 2023-07-30 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Financeapp', '0011_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
