# Generated by Django 3.0.5 on 2020-08-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ielts', '0017_auto_20200824_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commontaskoneacademic',
            name='uid',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='commontaskonegeneral',
            name='uid',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='commontasktwo',
            name='uid',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
