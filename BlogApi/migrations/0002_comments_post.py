# Generated by Django 4.0.5 on 2022-06-28 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BlogApi.post'),
            preserve_default=False,
        ),
    ]
