# Generated by Django 4.1.1 on 2022-10-07 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_requestedbook_borrow_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestedbook',
            name='borrow_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
