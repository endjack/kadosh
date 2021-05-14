from django.db import models

# Create your models here.
class Membro(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    data_aniversario = models.DateField()
    grupo_membro = models.ForeignKey('membros.Grupo', on_delete=models.CASCADE,blank=True,null=True)
    ministerios = models.ManyToManyField('membros.Ministerio', blank=True)

    def __str__(self):
        return str(self.nome) + ' - ' + str(self.telefone)

class Grupo(models.Model):
    lider = models.ForeignKey(Membro, related_name='lider_grupo', on_delete=models.CASCADE)
    #membros = models.ManyToManyField(Membro)
    dia_semana = models.CharField(max_length=20, default='dia')
    hora = models.CharField(max_length=5, default='00:00')
        
    def __str__(self):
        return str(self.lider.nome) + ' - ' + str(self.dia_semana)

class Ministerio(models.Model):
    nome = models.CharField(max_length=200)
    lider = models.ForeignKey(Membro, related_name='lider_ministerio', on_delete=models.CASCADE)
    #membros = models.ManyToManyField(Membro)
    dia_semana = models.CharField(max_length=20, default='dia')
    hora = models.CharField(max_length=5, default='00:00')

    def __str__(self):
        return str(self.nome) + ' - ' + str(self.dia_semana)

