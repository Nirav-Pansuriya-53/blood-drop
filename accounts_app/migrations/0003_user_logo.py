# Generated by Django 4.1.7 on 2023-04-15 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0002_user_is_bloodbank'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='bloodbank_logo/'),
        ),
    ]