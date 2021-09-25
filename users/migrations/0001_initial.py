# Generated by Django 3.1.7 on 2021-09-21 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(blank=True, max_length=300)),
                ('profile_pic', models.ImageField(blank=True, upload_to='static/profile_pics')),
                ('friends', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('auther', models.CharField(max_length=125)),
                ('mode', models.CharField(default='public', max_length=11)),
                ('tag', models.CharField(max_length=75)),
                ('book_cover', models.ImageField(blank=True, upload_to='static/book_cover')),
                ('description', models.CharField(blank=True, max_length=500)),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.useraccount')),
            ],
        ),
    ]