from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    
class PostAdmin(admin.ModelAdmin):
    #campos de solo lectura
    readonly_fields = ['created', 'updated']
    # campos a mostrar en el admin
    list_display = ['title', 'author', 'published', 'post_categories']
    # forma de ordenar los registros
    ordering = ['author', 'published']
    # campos a buscar
    search_fields = ['title', 'content', 'author__username', 'categories__name']
    # jerarquia de fechas
    date_hierarchy = 'published'
    # filtros: generalmente a los campos relacionados
    list_filter = ['author__username', 'categories__name']
    
    
    # todo esto es para poder mostrar las categorias en el admin
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)