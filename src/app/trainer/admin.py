from django.contrib import admin
from app.trainer.model import Trainer

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_verify', 'rate')
    search_fields = ('user__email',)
    list_filter = ('is_verify', 'rate')
    ordering = ('user',)

admin.site.register(Trainer, TrainerAdmin)
