from django.db import models

class Pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombres = models.CharField(max_length=180)
    apellido_paterno = models.CharField(max_length=180)
    apellido_materno = models.CharField(max_length=180)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField(max_length=254)
    detalles_envio = models.TextField()

    class Meta:
        managed = True
        db_table = 'pedido'

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"
