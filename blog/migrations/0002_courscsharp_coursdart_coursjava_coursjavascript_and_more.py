# Generated by Django 4.2.2 on 2023-06-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="courscsharp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=500)),
                ("code", models.CharField(max_length=50000)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField(max_length=50000)),
                ("resultat", models.CharField(max_length=50000)),
            ],
            options={
                "ordering": ["-date_added"],
            },
        ),
        migrations.CreateModel(
            name="coursdart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=500)),
                ("code", models.CharField(max_length=50000)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField(max_length=50000)),
                ("resultat", models.CharField(max_length=50000)),
            ],
            options={
                "ordering": ["-date_added"],
            },
        ),
        migrations.CreateModel(
            name="coursjava",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=500)),
                ("code", models.CharField(max_length=50000)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField(max_length=50000)),
                ("resultat", models.CharField(max_length=50000)),
            ],
            options={
                "ordering": ["-date_added"],
            },
        ),
        migrations.CreateModel(
            name="coursjavascript",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=500)),
                ("code", models.CharField(max_length=50000)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField(max_length=50000)),
                ("resultat", models.CharField(max_length=50000)),
            ],
            options={
                "ordering": ["-date_added"],
            },
        ),
        migrations.CreateModel(
            name="courspython",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=500)),
                ("code", models.CharField(max_length=50000)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField(max_length=50000)),
                ("resultat", models.CharField(max_length=50000)),
            ],
            options={
                "ordering": ["-date_added"],
            },
        ),
        migrations.DeleteModel(
            name="coursp",
        ),
        migrations.AlterModelOptions(
            name="coursphp",
            options={"ordering": ["-date_added"]},
        ),
        migrations.RenameField(
            model_name="coursphp",
            old_name="codes",
            new_name="resultat",
        ),
    ]
