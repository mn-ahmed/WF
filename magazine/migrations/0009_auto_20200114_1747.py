# Generated by Django 2.2.9 on 2020-01-14 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0008_deeparchiveindexpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivearticleauthor',
            name='archive_article',
        ),
        migrations.RemoveField(
            model_name='archivearticleauthor',
            name='author',
        ),
        migrations.DeleteModel(
            name='ArchiveArticle',
        ),
        migrations.DeleteModel(
            name='ArchiveArticleAuthor',
        ),
    ]