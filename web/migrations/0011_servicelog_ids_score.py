# Generated by Django 4.1.3 on 2022-11-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0010_alter_servicelog_autonomous_system_organization_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicelog",
            name="ids_score",
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
