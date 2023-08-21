from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict

class HistorialChat(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Usuario")
  message=models.TextField(null=True, blank=True, verbose_name="Mensaje")
  # formato: 'YYYY-MM-DD HH:MM:SS'
  datetime=models.DateTimeField(verbose_name="Fecha enviado")

  def __str__(self):
    return self.message

  def toJSON(self):
    item=model_to_dict(self)
    item['user'] = {"id":self.user.id, "username":self.user.username}
    return item