# Generated by Django 4.2.5 on 2023-10-01 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0012_remove_chapter_manga_remove_page_chapter_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.IntegerField()),
                ('numberOfPages', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='manga',
            name='chapters',
        ),
        migrations.DeleteModel(
            name='Chapter',
        ),
    ]
