# Generated by Django 5.0.7 on 2024-08-05 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='icon_fa',
        ),
        migrations.AddField(
            model_name='skill',
            name='icon_svg',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Icon (svg code)'),
        ),
    ]
