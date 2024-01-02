from django.contrib import admin

from mailings.models import Client, Mailing, Message, Logs
from users.models import User


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'comment',)
    list_filter = ('full_name',)
    search_fields = ('full_name', 'email', 'comment')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Mailing)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'interval', 'status', 'owner')
    list_filter = ('start_date', 'end_date', 'interval', 'status', 'owner')
    search_fields = ('start_date', 'end_date')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'last_mailing_time', 'status',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('email',)
