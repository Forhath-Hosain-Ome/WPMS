# Generated by Django 5.2.4 on 2025-07-21 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("attendance", "0001_initial"),
        ("workers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
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
                ("date", models.DateField(auto_now_add=True)),
                ("check_in_time", models.DateTimeField()),
                ("check_out_time", models.DateTimeField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Present", "Present"),
                            ("Absent", "Absent"),
                            ("Late", "Late"),
                            ("On Leave", "On Leave"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "shift",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attendances",
                        to="attendance.shiftmodel",
                    ),
                ),
                (
                    "worker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attendances",
                        to="workers.workermodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Attendance",
                "verbose_name_plural": "Attendances",
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="WorkShift",
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
                ("assignment_date", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "shift",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="attendance.shiftmodel",
                    ),
                ),
                (
                    "worker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="workers.workermodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Work Shift",
                "verbose_name_plural": "Work Shifts",
                "ordering": ["-assignment_date"],
            },
        ),
    ]
