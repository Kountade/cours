# Generated by Django 4.2.2 on 2023-08-25 21:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0024_alter_blog_description_alter_illustrator_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="description",
        ),
    ]
