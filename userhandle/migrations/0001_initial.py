# Generated by Django 4.1.7 on 2023-03-30 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=6)),
                ('company_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
