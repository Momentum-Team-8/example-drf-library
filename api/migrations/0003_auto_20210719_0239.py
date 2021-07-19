# Generated by Django 3.2.5 on 2021-07-19 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210719_0200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookrecord',
            old_name='user',
            new_name='reader',
        ),
        migrations.AlterField(
            model_name='bookrecord',
            name='reading_state',
            field=models.CharField(blank=True, choices=[('wr', 'want to read'), ('rg', 'reading'), ('rd', 'read')], max_length=2, null=True),
        ),
    ]
