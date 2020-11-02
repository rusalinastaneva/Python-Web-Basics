from django.contrib import admin
from todo_app import models


# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_done')
    list_filter = ('is_done')


admin.site.register(models.Todo)
