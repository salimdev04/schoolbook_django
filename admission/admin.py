from django.contrib import admin

from .models import Admission, ShopCart, Stream

# Register your models here.


@admin.register(ShopCart)
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['campus', 'user', ]
    list_filter = ['user']


@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ['campus', 'student', 'created_at']
    list_filter = ['campus']


class Admissionline(admin.TabularInline):
    model = Admission
    readonly_fields = ('campus',)
    can_delete = False
    extra = 0


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['campus', 'student_infos']
    list_filter = ['campus']
