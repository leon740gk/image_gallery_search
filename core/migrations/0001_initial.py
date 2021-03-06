# Generated by Django 3.0.5 on 2020-10-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('own_id', models.CharField(max_length=255)),
                ('camera', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('cropped_picture', models.URLField()),
                ('full_picture', models.URLField()),
            ],
        ),
    ]
