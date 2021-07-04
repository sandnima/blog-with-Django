# Generated by Django 3.2.4 on 2021-07-01 13:00

import blog.models
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profiles.profile'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='lang',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(blog.models.get_default_language), to='blog.language'),
        ),
    ]
