# Generated by Django 3.0.9 on 2020-08-03 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_merge_20200803_0941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['location']},
        ),
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='image',
            name='categories',
        ),
        migrations.AddField(
            model_name='image',
            name='categories',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='images.categories'),
            preserve_default=False,
        ),
    ]
