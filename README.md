# ⚔️ Jogo RPG em Texto - Projeto POO

Um jogo de batalha em texto simples desenvolvido em Python para aplicar e consolidar os conceitos fundamentais de **Programação Orientada a Objetos (POO)**.

## 🚀 Como Jogar
Execute o arquivo principal para começar a partida:
```bash
python POO-Projetc/main.py
```

## 🧠 Conceitos de POO Aplicados

O projeto foi estruturado de forma modular, dividindo as regras do jogo do arquivo principal de execução. Durante a construção, aplicamos os seguintes pilares da Orientação a Objetos:

### 1. Classes e Objetos
Criamos os "moldes" (Classes como `Personagem`, `Heroi`, `Inimigo` e `Jogo`) que definem atributos e comportamentos. Durante a execução no `main.py`, nós "damos vida" a esses moldes criando instâncias reais (Objetos) para batalhar.

### 2. Encapsulamento
Protegemos os dados sensíveis do projeto. Atributos como pontuação e nível foram definidos como privados (ex: `self.__vida`). Isso garante que eles não sejam alterados acidentalmente de fora da classe. O acesso e a perda de vida só ocorrem de forma segura através de métodos controlados (como `receber_dano()`).

### 3. Herança
Eliminamos a repetição de código criando a classe base `Personagem`. Através dela, as subclasses `Heroi` e `Inimigo` herdam perfeitamente os atributos comuns (nome, vida, nível) e métodos (como `atacar`). O código fica muito mais limpo.

### 4. Polimorfismo
Trata-se da capacidade de modificar o comportamento de uma função herdada. O método `exibir_detalhes()` pertence à classe mãe, mas foi reescrito (sobrescrito) dentro do `Heroi` e `Inimigo` utilizando a função `super()`, permitindo que cada classe adicione informações diferentes na mesma chamada de método.

### 5. Interação entre Objetos
Demonstramos a comunicação entre diferentes entidades em campo. Nos métodos de combate, passamos os próprios objetos (como a variável `alvo`) como parâmetro. Isso permite que a classe de quem ataca interaja e subtraia a vida da classe de quem se defende dinamicamente.
