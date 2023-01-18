from django.contrib import admin
from .models import Project

# Register your models here.

#admin.site.register(Project)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'created') # ver las columnas
    list_editable = ('title',) # posibilidad de editar
    list_filter = ('title', 'created', 'updated')
    search_fields = ('title',)