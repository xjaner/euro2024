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
    list_display = ['usuari', 'get_first_name', 'get_is_active', 'get_date_joined']
    list_filter = ['usuari__is_active']
    ordering = ['-usuari__date_joined']

    @admin.display(description='Nom Real')
    def get_first_name(self, obj):
        return obj.usuari.first_name

    @admin.display(description='Registrat')
    def get_date_joined(self, obj):
        return obj.usuari.date_joined

    @admin.display(description='Activat?')
    def get_is_active(self, obj):
        return obj.usuari.is_active

admin.site.register(Jugador, JugadorAdmin)
