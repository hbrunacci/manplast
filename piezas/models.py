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
    calefaccion = models.ImageField(verbose_name='Seteo Calefaccion', null=True, blank=True, upload_to='uploads/')
    empujador = models.ImageField(verbose_name='Imagen Empujador', null=True, blank=True, upload_to='uploads/')
    sombra = models.ImageField(verbose_name='Imagen Sombra', null=True, blank=True, upload_to='uploads/')
    #troquel = models.IntegerField(null=False, blank=False)
    #altura_tupir = models.IntegerField(null=False, blank=False)
    observaciones = models.CharField(max_length=400, null=False, blank=False)

    imagen_pieza = models.ImageField(verbose_name='Imagen Pieza', null=True, blank=True, upload_to='uploads/')

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return F'{self.nombre} {self.cliente}'


# Create your models here.

class Cortes(Base_Model):
    TIPOS_CORTES = [('tupir', 'Tupir'),
                    ('sierra', 'Sierra'),
                    ('Agujereadora', 'Agujereadora'),
                    ('en_altura', 'Corte en altura'), ]

    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE, null=True, blank=True, related_name='cortes')
    tipo_corte = models.CharField(max_length=50, null=False, blank=False, choices=TIPOS_CORTES)
    detalle = models.CharField('Detalle', max_length=1000, null=True, blank=True)
    altura = models.IntegerField(null=True, blank=True)
    tiempo = models.IntegerField(null=True, blank=True)
    imagen_ref = models.ImageField(verbose_name='Imagen Muestra', null=True, blank=True, upload_to='uploads/')

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return F'{self.tipo_corte} {self.detalle}'
