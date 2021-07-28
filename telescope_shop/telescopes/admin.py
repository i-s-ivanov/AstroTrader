from django.contrib import admin

# Register your models here.
from telescope_shop.telescopes.models import Telescope


@admin.register(Telescope)
class TelescopeAdmin(admin.ModelAdmin):
    pass