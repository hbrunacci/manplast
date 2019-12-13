from django.db import models
from django.contrib.auth.models import User


class Base_Model(models.Model):
    create_date = models.DateTimeField('Fecha de creacion',auto_now= True)
    modify_date = models.DateTimeField('Fecha de modificacion',auto_now= True )
    user = models.ForeignKey(User,on_delete= models.CASCADE,null=True)

    class Meta:
        abstract=True
