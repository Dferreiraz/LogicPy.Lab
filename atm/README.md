# ATM Simulator (Simulador de Caixa Eletrônico)

Um simulador de caixa eletrônico desenvolvido em Python, executado diretamente no terminal (CLI). O projeto tem como objetivo praticar lógica de programação, regras de negócio, gerenciamento de saldo e validação de entradas, simulando operações financeiras básicas de forma simples e interativa.

## Funcionalidades

- **Consultar Saldo:** Exibe o saldo atual da conta.
- **Depositar:** Permite adicionar valores válidos ao saldo.
- **Sacar:** Realiza saques, verificando se o saldo disponível é suficiente.
- **Menu Interativo:** Permite navegar entre as operações até que o usuário decida encerrar a sessão.
- **Validação de Entradas:** Trata entradas inválidas, como letras e valores negativos.
- **Formatação Monetária:** Exibe os valores financeiros de maneira organizada.

## Conceitos Praticados

- **Lógica de Negócios:** Implementação das regras de depósito e saque.
- **Gerenciamento de Estado:** Atualização e manutenção do saldo durante a execução.
- **Validação de Dados:** Tratamento de entradas inválidas e restrições para operações financeiras.
- **Estruturas de Controle:** Utilização de condicionais e laços de repetição para controlar o fluxo da aplicação.
- **Organização de Código:** Separação das operações e organização da lógica do programa.
- **Interação via CLI:** Criação de menus e mensagens para interação com o usuário.
- **Formatação de Saída:** Apresentação clara dos valores monetários.

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
   cd LogicPy.Lab/atm
   ```

3. Execute o arquivo principal:

   ```bash
   python main.py
   ```

   Caso necessário, utilize `python3 main.py` no Linux ou macOS.

## Estrutura do Projeto

```text
atm/
└── main.py
```

## Objetivo do Projeto

Este projeto faz parte do **LogicPy.Lab**, um repositório dedicado à prática de lógica de programação e ao desenvolvimento de pequenos projetos utilizando Python. A proposta é consolidar os fundamentos da linguagem por meio de aplicações práticas e evolutivas.