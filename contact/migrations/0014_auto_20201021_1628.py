# Generated by Django 3.1.1 on 2020-10-21 16:28

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0013_auto_20201014_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='description',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]