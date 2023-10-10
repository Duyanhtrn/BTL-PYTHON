# Generated by Django 4.2.5 on 2023-10-01 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0015_chapter_remove_manga_chapterfiles_page_chapter_manga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='manga',
        ),
        migrations.RemoveField(
            model_name='page',
            name='chapter',
        ),
        migrations.AddField(
            model_name='chapter',
            name='pages',
            field=models.ManyToManyField(to='manga.page'),
        ),
        migrations.AddField(
            model_name='manga',
            name='chapters',
            field=models.ManyToManyField(to='manga.chapter'),
        ),
    ]
