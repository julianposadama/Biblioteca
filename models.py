from django.db import models

# Create your models here.


class Estudiante(models.Model):
    ApellidoPaterno = models.CharField(max_length=30)
    ApellidoMaterno = models.CharField(max_length=30)
    Nombres = models.CharField(max_length=30)
    CC = models.CharField(max_length=30)
    SEXOS = (('F', 'Femenino'),('M','Masculino'))
    sexo = models.CharField(max_length=1, choices=SEXOS, default='M')

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()
        

class Materia(models.Model):
    NombreMateria = models.CharField(max_length=30)
    
    def __str__(self):
        return "{0}".format(self.NombreMateria)

class Libro(models.Model):
    NombreLibro = models.CharField(max_length=30)
    #NombreAutor = models.CharField(max_length=30)

    def __str__(self):
        return "{0}".format(self.NombreLibro)

class Prestamos(models.Model):
    Estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    Materia = models.ForeignKey(Materia, null=False, blank=False, on_delete=models.CASCADE)
    Libro = models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)
    FechaPrestamo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}, {2}"
        return cadena.format(self.Estudiante, self.Materia, self.Libro)
