# Generated by Django 4.2.8 on 2023-12-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipehome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipename', models.CharField(max_length=100)),
                ('recipedis', models.TextField()),
                ('recipeimg', models.ImageField(default='recipeimage', upload_to='')),
            ],
        ),
    ]
