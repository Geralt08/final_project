# Generated by Django 2.2.1 on 2019-06-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PgeAuction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_number', models.CharField(max_length=16)),
                ('auction_title', models.CharField(max_length=400)),
                ('auction_date_publish', models.CharField(max_length=16)),
                ('auction_date_put', models.CharField(max_length=16)),
                ('auction_date_open', models.CharField(max_length=16)),
            ],
        ),
    ]
