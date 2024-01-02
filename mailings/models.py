from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {'null': True, 'blank': True}

STATUS_CHOICES = [
    ('Создана', 'Создана'),
    ('Запущена', 'Запущена'),
    ('Завершена', 'Завершена'),
]
INTERVAL_CHOICES = [
    ('разовая', 'разовая'),
    ('ежедневно', 'ежедневно'),
    ('раз в неделю', 'раз в неделю'),
    ('раз в месяц', 'раз в месяц'),
]


class Client(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(verbose_name='почта')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='чей клиент')

    def __str__(self):
        return f'{self.email} ({self.full_name})'

    def __repr__(self):
        return f'{self.email} ({self.full_name})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    title = models.CharField(max_length=250, verbose_name='тема')
    content = models.TextField(verbose_name='содержание')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Владелец сообщения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    name = models.CharField(max_length=50, verbose_name='название рассылки')
    mail_to = models.ManyToManyField(Client, verbose_name='кому')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)
    start_date = models.DateTimeField(default=timezone.now, verbose_name='время старта рассылки')
    next_date = models.DateTimeField(default=timezone.now, verbose_name='время следующей рассылки')
    end_date = models.DateTimeField(verbose_name='время окончания рассылки')
    interval = models.CharField(default='разовая', max_length=50, choices=INTERVAL_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, help_text="Выберите Создана или Завершена")

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Владелец рассылки')
    is_activated = models.BooleanField(default=True, verbose_name='действующая')

    def __str__(self):
        return f'"{self.name}"'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('start_date',)

        permissions = [
            ('set_is_activated', 'Может отключать рассылку')
        ]


class Logs(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)
    last_mailing_time = models.DateTimeField(auto_now=True, verbose_name='время последней рассылки')
    status = models.CharField(max_length=50, verbose_name='статус попытки', null=True)

    def __str__(self):
        return f'Отправлено: {self.last_mailing_time}, ' \
               f'Статус: {self.status}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'