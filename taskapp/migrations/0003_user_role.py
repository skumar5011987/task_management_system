# Generated by Django 5.1.7 on 2025-03-25 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskapp", "0002_alter_task_blocked_reason"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("manager", "Manager"),
                    ("developer", "Developer"),
                    ("analyst", "Analyst"),
                    ("qa", "QA"),
                ],
                default="developer",
                max_length=24,
            ),
        ),
    ]
