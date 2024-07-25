# Generated by Django 5.0.7 on 2024-07-25 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='not available', max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='mark',
            field=models.IntegerField(default=0),
        ),
    ]
