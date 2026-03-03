import random
class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.__nome}\nVida: {self.__vida}\nNivel: {self.__nivel}"

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 1, self.get_nivel() * 5)
        alvo.receber_dano(dano)
        print(f'{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} dano!')

    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0