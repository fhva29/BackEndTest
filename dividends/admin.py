from django.contrib import admin
from .models import Dividend

@admin.register(Dividend)
class DividendAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'date', 'value')
