from config import TARIFA_POR_HORA, PERMANENCIA_MINIMA     # só precisa desses dois mesmo


def calcular_valor(horas):
    """Recebe as horas de permanência e retorna o valor a pagar."""
    # Garante a cobrança mínima de 1 hora
    if horas < PERMANENCIA_MINIMA:
        horas = PERMANENCIA_MINIMA
    return horas * TARIFA_POR_HORA


def calcular_media(faturamento, saidas):
    """Retorna o valor médio acumulado"""
    if saidas == 0:
        return 0.0
    return faturamento / saidas

# vai ser usada para arrumar o padrao do valor no relatório, colocando no padrão de real
def formatar_moeda(valor):
    """Converte um número para o formato R$ 0,00."""
    texto = f"{valor:.2f}"
    texto = texto.replace(".", ",")
    return "R$ " + texto
