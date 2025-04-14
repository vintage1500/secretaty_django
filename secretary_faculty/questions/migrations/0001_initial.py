# Generated by Django 5.2 on 2025-04-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('applicant', 'Абитуриент'), ('student', 'Студент')], max_length=10, verbose_name='Тип пользователя')),
                ('question_text', models.TextField(verbose_name='Текст вопроса')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['-created_at'],
            },
        ),
    ]
