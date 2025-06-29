from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0013_alter_skill_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
