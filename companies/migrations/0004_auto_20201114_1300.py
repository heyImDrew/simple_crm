# Generated by Django 3.1.3 on 2020-11-14 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_partnership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnership',
            name='type',
            field=models.CharField(choices=[('Коммерческое партнерство', 'Коммерческое партнерство'), ('Не коммерческое партнерство', 'Не коммерческое партнерство'), ('Ограниченное партнерство', 'Ограниченное партнерство'), ('Полное партнерство', 'Полное партнерство'), ('Стратегическое партнерство', 'Стратегическое партнерство')], max_length=255),
        ),
    ]
