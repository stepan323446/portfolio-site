# Generated by Django 5.0.7 on 2024-09-18 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_rename_messagemodel_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('token', models.CharField(max_length=255)),
                ('chat_id', models.CharField(max_length=50)),
            ],
        ),
    ]
