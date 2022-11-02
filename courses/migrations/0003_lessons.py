# Generated by Django 3.2.8 on 2021-10-22 15:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_courses_teacher_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('duration', models.FloatField(validators=[django.core.validators.MinValueValidator(0.3), django.core.validators.MaxValueValidator(30.0)])),
                ('video_url', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.courses')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
