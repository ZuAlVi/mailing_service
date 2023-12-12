from django.contrib import admin

from mailings.models import Client, MailingSettings, Message, Log


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'fio', 'email')
    list_filter = ('fio',)
    search_fields = ('fio', 'email', 'comment')


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'start_time', 'end_time', 'period', 'status')
    list_filter = ('start_time', 'end_time', 'period', 'status')
    search_fields = ('start_time', 'end_time')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'mailing_list')
    list_filter = ('mailing_list', )
    search_fields = ('title', 'text')


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mailing_list', 'attempt_time', 'status', 'server_response')
    list_filter = ('mailing_list', 'status')
    search_fields = ('mailing_list', 'attempt_time', 'status')