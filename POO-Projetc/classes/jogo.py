from classes.heroi import Heroi
from classes.inimigo import Inimigo 


class Jogo:
    def __init__(self):
        self.heroi = Heroi('Herói', 100, 5, 'Força')
        self.inimigo = Inimigo('Inimigo', 50, 3, 'Voador')

    def iniciar_batalha(self):
        print("Inicianfo batalha!")

        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print('\nDetalhes dos personagens:')
            print(self.heroi.exibir_detalhes())
            print('\n')
            print(self.inimigo.exibir_detalhes())

            input('\nPressione Qualquer tecla para iniciar a batalha')
            escolha = int(input('Escolha (1 - Ataque Normal, 2 - Ataque Especial)'))

