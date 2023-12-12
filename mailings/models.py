from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    fio = models.CharField(max_length=50, verbose_name='ФИО')
    email = models.EmailField(max_length=150, unique=True, verbose_name='Почта')
    comment = models.TextField(verbose_name='Коментарий', **NULLABLE)

    def __str__(self):
        return f'{self.fio} - {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('fio',)


class MailingSettings(models.Model):
    DAILY = 'Раз в день'
    WEEKLY = 'Раз в неделю'
    MONTHLY = 'Раз в месяц'

    PERIOD_CHOICES = [
        (DAILY, 'Раз в день'),
        (WEEKLY, 'Раз в неделю'),
        (MONTHLY, 'Раз в месяц')
    ]

    CREATED = 'Создана'
    STARTED = 'Запущена'
    FINISHED = 'Завершена'

    STATUS_CHOICES = [
        (CREATED, 'Создана'),
        (STARTED, 'Запущена'),
        (FINISHED, 'Завершена')
    ]

    start_time = models.DateTimeField(verbose_name='Время старта рассылки')
    end_time = models.DateTimeField(verbose_name='Время окончания рассылки')
    period = models.CharField(max_length=15, verbose_name='Период рассылки', choices=PERIOD_CHOICES)
    status = models.CharField(max_length=15, verbose_name='Статус рассылки', choices=STATUS_CHOICES, default=CREATED)

    clients = models.ManyToManyField(Client, verbose_name='Клиенты рассылки')

    def __str__(self):
        return f'Период с {self.start_time} по {self.end_time}, {self.period}, статус: {self.status}'

    class Meta:
        verbose_name = 'Настройки рассылки'
        verbose_name_plural = 'Настройки рассылки'


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тема')
    text = models.TextField(verbose_name='Сообщение')
    mailing_list = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='Рассылка', related_name='messages', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Log(models.Model):
    attempt_time = models.DateTimeField(verbose_name='Последняя попытка', auto_now_add=True)
    status = models.BooleanField(verbose_name='Статус попытки')
    server_response = models.CharField(verbose_name='Ответ сервера', **NULLABLE)

    mailing_list = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='Рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент рассылки', **NULLABLE)

    def __str__(self):
        return f'{self.attempt_time} - {self.status}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
