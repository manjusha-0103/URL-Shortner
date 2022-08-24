# Generated by Django 4.0.6 on 2022-07-31 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURLManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='short',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='short',
            name='shortcode',
            field=models.CharField(blank=True, default='mgk@', max_length=15, unique=True),
        ),
    ]