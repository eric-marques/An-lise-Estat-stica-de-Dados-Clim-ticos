🌦️ Análise Estatística de Dados Climáticos (Trabalho 02)
Este repositório contém um projeto de automação para extração e análise estatística de dados meteorológicos históricos das cidades de Teresina, Fortaleza e São Paulo. O objetivo é aplicar conceitos de estatística descritiva sobre variáveis de temperatura e precipitação coletadas via API.

📋 Funcionalidades do Projeto
O fluxo de trabalho está dividido em duas etapas principais:

1. Extração e Tratamento (extração.py)
Consumo de API: Utiliza a API Open-Meteo para buscar dados históricos de latitude e longitude específicos.

Gerenciamento de Cache: Implementa requests_cache para evitar requisições redundantes e retry para garantir estabilidade em caso de falhas de conexão.

Estruturação de Dados: Converte as respostas da API em DataFrames do Pandas, ajustando fusos horários (America/Sao_Paulo) e formatos de data.

Exportação: Gera arquivos brutos nos formatos .csv e .xlsx.

2. Análise Estatística (medidas.py)
Cálculo de Medidas de Posição: Média, Mediana, Mínimo, Máximo e Quartis (Q1 e Q3).

Medidas de Variabilidade: Amplitude, Variância, Desvio-Padrão e Coeficiente de Variação (CV %).

Detecção de Outliers: Identificação automática de valores atípicos utilizando a técnica de Amplitude Interquartílica (IQR).

Relatórios Automáticos: O script imprime destaques no terminal (ex: cidade com maior temperatura) e salva uma tabela resumo consolidada.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.13.

Bibliotecas: * Pandas e Numpy (Processamento de dados).

Open-Meteo SDK (Interface da API).

Requests-cache & Retry-requests (Resiliência de rede).

📂 Estrutura de Arquivos
De acordo com o ambiente de desenvolvimento:

extração.py: Script de coleta de dados.

medidas.py: Script de processamento estatístico.

dados_climaticos.csv: Base de dados gerada após a extração.

tabela_medidas.xlsx: Relatório final com as métricas calculadas.

Gráficos: O projeto gera visualizações como boxplot_temperatura.png e hist_temperatura.png para suporte à análise.

🚀 Como Executar
Instale as dependências:

Bash
pip install pandas numpy openmeteo-requests requests-cache retry-requests
Execute a extração: python extração.py

Execute a análise: python medidas.py

Nota Acadêmica: Este projeto foi desenvolvido para a disciplina de Estatística, demonstrando a aplicação prática de medidas de tendência central e dispersão em dados reais.