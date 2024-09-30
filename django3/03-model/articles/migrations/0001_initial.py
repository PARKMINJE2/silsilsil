# Generated by Django 4.2.16 on 2024-09-20 00:43

from django.db import migrations, models

# 최종 설계도
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', 
                models.BigAutoField(
                    auto_created=True, 
                    primary_key=True, 
                    serialize=False, 
                    verbose_name='ID',
                    ),
                ),
                # 우리가 만든거
                ('title', models.CharField(max_length=10)),
                ('content', models.TextField()),
            ],
        ),
    ]
