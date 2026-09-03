from django.contrib import admin
from .models import Raca, Animal, Vacina


class VacinasInLine(admin.TabularInline):
    model = Vacina #Formulário de objeto vacina
    extra = 1      #Adiciona uma vacina por vez


class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Dados do animal", {"fields": ["raca", "nome", "tipo_animal", "nascimento"]}),
        ("Dados do dono do animal", {"fields": ["dono", "telefone_dono"]}),
    ]
    inlines = [VacinasInLine]


admin.site.register(Raca)
admin.site.register(Animal, AnimalAdmin)