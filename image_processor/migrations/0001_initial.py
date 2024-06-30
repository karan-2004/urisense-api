# Generated by Django 4.0.6 on 2024-06-30 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='strips/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chemical', models.CharField(choices=[('1', 'URO'), ('2', 'KET'), ('3', 'BIL'), ('4', 'BLD'), ('5', 'PRO'), ('6', 'NIT'), ('7', 'GLU'), ('8', 'LEU'), ('9', 'SG'), ('10', 'PH')], max_length=4)),
                ('red', models.IntegerField()),
                ('green', models.IntegerField()),
                ('blue', models.IntegerField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_processor.test')),
            ],
        ),
    ]
