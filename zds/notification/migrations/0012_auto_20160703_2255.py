from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notification", "0011_notification_is_dead"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="subscription",
            unique_together={("user", "content_type", "object_id")},
        ),
    ]
