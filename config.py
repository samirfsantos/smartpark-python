# config.py
# Constantes e configurações fixas do estacionamento SmartPark.
# Por convenção, constantes são escritas em LETRAS MAIÚSCULAS.

NOME_SISTEMA = "SMARTPARK"

CAPACIDADE_MAXIMA = 20          # quantidade total de vagas
TARIFA_POR_HORA = 5.00          # valor cobrado por hora
HORARIO_ABERTURA = 6            # abrindo às 06h
HORARIO_FECHAMENTO = 22         # fechando às 22h
PERMANENCIA_MINIMA = 1          # tempo mínimo cobrado

OCUPACAO_INICIAL = 0            # veículos estacionados ao iniciar
FATURAMENTO_INICIAL = 0.00      # faturamento ao iniciar

HORAS_SIMULACAO = 5             # tabela de preços simula de 1 até 5 horas

LINHA = "=" * 40                # usar isso para nao ter que escrever repetidamente na criacao do menu
