# Generated by Django 2.2.7 on 2019-12-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrservice', '0002_auto_20191206_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRcodeManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
