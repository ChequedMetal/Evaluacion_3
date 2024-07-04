from django.db import models

class Pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombres = models.CharField(max_length=180)
    apellido_paterno = models.CharField(max_length=180)
    apellido_materno = models.CharField(max_length=180)
    codigo_region = models.CharField(max_length=2)
    codigo_comuna = models.CharField(max_length=6)

    class Meta:
        managed = True
        db_table = 'Pedido'

    def __str__(self):
        return self.nombres