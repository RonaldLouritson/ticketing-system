from django.contrib import admin
from .models import *

class TicketAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	list_filter = ('status', 'requester_email')
	list_display = ('id', 'title', 'requester_email', 'status', 'description', 'locker_num', 'tag_num', 'updated_at')
	search_fields = ['title','status']

admin.site.register(Ticket, TicketAdmin)
admin.site.register(RandomNumber)

class LockerAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	list_filter = ('locker_num', 'locker_status', 'locker_available')
	list_display = ('id', 'locker_num', 'locker_status', 'locker_available', 'created_at', 'updated_at')
	search_fields = ['locker_num','locker_status','locker_available']

admin.site.register(Locker, LockerAdmin)