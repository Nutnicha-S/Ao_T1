# Generated by Django 3.0 on 2020-05-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0009_auto_20200502_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeGPA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GPA', models.CharField(max_length=255)),
                ('gpa_term', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='Semister',
            new_name='Semester',
        ),
        migrations.DeleteModel(
            name='GPA',
        ),
    ]