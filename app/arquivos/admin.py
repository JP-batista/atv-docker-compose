from django.contrib import admin

from .models import Arquivo


@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "arquivo", "enviado_em")
