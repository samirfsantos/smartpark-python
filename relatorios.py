import config
import financeiro

def aviso_em_desenvolvimento(nome_relatorio):
    """Aviso padrão :-)"""
    print(f"\n[EM DESENVOLVIMENTO] {nome_relatorio} ainda não implementado.")


def exibir_vagas(ocupadas):
    """Mostra como tá a ocupação."""
    disponiveis = config.CAPACIDADE_MAXIMA - ocupadas
    percentual = ocupadas / config.CAPACIDADE_MAXIMA * 100

    print("\n======= CONTROLE DE VAGAS =======\n")
    print(f"Capacidade total:   {config.CAPACIDADE_MAXIMA}")
    print(f"Vagas ocupadas:     {ocupadas}")
    print(f"Vagas disponíveis:  {disponiveis}")
    print(f"Taxa de ocupação:   {percentual:.0f}%")

    if ocupadas >= config.CAPACIDADE_MAXIMA:
        print("\nLotado, pega o beco")
    else:
        print("\nCabe mais")

    print("\n" + "=" * 33)



def exibir_faturamento(faturamento, saidas):

    aviso_em_desenvolvimento("Relatório de faturamento")


def exibir_relatorio(entradas, saidas, ocupadas, faturamento):

    aviso_em_desenvolvimento("Relatório de movimentações")


def exibir_tabela_precos():

    aviso_em_desenvolvimento("Tabela de preços")


def exibir_comprovante(horas, valor, ocupadas):

    aviso_em_desenvolvimento("Comprovante de saída")


def exibir_resumo_final(entradas, saidas, faturamento):

    aviso_em_desenvolvimento("Resumo final")