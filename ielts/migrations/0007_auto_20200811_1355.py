# Generated by Django 3.0.5 on 2020-08-11 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ielts', '0006_auto_20200811_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='answertaskone',
            name='checked_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='answertaskone',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answertasktwo',
            name='checked_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='answertasktwo',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
