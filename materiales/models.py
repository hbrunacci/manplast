from django.db import models
from manplast.models import Base_Model

# Create your models here.

class Material(Base_Model):
    nombre = models.CharField(max_length=60,blank=False,null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('pk',)


class Marco(Base_Model):
    nombre = models.CharField(max_length=50,blank=False,null=False)
    maquina = models.CharField(max_length=10,blank=False,null=False)
    ancho_util = models.IntegerField(blank=False,null=False)
    largo_util = models.IntegerField(blank=False,null=False)
    ancho_lamina = models.IntegerField(blank=False,null=False)
    largo_lamina = models.IntegerField(blank=False,null=False)
    superficie = models.IntegerField(blank=False,null=False)

    class Meta:
        ordering = ('pk',)
