# Generated by Django 5.0.7 on 2024-09-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0014_filemodel_button_text_filemodel_button_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='is_contact_file',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
