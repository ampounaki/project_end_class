# Generated by Django 4.2.5 on 2023-09-08 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Karbaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('family', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]
