# Generated by Django 3.2.3 on 2021-08-04 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0004_auto_20210804_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='myform',
            name='supervisor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='evaluation.supervisor'),
            preserve_default=False,
        ),
    ]
