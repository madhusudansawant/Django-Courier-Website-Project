# Generated by Django 4.1.2 on 2022-10-12 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MumbaiExpress', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginmodel',
            old_name='usern',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='signupmodel',
            old_name='usern',
            new_name='username',
        ),
    ]
