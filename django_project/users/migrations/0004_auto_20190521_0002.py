# Generated by Django 2.2.1 on 2019-05-20 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]