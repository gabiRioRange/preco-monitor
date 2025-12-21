# 📊 Preço Monitor — Scraper de Preços com Exportação para Excel

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![Lib](https://img.shields.io/badge/Lib-Pandas%20|%20BS4%20|%20OpenPyXL-orange)

## 📝 Descrição Geral

O **Preço Monitor** é uma solução automatizada de Web Scraping (ETL) desenvolvida para monitorar preços de produtos em e-commerces. O sistema coleta dados em tempo real, trata as informações e as exporta para uma base histórica em Excel, permitindo a análise de variação de preços (De/Por) ao longo do tempo.

Projetado para ser resiliente e autônomo, o sistema inclui scripts de automação para execução diária via Agendador de Tarefas do Windows.

## 🎯 Objetivos e Funcionalidades

* **Monitoramento Completo:** Coleta **Preço Atual** e **Preço Antigo** (para identificar promoções reais).
* **ETL Automatizado:** Pipeline de limpeza que converte moedas (R$) e textos para números decimais (`float`).
* **Histórico Incremental:** O sistema não sobrescreve os dados; ele anexa novas leituras ao arquivo Excel existente (`append`), criando uma linha do tempo.
* **Automação Windows:** Inclui script `.bat` configurado para rodar em *background* via Task Scheduler.
* **Tratamento de Erros:** Logs de execução e blindagem contra falhas de conexão ou mudanças de layout (404/Timeout).

## 🛠 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Coleta:** `Requests` (Alta performance) e `BeautifulSoup4` (Parsing HTML).
* **Dados:** `Pandas` (Estruturação e Limpeza).
* **Persistência:** `OpenPyXL` (Manipulação avançada de Excel .xlsx).
* **Automação:** Batch Script (`.bat`) para Windows.

## 📂 Estrutura do Projeto

text

    preco-monitor/
    │
    ├── data/                   # Armazena o histórico (ignorada pelo Git)
    │   └── historico_precos.xlsx
    │
    ├── src/                    # Módulos do Sistema
    │   ├── scraper.py          # Extração (Requests/BS4)
    │   ├── cleaner.py          # Limpeza e Padronização (Pandas)
    │   └── exporter.py         # Salvamento Inteligente (OpenPyXL)
    │
    ├── config.py               # Configurações (URLs e Seletores CSS)
    ├── executar.bat            # Script para automação no Windows
    ├── main.py                 # Orquestrador principal
    ├── requirements.txt        # Dependências
    └── README.md               # Documentação

## 🆕 Melhorias Recentes

- **Logging Estruturado:** Logs salvos em `logs/preco_monitor.log` para rastreamento detalhado.
- **Retry com Backoff:** Tentativas automáticas em caso de falha, com espera exponencial para evitar sobrecarga.
- **Testes Unitários:** Cobertura básica com unittest em `tests/`.
- **Configuração Flexível:** Exemplos comentados para Amazon e Magazine Luiza.
- **Dashboard Web:** Interface simples com Streamlit para visualizar dados (`streamlit run dashboard.py`).

## 🚀 Como Usar
1. Instalação

Clone o repositório e instale as dependências:
Bash

    git clone [https://github.com/gabiRioRange/preco-monitor.git](https://github.com/gabiRioRange/preco-monitor.git)
    
    cd preco-monitor
    
    python -m venv .venv
# Ative a venv (Windows: .venv\Scripts\activate)
    pip install -r requirements.txt

2. Configuração (config.py)

Adicione os produtos que deseja monitorar no arquivo config.py. Você deve fornecer a URL e os Seletores CSS (Classes ou IDs) dos elementos da página:
Python

    URLS_ALVO = [
        {
            "loja": "Mercado Livre",
            "url": "https://...",
            "seletor_nome": "h1.ui-pdp-title",
            "seletor_preco": ".ui-pdp-price__second-line .fraction",
            "seletor_preco_antigo": ".ui-pdp-price__original-value .fraction"
        }
    ]

3. Execução Manual

Para rodar uma vez e testar:
Bash

    python main.py

Para executar os testes:
Bash

    python -m unittest discover tests/

Para visualizar o dashboard:
Bash

    streamlit run dashboard.py

4. Agendamento Automático (Windows)

Para rodar todo dia automaticamente:

    Abra o Agendador de Tarefas do Windows.

    Crie uma nova tarefa básica.

    Em "Ação", selecione Iniciar um programa.

    Aponte para o arquivo executar.bat que está na raiz do projeto.

    Importante: No campo "Iniciar em (Opcional)", coloque o caminho da pasta do projeto.

👤 Autor

Desenvolvido por Gabriel / gabiRioRange. Focado em Desenvolvimento Backend, Automação e Ciência de Dados com Python.
