from django.db import models
from manplast.models import Base_Model
from materiales.models import Marco, Material
from clientes.models import Cliente

class Pieza(Base_Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, blank=False)
    marco = models.ForeignKey(Marco, on_delete=models.CASCADE, null=False, blank=False)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=False, blank=False)
    espesor = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    precalentado = models.IntegerField(null=False, blank=False)
    moldeo = models.IntegerField(null=False, blank=False)
    enfriado = models.IntegerField(null=False, blank=False)
    calefaccion = models.ImageField()
    empujador = models.ImageField()
    troquel = models.IntegerField(null=False,blank=False)
    altura_tupir = models.IntegerField(null=False, blank=False)
    observaciones = models.CharField(max_length=400, null=False, blank=False)


    class Meta:
        ordering = ('pk',)

# Create your models here.
