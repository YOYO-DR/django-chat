from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import HistorialChat

class InicioView(TemplateView):
    template_name="chat.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["room_name"] = "social"
        historial=[]
        for i in HistorialChat.diasRegistros():
          # filtro la fecha asi, porque podria hacerlo datetime__date=i, pero como cambie la zona horaria a America/Bogota, filtro la busqueda como string
          registros=[j.toJSON() for j in HistorialChat.objects.filter(datetime__icontains=i).order_by("datetime")]
          historial.append({"dia":i,"registros":registros})
        context['historial']=historial
        return context
    