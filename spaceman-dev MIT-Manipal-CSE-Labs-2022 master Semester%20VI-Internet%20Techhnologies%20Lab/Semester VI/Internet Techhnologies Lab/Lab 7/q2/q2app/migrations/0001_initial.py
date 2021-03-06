# Generated by Django 3.2 on 2021-05-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Street', models.CharField(max_length=500)),
                ('City', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Company', models.CharField(max_length=200)),
                ('Salary', models.IntegerField()),
            ],
        ),
    ]
