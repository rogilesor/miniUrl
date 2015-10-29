from django.contrib import admin
from .models import MiniUrl

class MiniUrlAdmin(admin.ModelAdmin):
	list_display=('url','code','date','pseudo','nb_acces')
	list_filter=('pseudo',)
	date_hierarchy='date'
	ordering = ('date',)
	search_fields=('url',)

admin.site.register(MiniUrl,MiniUrlAdmin)