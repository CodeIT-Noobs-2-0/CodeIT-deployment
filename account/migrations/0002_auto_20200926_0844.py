# Generated by Django 3.1.1 on 2020-09-26 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo_admin',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='DOB'),
        ),
    ]