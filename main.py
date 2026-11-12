# main.py
# Menu principal e controle da execução do SmartPark.
# Versão inicial: estrutura do menu. As funcionalidades serão
# implementadas continuamentee

import config

def exibir_menu():
    """Mostra as opções do menu principal."""
    print("\n" + config.LINHA)
    print(f"        {config.NOME_SISTEMA} - SISTEMA")
    print(config.LINHA)
    print("1 - Registrar entrada de veículo")
    print("2 - Registrar saída de veículo")
    print("3 - Consultar vagas disponíveis")
    print("4 - Consultar faturamento")
    print("5 - Relatório de movimentações")
    print("6 - Consultar tabela de preços")
    print("0 - Encerrar sistema")
    print(config.LINHA)


def ler_opcao():
    """Lê a opção do menu. Retorna -1 se o usuário digitar algo que não é número."""
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("\n[ERRO] Digite apenas o número da opção.")
        return -1
    return opcao


def main():
    executando = True

    while executando:
        exibir_menu()
        opcao = ler_opcao()

        match opcao:
            case 1 | 2 | 3 | 4 | 5 | 6:
                print("\n[EM DESENVOLVIMENTO] Funcionalidade ainda não implementada.")

            case 0:
                print("\nObrigado por utilizar o SmartPark. Até logo!")
                executando = False

            case _:             # usando para controlar qualquer numero diferente do menu
                if opcao != -1:
                    print("\n[ERRO] Opção inválida! Escolha uma opção do menu.")


main()