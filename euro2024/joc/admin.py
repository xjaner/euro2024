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
    list_filter = ['is_active']

admin.site.register(Jugador, JugadorAdmin)
