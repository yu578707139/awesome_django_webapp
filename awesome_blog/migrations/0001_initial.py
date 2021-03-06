# Generated by Django 2.1.3 on 2018-11-30 07:01

from django.db import migrations, models
import time


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.CharField(default='0015435613035935360b03a54e1449985dc0a7acb1d0308000', max_length=32, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=32)),
                ('title', models.TextField(max_length=50)),
                ('summary', models.TextField(max_length=100)),
                ('content', models.TextField(max_length=500)),
                ('gmt_created', models.DateTimeField(default=time.time)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(default='001543561303594bd4d007043d34292889929d1804f1138000', max_length=32, primary_key=True, serialize=False)),
                ('blog_id', models.CharField(max_length=32)),
                ('user_id', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=32)),
                ('content', models.TextField(max_length=500)),
                ('gmt_created', models.DateTimeField(default=time.time)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(default='0015435613035937466884121ae42e2ac763bb9a03024f5000', max_length=32, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('gmt_created', models.DateTimeField(default=time.time)),
            ],
        ),
    ]
