# Generated by Django 2.1.4 on 2019-01-09 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181226_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Gender',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='IEP_or_504_Plan',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='Race',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='Sex',
            field=models.CharField(default='', max_length=12),
        ),
    ]
