# Generated by Django 4.2.3 on 2023-07-30 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Financeapp', '0005_alter_userprofile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
