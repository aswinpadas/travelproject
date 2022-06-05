# Generated by Django 4.0.4 on 2022-06-05 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('blog_img', models.ImageField(upload_to='pictures')),
                ('news_post_title', models.CharField(max_length=50)),
                ('news_post_category', models.CharField(max_length=30)),
                ('news_post_content', models.TextField()),
            ],
        ),
    ]
