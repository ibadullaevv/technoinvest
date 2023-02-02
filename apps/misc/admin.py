from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import *


@admin.register(Article)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)

admin.site.register(Post)
admin.site.register(Slider)
admin.site.register(AboutCompany)
admin.site.register(OurService)
