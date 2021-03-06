# Generated by Django 4.0.6 on 2022-07-19 19:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bread',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='bread',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='meat',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='meat',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='option',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='option',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated'),
        ),
    ]
