from django.db import models
from datetime import date
# Create your models here.
class Meta:
    permissions = [
        ("puede_crear_documentos", "puede crear documentos"),
        ("puede_revisar_documentos", "puede revisar documentos"),
    ]

class Puerto(models.Model):
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} - {self.ubicacion}"

class Nave(models.Model):
    nombre = models.CharField(max_length=100)
    bandera = models.CharField(max_length=100)
    capacidad = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

class Ruta(models.Model):
    #este default fue añadido solo para que no diera problemas para modelos anteriores
    #sin embargo el enviar los formularios no se permite esté en blaco
    fechaSalida = models.DateField(blank=True, default=date(2024,1,12))
    nave = models.ForeignKey(Nave, on_delete=models.CASCADE)

#este class valida que cada ruta creada con una nave, no pueda tener una misma fecha asignada
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nave', 'fechaSalida'],
                name='unique_nave_fecha'
            )
        ]

    def __str__(self):
        escalas = ", ".join([str(escala.puertoDestino) for escala in self.escalas.all()])
        return f"Nave: {self.nave} - Escalas: {escalas}"
    
    #libros = ", ".join([libro.titulo for libro in self.libros.all()]) return f"{self.nombre} ({libros})"

    #cuando se ocupa una rel de uno a muchos se pone en el muchos, asi se puede acceder desde el otro
class Escala(models.Model):
    nombre = models.CharField(max_length=200)
    puertoDestino = models.ForeignKey(Puerto, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name='escalas')

    def __str__(self):
        return f"Puerto Destino: {self.puertoDestino}"

class Documento(models.Model):
    #este tipo debio haber sido tipo choice
    tipo = models.CharField(max_length=200)
    nombreBuque = models.CharField(max_length=200)
    estado = models.CharField(
        max_length=20,
        choices=[('pendiente', 'Pendiente'), ('revisado', 'Revisado')],
        default= 'pendiente'
    )
    infovendedor = models.CharField(max_length=200)
    escala = models.ForeignKey(Escala, on_delete=models.CASCADE, related_name='documentos')

    def __str__(self):
        return f"{self.tipo} - #{self.id}"


