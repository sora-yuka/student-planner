# Generated by Django 5.1.1 on 2024-10-03 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_options_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
