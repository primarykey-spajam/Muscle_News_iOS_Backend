from django.contrib import admin

from .models import Muscle
# Register your models here.

@admin.register(Muscle)
class MuscleAdmin(admin.ModelAdmin):
    pass
