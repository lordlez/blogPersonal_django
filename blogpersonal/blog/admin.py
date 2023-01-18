from django.contrib import admin
from . models import Post

# Register your models here.
#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'desc', 'created') # ver las columnas
    list_display_links = ('id', 'title') # crear link a las columnas
    list_filter = ('created', 'updated') # crear filtrado
    search_fields = ('title', 'desc') # crear barra busqueda

    readonly_fields = ('created', 'updated') # mostrar fecha creacion y actualizacion

