from django.db import models

# Create your models here.

class Solicitud(models.Model):
    nombre = models.CharField(max_length=50)
    archivo = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.nombre, self.archivo)
