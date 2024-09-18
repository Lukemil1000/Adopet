from django.contrib import admin
from adopet.models import Tutor

class TutorAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "phone", "city")
    list_per_page = 10

admin.site.register(Tutor, TutorAdmin)
