# Generated by Django 2.2 on 2020-05-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_auto_20200512_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
