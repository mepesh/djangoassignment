# Generated by Django 3.0.8 on 2020-07-23 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.Author'),
        ),
    ]
