from django.contrib import admin

# Register your models here.
from telescope_shop.telescopes.models import Telescope, Comment


@admin.register(Telescope)
class TelescopeAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'location', 'user',)
    list_filter = ('make', 'model', 'location', 'created',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'telescope', 'text',)
    list_filter = ('created', 'name',)

