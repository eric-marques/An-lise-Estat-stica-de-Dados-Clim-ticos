🌦️ Análise Estatística de Dados Climáticos
Este projeto automatiza a extração e análise estatística de dados meteorológicos históricos para as cidades de Teresina, Fortaleza e São Paulo durante o primeiro trimestre de 2025. Desenvolvido como um trabalho universitário, o foco é a aplicação prática de medidas de tendência central e variabilidade em conjuntos de dados reais obtidos via API.

📋 Funcionalidades
O sistema está estruturado em dois módulos principais:

1. Extração de Dados (extração.py)
Integração com API: Consumo de dados históricos através da API Open-Meteo.

Resiliência: Implementação de sistema de cache (requests_cache) e políticas de tentativas automáticas (retry) para garantir a integridade da coleta.

Tratamento: Conversão de fuso horário local e estruturação dos dados em DataFrames organizados por cidade.

2. Processamento Estatístico (medidas.py)
Medidas de Posição: Cálculo de Média, Mediana, Mínimo, Máximo e Quartis (Q1 e Q3).

Análise de Dispersão: Cálculo de Variância, Desvio-Padrão e Coeficiente de Variação (CV) para comparar a estabilidade climática entre as regiões.

Detecção de Outliers: Identificação de anomalias climáticas usando o método de Amplitude Interquartílica (IQR).

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.13.

Manipulação de Dados: Pandas e Numpy.

Comunicação API: openmeteo-requests, requests-cache, retry-requests.

Visualização: Geração de Boxplots e Histogramas para análise gráfica.

📂 Estrutura do Projeto
extração.py: Script para coleta e geração da base bruta (dados_climaticos.csv).

medidas.py: Script para processamento estatístico e geração de relatórios (tabela_medidas.xlsx).

Gráficos: Visualizações automáticas de temperatura e precipitação.

🚀 Como Executar
Clone este repositório.

Instale as dependências:

Bash
pip install pandas numpy openmeteo-requests requests-cache retry-requests
Execute python extração.py para gerar a base de dados.

Execute python medidas.py para visualizar o resumo estatístico e os destaques.

Nota: Este repositório faz parte das entregas da disciplina de Estatística.
