# Generated by Django 5.0.1 on 2024-02-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]