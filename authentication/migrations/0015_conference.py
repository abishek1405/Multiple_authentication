# Generated by Django 4.0.6 on 2022-08-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_alter_pub_papertitle_alter_pub_yearofpub'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=400)),
                ('noc', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=200)),
                ('organizer', models.CharField(max_length=100)),
                ('day', models.DateField()),
                ('isbn', models.IntegerField()),
                ('page', models.IntegerField()),
                ('proof', models.FileField(upload_to='')),
            ],
        ),
    ]
