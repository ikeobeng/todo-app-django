from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_deadline', 'completed')
    list_filter = ('completed',)
    search_fields = ('title', 'description')

admin.site.register(Todo, TodoAdmin)
