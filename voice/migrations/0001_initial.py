# Generated by Django 2.2.1 on 2019-05-18 10:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('newsText', models.TextField()),
                ('newsVoice', models.FileField(upload_to='')),
                ('textType', models.CharField(max_length=30)),
            ],
        ),
    ]