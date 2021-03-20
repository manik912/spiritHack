# Generated by Django 3.1.7 on 2021-03-20 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20210320_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('file', models.FileField(blank=True, default='', null=True, upload_to='file/')),
                ('Subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.subject')),
                ('resource_by', models.ForeignKey(limit_choices_to={'is_student': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('due_at', models.DateTimeField()),
                ('Subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.subject')),
                ('reminder_by', models.ForeignKey(limit_choices_to={'is_student': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
