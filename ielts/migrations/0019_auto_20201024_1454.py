# Generated by Django 3.0.5 on 2020-10-24 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ielts', '0018_auto_20200824_2010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answertaskoneacademic',
            options={'ordering': ['timestamp']},
        ),
        migrations.AlterModelOptions(
            name='answertaskonegeneral',
            options={'ordering': ['timestamp']},
        ),
        migrations.AlterModelOptions(
            name='answertasktwo',
            options={'ordering': ['timestamp']},
        ),
    ]