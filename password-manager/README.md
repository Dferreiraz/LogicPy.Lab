# Password Manager (Gerador de Senhas Seguras)

Uma aplicação de linha de comando (CLI) desenvolvida em Python para gerar senhas aleatórias, personalizáveis e com diferentes níveis de complexidade. O projeto tem como objetivo praticar manipulação de strings, utilização de módulos nativos, criação de funções reutilizáveis e validação de parâmetros para a geração de senhas.

## Funcionalidades

- **Geração em Lote:** Permite gerar de 1 a 20 senhas em uma única execução.
- **Personalização de Comprimento:** Permite definir o tamanho das senhas entre 6 e 50 caracteres.
- **Nível de Complexidade:** Oferece a opção de incluir ou excluir caracteres especiais na composição das senhas.
- **Validação de Entradas:** Trata valores inválidos e parâmetros fora dos limites permitidos.
- **Formatação de Saída:** Exibe as senhas geradas de maneira organizada no terminal.

## Conceitos Praticados

- **Manipulação de Strings:** Utilização das constantes do módulo `string`, incluindo letras, dígitos e caracteres de pontuação.
- **Geração Aleatória:** Utilização do módulo `random` para selecionar caracteres durante a criação das senhas.
- **Funções e Parâmetros:** Criação de funções reutilizáveis com parâmetros configuráveis e valores padrão.
- **Validação de Dados:** Tratamento de exceções com `try/except` e verificação dos parâmetros informados pelo usuário.
- **Loops e Iteração:** Utilização de estruturas de repetição para gerar múltiplas senhas em sequência.
- **Organização de Código:** Separação das responsabilidades para facilitar a leitura e a manutenção do programa.
- **Interação via CLI:** Construção de uma interface textual para receber parâmetros e apresentar resultados.

## Tecnologias Utilizadas

- **Python 3**
- **Módulo `random`**
- **Módulo `string`**
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
   cd LogicPy.Lab/password-manager
   ```

3. Execute o arquivo principal:

   ```bash
   python main.py
   ```

   Caso necessário, utilize `python3 main.py` no Linux ou macOS.

## Estrutura do Projeto

```text
password-manager/
└── main.py
```

## Objetivo do Projeto

Este projeto faz parte do **LogicPy.Lab**, um repositório dedicado à prática de lógica de programação e ao desenvolvimento de pequenos projetos utilizando Python. A proposta é consolidar os fundamentos da linguagem por meio de aplicações práticas e evolutivas.