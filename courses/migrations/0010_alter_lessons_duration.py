# Generated by Django 3.2.8 on 2021-11-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_classes_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='duration',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
