# Generated by Django 2.1.2 on 2018-10-14 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blibliopy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestar',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
    ]
