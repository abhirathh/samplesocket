# Generated by Django 4.0.3 on 2022-04-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chatLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=0, max_length=255)),
                ('user_chat', models.CharField(default=0, max_length=255)),
                ('system_chat', models.CharField(default=0, max_length=255)),
            ],
        ),
    ]