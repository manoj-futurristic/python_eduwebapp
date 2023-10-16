# Generated by Django 4.2.6 on 2023-10-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('type', models.SlugField(unique=True)),
                ('is_hide', models.BooleanField(default=False)),
                ('categgory_image', models.ImageField(blank=True, default='placeholders/placeholder.jpg', null=True, upload_to='category-images', verbose_name='Category Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Joined')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
