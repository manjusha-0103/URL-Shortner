# Generated by Django 4.0.4 on 2022-09-02 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0002_shorturlmanager_short_active_alter_short_shortcode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShortURLManager',
        ),
    ]
