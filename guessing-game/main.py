"""
Guessing Game - Jogo de Adivinhação
Projeto desenvolvido para praticar:
- Estruturas de controle (while, if/elif/else)
- Geração de números aleatórios
- Validação de entrada do usuário
- Contadores e lógica de repetição
"""

import random


def obter_palpite() -> int:
    """Solicita e valida o palpite do usuário."""
    while True:
        try:
            palpite = int(input("Qual é o seu palpite? (1-100): "))
            if 1 <= palpite <= 100:
                return palpite
            print("[AVISO] Por favor, digite um número entre 1 e 100.")
        except ValueError:
            print("[ERRO] Entrada inválida! Digite apenas números inteiros.")


def jogar() -> None:
    """Função principal do jogo de adivinhação."""
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("\n" + "=" * 50)
    print("[INFO] Pensei em um número entre 1 e 100. Tente adivinhar!")
    print("=" * 50 + "\n")

    while True:
        palpite = obter_palpite()
        tentativas += 1

        if palpite == numero_secreto:
            print(f"\n[SUCESSO] Você acertou em {tentativas} tentativas!")
            print(f"[INFO] O número secreto era: {numero_secreto}")
            break
        elif palpite < numero_secreto:
            print("[DICA] Errou! O número secreto é MAIOR.")
        else:
            print("[DICA] Errou! O número secreto é MENOR.")
        
        if tentativas % 5 == 0:
            distancia = abs(palpite - numero_secreto)
            if distancia <= 10:
                print("[DICA] Você está MUITO perto!")
            elif distancia <= 25:
                print("[DICA] Você está perto!")
            else:
                print("[DICA] Você está longe!")
        print()


def main() -> None:
    """Ponto de entrada do programa."""
    jogar()
    
    while True:
        jogar_novamente = input("\nJogar novamente? (s/n): ").lower().strip()
        if jogar_novamente in ['s', 'sim']:
            print("\n" + "=" * 50)
            jogar()
        elif jogar_novamente in ['n', 'nao', 'não']:
            print("\n[SISTEMA] Obrigado por jogar o LogicPy Guessing Game! Até a próxima!")
            break
        else:
            print("[AVISO] Por favor, digite 's' para sim ou 'n' para não.")


if __name__ == "__main__":
    main()