# Generated by Django 3.2.8 on 2021-11-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0009_alter_material_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='isvalid',
            field=models.IntegerField(choices=[(0, '无效'), (1, '有效')], default=1, null=True),
        ),
    ]