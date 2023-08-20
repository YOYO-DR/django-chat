from django.db import models
from django.contrib.auth.models import User

class HistorialChat(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Usuario")
  message=models.TextField(null=True, blank=True, verbose_name="Mensaje")
  datetime=models.DateTimeField(auto_now_add=True, verbose_name="Fecha enviado")
