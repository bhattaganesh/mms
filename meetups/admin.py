from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Location, Meetup, Participant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date', )
    list_filter = ('location', 'date', )
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)