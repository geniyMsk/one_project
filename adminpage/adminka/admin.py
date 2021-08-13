from django.contrib import admin

from .models import users, motivating_phrases, notify_phrases, jobs, progress

@admin.register(users)
class usersAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'name', 'username', 'reg_dt', 'args')


@admin.register(motivating_phrases)
class phrasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'phrase')
    ordering = ['id']


@admin.register(notify_phrases)
class phrasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'phrase')
    ordering = ['id']


@admin.register(jobs)
class jobsAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'time')


@admin.register(progress)
class progressAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'dt', 'text']