# Generated by Django 3.1.1 on 2020-09-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0005_remove_question_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=300)),
                ('num', models.IntegerField()),
            ],
        ),
    ]
