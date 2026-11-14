from typing import Protocol

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

    media = financeiro.calcular_media(faturamento, saidas)

    print("\n ============FATURAMENTO=========")
    print(f"Faturamento total:   {financeiro.formatar_moeda(faturamento)}")
    print(f"Total de saidas: {saidas}")
    print(f"Média por saída: {financeiro.formatar_moeda(media)}")
    print("\n" "="* 30)

    aviso_em_desenvolvimento("Relatório de faturamento")


def exibir_relatorio(entradas, saidas, ocupadas, faturamento):

    print("\n==========RELATÓRIO DE MOVIMENTAÇÕES===========")
    print(f"Total de entradas: {entradas}")
    print(f"Total de saidas: {saidas}")
    print(f"Veículos estacionados: {ocupadas}")
    print(f"Faturamento: {financeiro.formatar_moeda(faturamento)}")
    print( "\n" "=" * 40)

    aviso_em_desenvolvimento("Relatório de movimentações")


def exibir_tabela_precos():

    print("========TABELA DE PREÇOS========")
    print(f"Tarifa por hora: {financeiro.formatar_moeda(config.TARIFA_POR_HORA)}")

    for horas in range (1,config.TARIFA_POR_HORA + 1):
        valor = financeiro.calcular_valor(horas)
        print(f"{horas} hora(s): {financeiro.formatar_moeda(valor)}")
print("\n" "=" * 33)

aviso_em_desenvolvimento("Tabela de preços")


def exibir_comprovante(horas, valor, ocupadas):

    print("=======COMPROVANTE DE SAÍDA=========")
    print(f"Horas de permanência: {horas}")
    print(f"Valor pago: {financeiro.formatar_moeda(valor)}")
    print(f"Vagas disponíveis: {disponiveis}")
    print("\n" "=" * 36)

    aviso_em_desenvolvimento("Comprovante de saída")


def exibir_resumo_final(entradas, saidas, faturamento):

    print("=========RESUMO FINAL SMARTPARK===========")
    print(f"Total de entradas: {entradas}")
    print(f"Total de saidas: {saidas}")
    print(f"Total de faturamento: {financeiro.formatar_moeda(faturamento)}")
    print(f"Média por saída: {financeiro.formatar_moeda(media)}")
    print("\n" "=" * 39)

    aviso_em_desenvolvimento("Resumo final")