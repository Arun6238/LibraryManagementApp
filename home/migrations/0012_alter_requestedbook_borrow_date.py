# Generated by Django 4.1.1 on 2022-10-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_requestedbook_borrow_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestedbook',
            name='borrow_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
