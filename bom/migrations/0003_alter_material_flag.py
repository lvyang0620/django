# Generated by Django 3.2.8 on 2021-11-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0002_auto_20211120_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='flag',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
