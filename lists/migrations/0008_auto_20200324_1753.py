# Generated by Django 3.0 on 2020-03-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_auto_20200324_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='gpa',
            field=models.ManyToManyField(to='lists.GPA'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='term1',
            field=models.ManyToManyField(to='lists.Term1'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='term2',
            field=models.ManyToManyField(to='lists.Term2'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='term3',
            field=models.ManyToManyField(to='lists.Term3'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='term4',
            field=models.ManyToManyField(to='lists.Term4'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='term5',
            field=models.ManyToManyField(to='lists.Term5'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='term6',
            field=models.ManyToManyField(to='lists.Term6'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='term7',
            field=models.ManyToManyField(to='lists.Term7'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='term8',
            field=models.ManyToManyField(to='lists.Term8'),
        ),
    ]
