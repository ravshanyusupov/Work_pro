# Generated by Django 3.2.9 on 2022-01-09 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_income_outcome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='cost',
        ),
        migrations.AddField(
            model_name='outcome',
            name='income_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.income'),
        ),
    ]
