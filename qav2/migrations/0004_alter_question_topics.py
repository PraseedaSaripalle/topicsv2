# Generated by Django 3.2.12 on 2022-03-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qav2', '0003_alter_topic_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='topics',
            field=models.ManyToManyField(to='qav2.Topic'),
        ),
    ]
