# Generated by Django 5.0.2 on 2024-02-11 17:54

import ckeditor.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_cat', models.CharField(max_length=60, unique=True)),
                ('blogcat_img', models.ImageField(upload_to='images/')),
                ('blogcat_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_email', models.EmailField(max_length=254)),
                ('u_message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubscribedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='blog_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=100)),
                ('cover_img', models.ImageField(upload_to='images/')),
                ('blog_description', ckeditor.fields.RichTextField(blank=True)),
                ('like_count', models.IntegerField(default=0, null=True)),
                ('view_count', models.IntegerField(default=0, null=True)),
                ('blog_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblogs.blog_category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myblogs.blog_post')),
            ],
        ),
    ]