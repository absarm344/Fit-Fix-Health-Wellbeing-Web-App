# Generated by Django 4.2.3 on 2023-07-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_subplan_subplanfeatures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subplanfeatures',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
