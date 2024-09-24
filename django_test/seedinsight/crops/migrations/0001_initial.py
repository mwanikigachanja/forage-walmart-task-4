# Generated by Django 5.1.1 on 2024-09-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(max_length=100)),
                ('variety', models.CharField(max_length=100)),
                ('altitude_zone', models.CharField(max_length=100)),
                ('maturity', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=50)),
                ('yield_per_acre', models.CharField(max_length=50)),
                ('attributes', models.TextField()),
            ],
        ),
    ]
