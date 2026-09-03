from django.db import models
import datetime
from django.utils import timezone


class Raca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Animal(models.Model):
    nome = models.CharField(max_length=50)
    dono = models.CharField(max_length=50)
    nascimento = models.DateTimeField('Data de nascimento')
    telefone_dono = models.CharField("Telefone do dono", max_length=11)
    tipo_animal = models.CharField("Tipo do Animal", max_length=1)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)

    def nascimento_valido(self):
        #Não pode ser no futuro
        amanha = timezone.now() + datetime.timedelta(days=1)
        #Não pode ser muito no passado
        vinte_anos_atras = timezone.now() - datetime.timedelta(days=20*365)



    def __str__(self):
        resposta = f'{self.nome} ({self.raca})'
        return resposta


class Vacina(models.Model):
    data_vacinacao = models.DateTimeField("Data da vacinação")
    nome_vacina = models.CharField("Nome da vacina", max_length=50)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        resposta = f'{self.nome_vacina} (em {self.data_vacinacao})'
        return resposta


