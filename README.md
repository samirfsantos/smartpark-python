# SmartPark — Sistema de Controle de Estacionamento

Projeto da Fase 01 da disciplina **Programação Estruturada em Python**.

O SmartPark é um sistema de terminal que controla a entrada e a saída de veículos 
de um estacionamento, acompanha a ocupação das vagas, calcula as cobranças e 
apresenta o faturamento e um relatório das movimentações.


## Integrantes

Samir Freitas dos Santos - samirsantos@gmail.com
Gabriel Henrique Santos Araújo - gabriel.santos.araujo@maisunifacisa.com.br


## Funcionalidades

## Menu
1. **Registrar entrada** — verifica se há vaga, registra o veículo e informa as vagas restantes.
2. **Registrar saída** — pede as horas de permanência, calcula o valor, libera a vaga e emite um comprovante.
3. **Consultar vagas** — mostra capacidade, vagas ocupadas, vagas livres e taxa de ocupação.
4. **Consultar faturamento** — mostra o total arrecadado, as saídas e a média por saída.
5. **Relatório de movimentações** — resumo de entradas, saídas, ocupação e faturamento.
6. **Tabela de preços** — tarifa por hora e simulação de 1 a 5 horas.
0. **Encerrar** — exibe o resumo final e fecha o programa.


## Validações importantes

- Texto digitado no lugar de número é tratado com try/except e o usuário pode tentar de novo.
- Entrada com estacionamento lotado e saída com estacionamento vazio são recusadas.
- Permanência igual a zero ou negativa é rejeitada.
- Opção inexistente no menu exibe mensagem e volta ao menu.
- A média de faturamento não divide por zero quando não há saídas.


## Estrutura do projeto

SmartPark/<br>
├── main.py          # Menu principal e local onde vai ter da execução do projeto em si<br>
├── movimentacao.py  # Regras de entrada e saída de veículos<br>
├── financeiro.py    # Cálculos de cobrança e faturamento<br>
├── relatorios.py    # Exibição de relatórios operacionais<br>
├── config.py        # Constantes e configurações<br>
├── README.md        # Apresentação e instruções do projeto<br>
└── .gitignore       # Arquivos ignorados pelo Git<br>

Usar o Python **3.10 ou superior**

## Como executar


git clone https://github.com/samirfsantos/smartpark-python.git<br>
cd smartpark-python<br>
python main.py<br>

