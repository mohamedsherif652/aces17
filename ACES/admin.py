from django.contrib import admin
from .models import applicant, interviewSlots

# Register your models here.

admin.site.register(applicant)
admin.site.register(interviewSlots)