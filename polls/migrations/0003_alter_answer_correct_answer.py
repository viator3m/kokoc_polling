# Generated by Django 4.1.7 on 2023-03-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correct_answer',
            field=models.BooleanField(default=False, verbose_name='Правильный'),
        ),
    ]
