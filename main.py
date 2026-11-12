# main.py
# Menu principal e controle da execução do SmartPark.

import config
from movimentacao import registrar_entrada, registrar_saida   # fiz assim por conta do que o professor fala no item 7, aí só vai poder chamar diretamente essas duas funcoes
import financeiro as fin                            # isso é só para importar normal e usar o nome mais curto
import relatorios as rel                            # isso é só para importar normal e usar o nome mais curto


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
    """Vai ler a opção do menu. Repete até o usuário digitar um número inteiro."""
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("[ERRO] Digite apenas o número da opção.")
        else:
            return opcao


def main():

    ocupadas = config.OCUPACAO_INICIAL
    total_entradas = 0
    total_saidas = 0
    faturamento = config.FATURAMENTO_INICIAL

    executando = True

    while executando:
        exibir_menu()
        opcao = ler_opcao()

        match opcao:
            case 1:
                # Só altera os contadores se a entrada foi aceita
                if registrar_entrada(ocupadas):
                    ocupadas = ocupadas + 1
                    total_entradas = total_entradas + 1

            case 2:
                horas = registrar_saida(ocupadas)
                # horas = 0 significa saída recusada: nada é alterado
                if horas > 0:
                    valor = fin.calcular_valor(horas)
                    ocupadas = ocupadas - 1
                    total_saidas = total_saidas + 1
                    faturamento = faturamento + valor
                    rel.exibir_comprovante(horas, valor, ocupadas)

            case 3:
                rel.exibir_vagas(ocupadas)

            case 4:
                rel.exibir_faturamento(faturamento, total_saidas)

            case 5:
                rel.exibir_relatorio(total_entradas, total_saidas, ocupadas, faturamento)

            case 6:
                rel.exibir_tabela_precos()

            case 0:
                rel.exibir_resumo_final(total_entradas, total_saidas, faturamento)
                print("\nObrigado por utilizar o SmartPark. Até logo!")
                executando = False

            case _:
                print("\n[ERRO] Opção inválida! Escolha uma opção do menu.")


main()
