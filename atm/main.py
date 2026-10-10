"""
ATM Simulator - Simulador de Caixa Eletrônico
Projeto desenvolvido para praticar:
- Lógica de negócios e gerenciamento de estado (saldo)
- Validação de entrada e tratamento de erros
- Estruturação de menus e loops de controle
- Formatação de moeda e saída no terminal
"""

def exibir_menu() -> None:
    """Exibe as opções do menu principal."""
    print("\n" + "=" * 40)
    print("CAIXA ELETRÔNICO")
    print("=" * 40)
    print("[1] Consultar Saldo")
    print("[2] Depositar")
    print("[3] Sacar")
    print("[4] Sair")
    print("=" * 40)

def obter_valor(mensagem: str) -> float:
    """Solicita e valida um valor monetário positivo."""
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))
            if valor > 0:
                return valor
            print("[AVISO] O valor deve ser maior que zero.")
        except ValueError:
            print("[ERRO] Entrada inválida! Digite apenas números (ex: 50 ou 50.50).")

def consultar_saldo(saldo: float) -> None:
    """Exibe o saldo atual formatado."""
    print(f"\n[INFO] Seu saldo atual é: R$ {saldo:.2f}")

def depositar(saldo: float) -> float:
    """Realiza a operação de depósito."""
    print("\n--- DEPÓSITO ---")
    valor = obter_valor("Quanto deseja depositar? R$ ")
    saldo += valor
    print(f"[SUCESSO] Depósito de R$ {valor:.2f} realizado com sucesso!")
    return saldo

def sacar(saldo: float) -> float:
    """Realiza a operação de saque com validação de saldo."""
    print("\n--- SAQUE ---")
    valor = obter_valor("Quanto deseja sacar? R$ ")
    
    if valor > saldo:
        print("[ERRO] Saldo insuficiente! Operação cancelada.")
    else:
        saldo -= valor
        print(f"[SUCESSO] Saque de R$ {valor:.2f} realizado com sucesso!")
        
    return saldo

def main() -> None:
    """Ponto de entrada do simulador de caixa eletrônico."""
    saldo = 1000.00
    
    print("\n" + "=" * 40)
    print("Bem-vindo ao LogicPy Bank!")
    print(f"Saldo inicial: R$ {saldo:.2f}")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            consultar_saldo(saldo)
        elif opcao == '2':
            saldo = depositar(saldo)
        elif opcao == '3':
            saldo = sacar(saldo)
        elif opcao == '4':
            print("\n[SISTEMA] Obrigado por usar o LogicPy Bank. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida! Por favor, escolha entre 1 e 4.")

if __name__ == "__main__":
    main()