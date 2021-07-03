# Generated by Django 3.2.4 on 2021-06-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20210628_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Типы актеров и режисеров',
                'verbose_name_plural': 'Типы актеров и режисеров',
            },
        ),
    ]
