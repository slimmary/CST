# Generated by Django 2.2.24 on 2022-01-06 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20211124_1446'),
        ('workorders', '0006_auto_20220106_1544'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WorOrderItem',
            new_name='WorkOrderItem',
        ),
    ]
