# Generated by Django 2.2 on 2021-08-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_validated_app', '0002_auto_20210804_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='actions',
            field=models.TextField(),
        ),
    ]