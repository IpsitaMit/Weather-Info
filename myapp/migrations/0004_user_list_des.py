# Generated by Django 4.1.7 on 2023-11-02 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_login_user_list_delete_credentials'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_list',
            name='des',
            field=models.CharField(default='ull', max_length=10),
        ),
    ]
