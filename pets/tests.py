import datetime

from django.test import TestCase
from datetime import date
from .models import Animal


class AnimalTest(TestCase):

    def test_data_futura(self):
        hoje = date.today()
        amanha = hoje + datetime.timedelta(days=1)

        animalNascidoHoje = Animal()
        animalNascidoHoje.nascimento = hoje
        self.assertTrue(animalNascidoHoje.nascimento_valido(), "Data de nascimento inválida")

        animalNascidoAmanha = Animal()
        animalNascidoAmanha.nascimento = amanha
        self.assertFalse(animalNascidoAmanha.nascimento_valido(), "Data de nascimento inválida")


    def test_data_muito_antiga(self):
        hoje = date.today()
        vinteAnosAtras = hoje - datetime.timedelta(days=(365 * 20)-1)
        poucoMaisDeVinteAnosAtras = hoje - datetime.timedelta(days=(365 * 20) + 1)

        animalNascidoHa20Anos = Animal()
        animalNascidoHa20Anos.nascimento = vinteAnosAtras
        self.assertTrue(animalNascidoHa20Anos.nascimento_valido(), "Data de nascimento inválida")

        animalNascidoHaMaisDe20Anos = Animal()
        animalNascidoHaMaisDe20Anos.nascimento = poucoMaisDeVinteAnosAtras
        self.assertFalse(animalNascidoHaMaisDe20Anos.nascimento_valido(), "Data de nascimento inválida")