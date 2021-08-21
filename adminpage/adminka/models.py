from django.db import models


class users(models.Model):
    chat_id = models.BigIntegerField(
        verbose_name='ID пользователя',
        unique=True
    )
    name = models.TextField(
        verbose_name='Имя пользователя'
    )
    username = models.TextField(
        verbose_name='Ник пользователя',
        null=True
    )
    reg_dt = models.DateTimeField(
        verbose_name='Дата регистрации'
    )
    args = models.TextField(
        verbose_name='Аргумент к /start',
        null=True
    )

    class Meta():
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        db_table = 'users'


class motivating_phrases(models.Model):
    phrase = models.TextField(
        verbose_name='Фраза'
    )

    class Meta():
        verbose_name = 'мотивирующая фраза'
        verbose_name_plural = 'мотивирующие фразы'
        db_table = 'motivating_phrases'


class notify_phrases(models.Model):
    phrase = models.TextField(
        verbose_name='Фраза'
    )

    class Meta():
        verbose_name = 'напоминающая фраза'
        verbose_name_plural = 'напоминающие фразы'
        db_table = 'notify_phrases'


class jobs(models.Model):
    chat_id = models.BigIntegerField(
        verbose_name='ID пользователя'
    )
    time = models.TimeField(
        verbose_name='Время отправки'
    )
    job_id = models.TextField(
        verbose_name='ID отправки',
        null=True
    )
    class Meta():
        verbose_name = 'отправка по таймеру'
        verbose_name_plural = 'отправки по таймеру'
        db_table = 'jobs'


class progress(models.Model):
    chat_id = models.IntegerField(
        verbose_name='ID пользователя'
    )
    dt = models.DateTimeField(
        verbose_name='Время'
    )
    text = models.TextField(
        verbose_name='Достижение'
    )
    class Meta():
        verbose_name = 'достижение'
        verbose_name_plural = 'достижения'
        db_table = 'progress'


class thank_phrases(models.Model):
    phrase = models.TextField(
        verbose_name='Фраза'
    )

    class Meta():
        verbose_name = 'фраза поблагодарить'
        verbose_name_plural = 'фразы поблагодарить'
        db_table = 'thank_phrases'