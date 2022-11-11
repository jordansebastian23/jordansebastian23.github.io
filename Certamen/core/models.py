from django.db import models

# Create your models here.
class residencia(models.Model):
    telefono = models.CharField(max_length=50)
    dueño = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)


class correspondecia(models.Model):
    fecha_recepcion = models.DateTimeField('date published')
    conserje = models.CharField(max_length=50)
    remitente = models.CharField(max_length=50)
    destinatario = models.CharField(max_length=50)
    nro_residencia = models.ForeignKey(residencia, on_delete=models.CASCADE)
    RECIBIDO= 'RECIBIDO'
    NO_RECIBIDO= 'NO RECIBIDO'
    EN_PROCESO= 'EN PROCESO'
    ESTADO_CHOICES = [
        (RECIBIDO, 'RECIBIDO'),
        (NO_RECIBIDO, 'NO RECIBIDO'),
        (EN_PROCESO, 'EN PROCESO'),
    ]
    estado = models.CharField(
        max_length=50,
        choices=ESTADO_CHOICES,
        default=NO_RECIBIDO,
    )

def __str__(self):
    return all
