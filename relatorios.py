# relatorios.py
# Exibição de relatórios operacionais.
# Todas as funções recebem os dados por parâmetro: nenhum contador fica guardado aqui.

import config
from financeiro import formatar_moeda, calcular_media, calcular_valor

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
    """mostra o faturamento total, as saídas e a média por saída."""
    media = calcular_media(faturamento, saidas)

    print("\n======= FATURAMENTO =======\n")
    print(f"Total arrecadado:   {formatar_moeda(faturamento)}")
    print(f"Saídas registradas: {saidas}")
    print(f"Média por saída:    {formatar_moeda(media)}")
    print("\n" + "=" * 33)


def exibir_relatorio(entradas, saidas, ocupadas, faturamento):
    """mostra o resumo de todas as movimentações."""
    disponiveis = config.CAPACIDADE_MAXIMA - ocupadas

    print("\n====== RELATORIO SMARTPARK ======\n")
    print(f"Total de entradas:      {entradas}")
    print(f"Total de saídas:        {saidas}")
    print(f"Veículos estacionados:  {ocupadas}")
    print(f"Vagas disponíveis:      {disponiveis}")
    print(f"Faturamento:            {formatar_moeda(faturamento)}")
    print("\n" + "=" * 33)


def exibir_tabela_precos():
    """mostra a tarifa e simula valores de 1 até 5 horas."""
    print("\n======= TABELA DE PREÇOS =======\n")
    print(f"Tarifa por hora: {formatar_moeda(config.TARIFA_POR_HORA)}")
    print(f"Funcionamento: {config.HORARIO_ABERTURA:02d}h às {config.HORARIO_FECHAMENTO}h")
    print(f"Permanência mínima cobrada: {config.PERMANENCIA_MINIMA} hora\n")

    for hora in range(1, config.HORAS_SIMULACAO + 1):
        valor = calcular_valor(hora)
        print(f"{hora} hora(s) -> {formatar_moeda(valor)}")

    print("\n" + "=" * 33)


def exibir_comprovante(horas, valor, ocupadas):
    """comprovante de saída."""
    print("\n======= COMPROVANTE DE SAÍDA =======\n")
    print(f"Tempo de permanência: {horas} hora(s)")
    print(f"Tarifa por hora:      {formatar_moeda(config.TARIFA_POR_HORA)}")
    print(f"Valor pago:           {formatar_moeda(valor)}")
    print(f"Vagas disponíveis:    {config.CAPACIDADE_MAXIMA - ocupadas}")
    print("\n" + "=" * 33)


def exibir_resumo_final(entradas, saidas, faturamento):
    """resumo exibido ao encerrar o sistema."""
    print("\n======= RESUMO FINAL =======\n")
    print(f"Total de entradas: {entradas}")
    print(f"Total de saídas:   {saidas}")
    print(f"Faturamento :       {formatar_moeda(faturamento)}")
    print("\n" + "=" * 33)

