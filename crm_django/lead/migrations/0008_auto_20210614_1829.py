# Generated by Django 3.2.3 on 2021-06-14 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0007_auto_20210614_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium')], default='medium', max_length=25),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('contacted', 'Contacted'), ('new', 'New'), ('lost', 'Lost'), ('won', 'Won'), ('inprogress', 'Inprogress')], default='new', max_length=25),
        ),
    ]
