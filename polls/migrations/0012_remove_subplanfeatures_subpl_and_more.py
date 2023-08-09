# Generated by Django 4.2.3 on 2023-07-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_alter_subplanfeatures_subpl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subplanfeatures',
            name='subPl',
        ),
        migrations.AlterField(
            model_name='subplanfeatures',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AddField(
            model_name='subplanfeatures',
            name='subpl',
            field=models.ManyToManyField(to='polls.subplan'),
        ),
    ]