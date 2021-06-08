# Generated by Django 3.2.3 on 2021-06-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0003_auto_20210531_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=25),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('contacted', 'Contacted'), ('inprogress', 'Inprogress'), ('lost', 'Lost'), ('won', 'Won')], default='new', max_length=25),
        ),
    ]
