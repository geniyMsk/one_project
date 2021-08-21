from django.contrib import admin

from .models import users, motivating_phrases, notify_phrases, jobs, progress, thank_phrases

@admin.register(users)
class usersAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'name', 'username', 'reg_dt', 'args')


@admin.register(motivating_phrases)
class motivating_phrasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'phrase')
    ordering = ['id']


@admin.register(notify_phrases)
class notify_phrasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'phrase')
    ordering = ['id']


@admin.register(thank_phrases)
class thank_phrasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'phrase')
    ordering = ['id']


@admin.register(jobs)
class jobsAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'time', 'job_id')


@admin.register(progress)
class progressAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'dt', 'text']