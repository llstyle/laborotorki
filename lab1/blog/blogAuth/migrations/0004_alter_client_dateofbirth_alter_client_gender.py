# Generated by Django 4.0.5 on 2022-06-17 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogAuth', '0003_alter_client_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='dateOfBirth',
            field=models.DateField(null=True, verbose_name='Дата выхода'),
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('Fm', 'Female'), ('Ml', 'Male')], default='Ml', max_length=9),
        ),
    ]
