# Generated by Django 4.1.7 on 2023-04-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailytask',
            name='date',
            field=models.DateField(default='2000-10-22'),
            preserve_default=False,
        ),
    ]