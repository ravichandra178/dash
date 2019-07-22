# Generated by Django 2.2.2 on 2019-07-19 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import leave.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.SlugField(default='', max_length=10)),
                ('message', models.TextField()),
                ('approve', models.BooleanField(default=False)),
                ('from_date', models.DateField(default=leave.models.g)),
                ('to_date', models.DateField(default=leave.models.g)),
                ('created_at', models.DateTimeField(default=leave.models.now)),
                ('note', models.TextField(default='Remarks')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
