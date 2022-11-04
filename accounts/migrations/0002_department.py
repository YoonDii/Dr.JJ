# Generated by Django 3.2.13 on 2022-11-03 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('선택', None), ('개발', '개발'), ('기획', '기획'), ('디자인', '디자인')], default='선택', max_length=10)),
            ],
        ),
    ]