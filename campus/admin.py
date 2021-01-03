from django.contrib import admin

from .models import Campus, Category, Images, Level, Speciality
# Register your models here.


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status',)
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pays',)
    prepopulated_fields = {'slug': ('pays',)}


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
