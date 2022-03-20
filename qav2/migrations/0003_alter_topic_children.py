# Generated by Django 3.2.12 on 2022-03-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qav2', '0002_alter_topic_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='children',
            field=models.ManyToManyField(blank=True, null=True, related_name='parents', to='qav2.Topic'),
        ),
    ]