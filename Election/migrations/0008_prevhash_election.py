# Generated by Django 3.1.7 on 2021-03-27 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0007_prevhash'),
    ]

    operations = [
        migrations.AddField(
            model_name='prevhash',
            name='election',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Election.election'),
        ),
    ]