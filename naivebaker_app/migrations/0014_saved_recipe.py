# Generated by Django 4.2.6 on 2023-11-09 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('naivebaker_app', '0013_recipe_category_recipe_meal_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='saved_recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('ingredients', models.TextField()),
                ('cookinstru', models.TextField()),
                ('image', models.TextField()),
                ('vegitarity', models.CharField(default='veg', max_length=8, null=True)),
                ('category', models.CharField(default='Indian', max_length=10, null=True)),
                ('meal_time', models.CharField(default='breakfast', max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
