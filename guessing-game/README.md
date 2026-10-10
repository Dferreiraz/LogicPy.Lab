# Guessing Game (Jogo de Adivinhação)

Um jogo de adivinhação desenvolvido em Python e executado diretamente no terminal (CLI). O objetivo é descobrir um número secreto gerado aleatoriamente pelo sistema, utilizando os palpites e as dicas fornecidas durante a partida. O projeto tem como foco a prática de estruturas de controle, geração de números aleatórios, validação de entradas e organização de código.

## Funcionalidades

- **Geração Aleatória:** Seleciona um número secreto entre 1 e 100 para cada nova partida.
- **Feedback em Tempo Real:** Informa se o palpite é maior ou menor que o número secreto.
- **Contador de Tentativas:** Registra a quantidade de palpites realizados até o acerto.
- **Sistema de Dicas:** Fornece pistas sobre a proximidade dos palpites, conforme a lógica implementada no jogo.
- **Nova Partida:** Permite iniciar outra rodada sem precisar reiniciar o programa.
- **Validação de Entradas:** Trata valores inválidos, como letras e entradas fora do formato esperado.

## Conceitos Praticados

- **Estruturas de Controle:** Utilização de laços de repetição (`while`) e estruturas condicionais (`if`, `elif` e `else`) para controlar o fluxo do jogo.
- **Geração de Números Aleatórios:** Utilização do módulo `random` para gerar o número secreto.
- **Validação de Dados:** Tratamento de entradas inválidas para evitar erros durante a execução.
- **Gerenciamento de Estado:** Controle do número secreto, dos palpites e do contador de tentativas.
- **Modularização:** Organização da lógica em funções para facilitar a leitura, a manutenção e a reutilização do código.
- **Interação via CLI:** Desenvolvimento de uma interface textual interativa no terminal.

## Tecnologias Utilizadas

- **Python 3**
- **Módulo `random`**
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
   cd LogicPy.Lab/guessing-game
   ```

3. Execute o arquivo principal:

   ```bash
   python main.py
   ```

   Caso necessário, utilize `python3 main.py` no Linux ou macOS.

## Estrutura do Projeto

```text
guessing-game/
└── main.py
```

## Objetivo do Projeto

Este projeto faz parte do **LogicPy.Lab**, um repositório dedicado à prática de lógica de programação e ao desenvolvimento de pequenos projetos utilizando Python. A proposta é consolidar os fundamentos da linguagem por meio de aplicações práticas e evolutivas.