# Generated by Django 4.2.6 on 2023-11-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naivebaker_app', '0015_rename_saved_recipe_save_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='save_recipe',
            old_name='category',
            new_name='cusinetype',
        ),
        migrations.RemoveField(
            model_name='save_recipe',
            name='cookinstru',
        ),
        migrations.RemoveField(
            model_name='save_recipe',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='save_recipe',
            name='vegitarity',
        ),
        migrations.AddField(
            model_name='save_recipe',
            name='preptime',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
