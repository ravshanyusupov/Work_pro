# Generated by Django 3.2.9 on 2022-01-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20220113_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='update_time',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('День', 'День'), ('Час', 'Час')], default='День', max_length=200),
        ),
    ]
