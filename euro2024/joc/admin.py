from django.contrib import admin
from joc.models import Jugador
from django_registration.backends.activation.views import RegistrationView

@admin.action(description='Acceptar els jugadors seleccionats')
def approve_players(modeladmin, request, queryset):
    rv = RegistrationView()
    rv.setup(request)
    for jugador in queryset:
        rv.send_activation_email(jugador.usuari)

class JugadorAdmin(admin.ModelAdmin):
    actions = [approve_players]
    readonly_fields = ('usuari', 'posicio', 'posicio_anterior', 'punts', 'punts_anterior',
                       'punts_resultats', 'punts_grups', 'punts_equips_encertats')
    list_filter = ['usuari__is_active']

admin.site.register(Jugador, JugadorAdmin)
