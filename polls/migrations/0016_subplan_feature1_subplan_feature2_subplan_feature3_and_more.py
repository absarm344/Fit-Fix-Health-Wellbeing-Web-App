# Generated by Django 4.2.3 on 2023-07-13 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_subplanfeatures_delete_subplanfeature'),
    ]

    operations = [
        migrations.AddField(
            model_name='subplan',
            name='feature1',
            field=models.CharField(default='Null', max_length=300),
        ),
        migrations.AddField(
            model_name='subplan',
            name='feature2',
            field=models.CharField(default='Null', max_length=300),
        ),
        migrations.AddField(
            model_name='subplan',
            name='feature3',
            field=models.CharField(default='Null', max_length=300),
        ),
        migrations.AddField(
            model_name='subplan',
            name='feature4',
            field=models.CharField(default='Null', max_length=300),
        ),
        migrations.AddField(
            model_name='subplan',
            name='feature5',
            field=models.CharField(default='Null', max_length=300),
        ),
        migrations.DeleteModel(
            name='subPlanFeatures',
        ),
    ]
