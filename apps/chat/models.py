from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.utils import timezone

from apps.chat.function import timezone_now_cre
from config.settings import TIME_ZONE

class HistorialChat(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Usuario")
  message=models.TextField(null=True, blank=True, verbose_name="Mensaje")
  # formato: 'YYYY-MM-DD HH:MM:SS'
  datetime=models.DateTimeField(auto_now_add=True,verbose_name="Fecha enviado")

  def __str__(self):
    return self.message

  def toJSON(self):
    item=model_to_dict(self)
    item['user'] = {"id":self.user.id, "username":self.user.username}
    # agrego una key para no modificar el original, y le aplico un formato para que aparezca de 0 a 12 y con su pm y am
    item['datetime']=timezone_now_cre(self.datetime,TIME_ZONE)
    item['datetime_format']=item['datetime'].strftime("%I:%M %p").lstrip("0")
    return item
  
  def diasRegistros():
    # asi obtengo las fechas sin la hora, el datetime es el campo, el date_only es como el filtro, en este caso, solo fechas
    #annotate agrega una columna o key a cada resultado llamada date_only
    # en este caso TruncDate toma una fecha y le quita las horas para dejar solo la fecha, y aqui se agrega a esa columna
    # con .values le digo que columnas quiero, en este caso, solo la que creamos, la de date_only
    # la funcion .distinct elimina los duplicados para solo tener , en este caso, fehcas unicas y no repetidas
    #dias= HistorialChat.objects.annotate(date_only=TruncDate('datetime')).values('date_only').distinct().order_by("date_only")

    # otra forma para poder limitar a los ultimos dias requeridos, porque despues de aplicar un [:] (slice), no se puede utilizar distinct()
    
    #obtengo los dias que quiero, y a cada uno le cambio su datetime al que quiero
    fechas=HistorialChat.objects.order_by('-datetime')[:10]
    for fecha in fechas:
      fecha.datetime=timezone_now_cre(fecha.datetime,TIME_ZONE)
    ultimosDias=[registro.datetime.date() for registro in fechas]

    # quitar los repetidos
    dias=list(set(ultimosDias))

    # retornarlo ordenado
    dias.sort()

    return [dias,fechas]
