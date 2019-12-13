from django.db import models
from manplast.models import Base_Model
# Create your models here.


class Cliente(Base_Model):
    razon_social = models.CharField(max_length=100,null=False,blank=True)

    def __str__(self):
        return self.razon_social

    class Meta:
        ordering = ('pk',)




