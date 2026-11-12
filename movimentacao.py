# movimentacao.py
# Regras de entrada e saída de veículos.
# A ocupação atual é recebida do main por parâmetro (o config fornece apenas o valor inicial)
# e devolve o resultado da operação e quem vai atualizar/incrementar os contadores é o main tambem

# RF01 — Registrar entrada
# RF02 — Registrar saída

import config

def vagas_disponiveis(ocupadas):
    """Retorna quantas vagas ainda estão livres."""
    return config.CAPACIDADE_MAXIMA - ocupadas


def estacionamento_lotado(ocupadas):
    """Retorna True se não houver mais vagas."""
    return ocupadas >= config.CAPACIDADE_MAXIMA


def estacionamento_vazio(ocupadas):
    """Retorna True se não houver nenhum veículo estacionado"""
    return ocupadas <= 0

# RF01 Registrar entrada dos veiculos
def registrar_entrada(ocupadas):
    """
    Tenta registrar a entrada de um veículo olhando se esta lotado
    Retorna True se a entrada foi permitida e False se foi recusada
    """
    if estacionamento_lotado(ocupadas):
        print("\n[ERRO] Estacionamento lotado! Entrada não permitida")
        return False

    restantes = vagas_disponiveis(ocupadas + 1)
    print("\n[OK] Entrada registrada com sucesso!!!!")
    print(f"Vagas disponíveis: {restantes}")
    return True

# fazer as validacoes do item 8
def ler_horas_permanencia():
    """
    O sistema vai estar preparado para lidar com situações inesperadas!!!
    """
    while True:
        try:
            horas = int(input("Informe as horas de permanência: "))
        except ValueError:
            print("[ERRO] Digite apenas números inteiros. Tente novamente.")
        else:
            if horas <= 0:
                print("[ERRO] O tempo deve ser maior que zero. Tente novamente.")
            else:
                return horas
        finally:
            print("-" * 40)


def registrar_saida(ocupadas):
    """
    Tenta registrar a saída de um veículo.
    Retorna as horas de permanência se a saída for válida,
    ou 0 se a saída for recusada ja q o estacionamento vazio
    """
    if estacionamento_vazio(ocupadas):
        print("\n[ERRO] Não há veículos estacionados. Saída não permitida.")
        return 0

    horas = ler_horas_permanencia()
    return horas
