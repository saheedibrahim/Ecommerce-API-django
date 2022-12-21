# Generated by Django 4.1.4 on 2022-12-21 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_tag', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=13)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('imageURL', models.URLField()),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='djangoapi.category')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('isbn', models.CharField(max_length=13)),
                ('pages', models.IntegerField()),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('description', models.TextField()),
                ('imageURL', models.URLField()),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='djangoapi.category')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]