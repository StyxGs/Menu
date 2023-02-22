from django.contrib import admin

from menu.models import CategoriesMenu, Menu


class CategoriesMenuAdmin(admin.TabularInline):
    model = CategoriesMenu
    fields = ('name', 'slug', 'parent',)
    prepopulated_fields = {"slug": ("name",)}
    extra = 0


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = (CategoriesMenuAdmin,)
