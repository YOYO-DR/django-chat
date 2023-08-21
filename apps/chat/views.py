from django.http import JsonResponse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import json
from .models import HistorialChat
from django.contrib.auth.models import User

class InicioView(TemplateView):
    template_name="chat.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        data=json.loads(request.body)
        try:
          user=User.objects.get(username=data['username'])
        except User.DoesNotExist:
          return JsonResponse({"error":"Usuario no existe"})
        except Exception as e:
           return JsonResponse({"error":str(e)})

        HistorialChat(user=user,message=data['message'],datetime=data['datetime']).save()

        return JsonResponse({"ok":"ok"})
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["room_name"] = "social"
        context['historial']=[message.toJSON() for message in HistorialChat.objects.all().order_by("datetime")]
        return context
    