# Generated by Django 3.2.6 on 2023-02-09 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20230209_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentation',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documentations', to='home.user'),
        ),
    ]
