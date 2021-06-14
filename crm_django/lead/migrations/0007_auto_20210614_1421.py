# Generated by Django 3.2.3 on 2021-06-14 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lead', '0006_auto_20210609_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignedleads', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('medium', 'Medium'), ('high', 'High'), ('low', 'Low')], default='medium', max_length=25),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('contacted', 'Contacted'), ('new', 'New'), ('inprogress', 'Inprogress'), ('lost', 'Lost'), ('won', 'Won')], default='new', max_length=25),
        ),
    ]
