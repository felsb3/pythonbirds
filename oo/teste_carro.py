from unittest import TestCase

from oo.carro import Motor

from oo.carro import Direcao

class CarroTestCase(TestCase):

    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
        motor = Motor()
        motor.acelerar()
        motor.acelerar()
        motor.acelerar()
        motor.frear()
        self.assertEqual(1, motor.velocidade)
        motor = Motor()
        motor.acelerar()
        motor.acelerar()
        motor.acelerar()
        motor.frear()
        motor.frear()
        self.assertEqual(0, motor.velocidade)

    def test_direcao(self):
        direcao = Direcao()
        self.assertEqual('Norte', direcao.valor)

    def test_virar_a_direita(self):
        direcao = Direcao()
        direcao.girar_a_direita()
        self.assertEqual('Leste', direcao.valor)

    def test_virar_a_esquerda(self):
        direcao = Direcao()
        direcao.girar_a_esquerda()
        self.assertEqual('Oeste', direcao.valor)
        direcao = Direcao()
        direcao.girar_a_esquerda()
        direcao.girar_a_esquerda()
        self.assertEqual('Sul', direcao.valor)
