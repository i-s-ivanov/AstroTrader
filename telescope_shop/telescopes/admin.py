from django.contrib import admin

# Register your models here.
from telescope_shop.telescopes.models import Telescope, Comment
from mptt.admin import MPTTModelAdmin


@admin.register(Telescope)
class TelescopeAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'location', 'user',)
    list_filter = ('make', 'model', 'location', 'created',)


admin.site.register(Comment, MPTTModelAdmin)