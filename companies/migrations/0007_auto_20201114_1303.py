# Generated by Django 3.1.3 on 2020-11-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_auto_20201114_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
