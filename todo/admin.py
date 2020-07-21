# Register your models here.

from django.contrib import admin
from .models import todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('work_id','work','due_date','desc')

admin.site.register(todo,TodoAdmin)