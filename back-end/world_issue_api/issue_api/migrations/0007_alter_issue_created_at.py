# Generated by Django 4.2.3 on 2023-07-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_api', '0006_alter_issue_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
