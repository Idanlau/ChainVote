# Generated by Django 3.1.7 on 2021-03-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0005_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='rejected',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
