"""
Tic-Tac-Toe - Jogo da Velha
Projeto desenvolvido para praticar:
- Manipulação de listas e mapeamento de índices
- Lógica algorítmica para verificação de vitória e empate
- Controle de turnos e validação de jogadas
- Renderização de interface no terminal (ASCII)
"""

def criar_tabuleiro() -> list:
    """Cria e retorna um tabuleiro vazio."""
    return [" " for _ in range(9)]

def exibir_tabuleiro(tabuleiro: list) -> None:
    """Imprime o tabuleiro formatado no terminal."""
    print("\n")
    print(f"  {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}  ")
    print(" ---+---+--- ")
    print(f"  {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}  ")
    print(" ---+---+--- ")
    print(f"  {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}  ")
    print("\n")

def verificar_vencedor(tabuleiro: list, jogador: str) -> bool:
    """Verifica se o jogador atual venceu o jogo."""
    vitorias = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(tabuleiro[i] == jogador for i in combo) for combo in vitorias)

def verificar_empate(tabuleiro: list) -> bool:
    """Verifica se o jogo terminou em empate."""
    return " " not in tabuleiro

def obter_jogada(tabuleiro: list, jogador: str) -> int:
    """Solicita e valida a posição da jogada do usuário."""
    while True:
        try:
            posicao = int(input(f"Jogador {jogador}, escolha uma posição (1-9): "))
            if 1 <= posicao <= 9:
                indice = posicao - 1
                if tabuleiro[indice] == " ":
                    return indice
                print("[AVISO] Posição já ocupada! Tente outra.")
            else:
                print("[AVISO] Digite um número entre 1 e 9.")
        except ValueError:
            print("[ERRO] Entrada inválida! Digite apenas números.")

def jogar_novamente() -> bool:
    """Pergunta ao usuário se deseja iniciar uma nova partida."""
    while True:
        resposta = input("\nDeseja jogar novamente? (s/n): ").lower().strip()
        if resposta in ['s', 'sim']:
            return True
        if resposta in ['n', 'nao', 'não']:
            return False
        print("[AVISO] Por favor, digite 's' para sim ou 'n' para não.")

def main() -> None:
    """Ponto de entrada do Jogo da Velha."""
    print("\n" + "=" * 40)
    print("JOGO DA VELHA")
    print("=" * 40)
    print("Instruções: As posições são numeradas de 1 a 9,")
    print("da esquerda para a direita, de cima para baixo.")
    
    while True:
        tabuleiro = criar_tabuleiro()
        jogador_atual = "X"
        jogo_ativo = True
        
        print("\n[SISTEMA] Novo jogo iniciado!")
        
        while jogo_ativo:
            exibir_tabuleiro(tabuleiro)
            indice = obter_jogada(tabuleiro, jogador_atual)
            tabuleiro[indice] = jogador_atual
            
            if verificar_vencedor(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"[SUCESSO] Jogador {jogador_atual} venceu!")
                jogo_ativo = False
            elif verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print("[INFO] O jogo terminou em empate!")
                jogo_ativo = False
            else:
                jogador_atual = "O" if jogador_atual == "X" else "X"
                
        if not jogar_novamente():
            print("\n[SISTEMA] Obrigado por jogar LogicPy Jogo da velha! Até a próxima.")
            break

if __name__ == "__main__":
    main()