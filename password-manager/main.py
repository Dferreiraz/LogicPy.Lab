"""
Password Generator - Gerador de Senhas Seguras
Projeto desenvolvido para praticar:
- Manipulação de strings
- Módulos random e string
- Funções com parâmetros e retorno
- Loops e formatação de saída
"""

import random
import string


def gerar_senha(comprimento: int = 12, usar_especiais: bool = True) -> str:
    """Gera uma senha aleatória e segura."""
    caracteres = string.ascii_letters + string.digits
    
    if usar_especiais:
        caracteres += string.punctuation
    
    return "".join(random.choice(caracteres) for _ in range(comprimento))


def validar_comprimento(valor: str) -> int:
    """Valida e retorna o comprimento da senha."""
    try:
        comprimento = int(valor)
        if 6 <= comprimento <= 50:
            return comprimento
        print("[AVISO] O comprimento deve estar entre 6 e 50 caracteres. Usando padrão (12).")
        return 12
    except ValueError:
        print("[ERRO] Entrada inválida! Usando comprimento padrão (12).")
        return 12


def main() -> None:
    """Função principal do gerador de senhas."""
    print("\n" + "=" * 50)
    print("GERADOR DE SENHAS SEGURAS")
    print("=" * 50 + "\n")
    
    while True:
        try:
            quantidade = int(input("Quantas senhas você quer gerar? "))
            if 1 <= quantidade <= 20:
                break
            print("[AVISO] Por favor, digite um número entre 1 e 20.")
        except ValueError:
            print("[ERRO] Entrada inválida! Digite apenas números.")
    
    comprimento_input = input("Qual o tamanho da senha? (padrão: 12): ")
    comprimento = validar_comprimento(comprimento_input)
    
    especiais = input("Incluir caracteres especiais? (s/n) [padrão: s]: ").lower().strip()
    usar_especiais = especiais not in ['n', 'nao', 'não']
    
    print("\n" + "=" * 50)
    print("SENHAS GERADAS:")
    print("=" * 50)
    
    for i in range(quantidade):
        senha = gerar_senha(comprimento, usar_especiais)
        print(f"{i + 1}. {senha}")
    
    print("=" * 50)
    print("\n[DICA] Guarde suas senhas em um local seguro!")
    print("[AVISO] Nunca compartilhe suas senhas!\n")
    print("\n[SISTEMA] Obrigado por usar o LogicPy Password Manager. Até logo!")


if __name__ == "__main__":
    main()