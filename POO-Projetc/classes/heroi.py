import random
from classes.personagem import Personagem

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"

    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 1, self.get_nivel() * 5)
        alvo.receber_dano(dano)
        print(f'{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} dano!')