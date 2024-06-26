from django.db.models import Q
from django.conf import settings
from django.views import generic

from joc.models import Jugador


class UsuarisView(generic.ListView):
    def get_queryset(self):
        return Jugador.objects.filter(usuari__is_active=True).filter(~Q(usuari_id=settings.ID_ADMIN))
