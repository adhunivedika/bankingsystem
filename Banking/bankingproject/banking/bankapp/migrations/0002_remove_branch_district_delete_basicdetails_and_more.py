# Generated by Django 4.2.5 on 2023-10-02 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='district',
        ),
        migrations.DeleteModel(
            name='BasicDetails',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='District',
        ),
    ]