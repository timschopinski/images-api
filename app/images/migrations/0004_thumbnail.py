# Generated by Django 4.1.4 on 2023-09-20 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
                ('url', models.ImageField(upload_to='thumbnails/')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumbnails', to='images.image')),
            ],
        ),
    ]
