# Generated by Django 3.1.7 on 2021-03-27 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0006_block_rejected'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrevHash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(max_length=1000000)),
            ],
        ),
    ]
