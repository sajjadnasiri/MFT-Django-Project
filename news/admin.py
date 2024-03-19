from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'ceated_date'
    list_display = ['title', 'content', 'active', 'ceated_date']
    # fields = ['content']
    search_fields = ['title', 'content']
    ordering = ['-ceated_date']
    list_filter = ['active']
    
    
# admin.site.register(News, NewsAdmin)