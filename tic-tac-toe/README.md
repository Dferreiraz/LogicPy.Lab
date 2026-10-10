# Tic-Tac-Toe (Jogo da Velha)

Um jogo da velha desenvolvido em Python e executado diretamente no terminal (CLI), permitindo que dois jogadores disputem uma partida em turnos alternados. O projeto tem como objetivo praticar lógica algorítmica, manipulação de listas, gerenciamento de estado e validação de jogadas, implementando as regras clássicas do jogo.

## Funcionalidades

- **Tabuleiro Interativo:** Exibe o tabuleiro no terminal e atualiza sua representação a cada jogada.
- **Modo para Dois Jogadores:** Permite que dois jogadores se alternem utilizando os símbolos `X` e `O`.
- **Detecção de Vitória:** Identifica automaticamente combinações vencedoras em linhas, colunas e diagonais.
- **Detecção de Empate:** Reconhece quando todas as posições estão ocupadas sem que haja um vencedor.
- **Validação de Jogadas:** Impede a seleção de posições inválidas ou já ocupadas.
- **Nova Partida:** Permite iniciar outro jogo após o término da partida, sem reiniciar o programa.

## Conceitos Praticados

- **Manipulação de Listas e Índices:** Utilização de listas para representar o tabuleiro e acessar as posições selecionadas pelos jogadores.
- **Lógica Algorítmica:** Implementação de verificações para identificar combinações vencedoras e condições de empate.
- **Controle de Turnos e Estado:** Gerenciamento do jogador atual, da alternância de turnos e do andamento da partida.
- **Validação de Dados:** Tratamento de entradas inválidas e verificação da disponibilidade das posições.
- **Renderização no Terminal (ASCII):** Formatação do tabuleiro com caracteres para facilitar a visualização do jogo.
- **Estruturas de Controle:** Utilização de condicionais e laços de repetição para controlar o fluxo da partida.
- **Modularização:** Organização da lógica em funções para facilitar a leitura e a manutenção do código.

## Tecnologias Utilizadas

- **Python 3**
- **Biblioteca padrão do Python**

## Pré-requisitos

- Python 3 instalado na máquina.
- Terminal ou prompt de comando.

## Como Executar

1. Clone o repositório, caso ainda não tenha feito isso:

   ```bash
   git clone https://github.com/Dferreiraz/LogicPy.Lab.git
   ```

2. Acesse a pasta do projeto:

   ```bash
   cd LogicPy.Lab/tic-tac-toe
   ```

3. Execute o arquivo principal:

   ```bash
   python main.py
   ```

   Caso necessário, utilize `python3 main.py` no Linux ou macOS.

## Estrutura do Projeto

```text
tic-tac-toe/
└── main.py
```

## Objetivo do Projeto

Este projeto faz parte do **LogicPy.Lab**, um repositório dedicado à prática de lógica de programação e ao desenvolvimento de pequenos projetos utilizando Python. A proposta é consolidar os fundamentos da linguagem por meio de aplicações práticas e evolutivas.