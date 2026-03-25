import pandas as pd
import numpy as np

# ── Carregar base ─────────────────────────────────────────────────
base = pd.read_csv("dados_climaticos.csv")
print("Cidades encontradas:", base["cidade"].unique())
print("Total de linhas:", len(base))

cidades = base["cidade"].unique()

# ── Função de cálculo ─────────────────────────────────────────────
def calcular_medidas(df, cidade, variavel, nome_variavel):
    dados = df[df["cidade"] == cidade][variavel].dropna()
    q1  = dados.quantile(0.25)
    q3  = dados.quantile(0.75)
    iqr = q3 - q1
    media = dados.mean()
    dp    = dados.std()
    outliers = int(((dados < q1 - 1.5*iqr) | (dados > q3 + 1.5*iqr)).sum())
    return {
        "Cidade":        cidade,
        "Variável":      nome_variavel,
        "Média":         round(media, 2),
        "Mediana":       round(dados.median(), 2),
        "Mínimo":        round(dados.min(), 2),
        "Máximo":        round(dados.max(), 2),
        "Q1":            round(q1, 2),
        "Q3":            round(q3, 2),
        "Amplitude":     round(dados.max() - dados.min(), 2),
        "Variância":     round(dados.var(), 2),
        "Desvio-Padrão": round(dp, 2),
        "CV (%)":        round((dp / media) * 100, 2),
        "Outliers":      outliers
    }

# ── Calcular para todas as cidades e variáveis ────────────────────
resultados = []
for cidade in cidades:
    resultados.append(calcular_medidas(base, cidade, "temperatura_media", "Temperatura Média (°C)"))
    resultados.append(calcular_medidas(base, cidade, "precipitacao",      "Precipitação (mm)"))

tabela = pd.DataFrame(resultados)

# ── Exibir resultado ──────────────────────────────────────────────
print("\n" + "="*80)
print("TABELA RESUMO — MEDIDAS DE POSIÇÃO E VARIABILIDADE")
print("="*80)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
print(tabela.to_string(index=False))

# ── Salvar ────────────────────────────────────────────────────────
tabela.to_excel("tabela_medidas.xlsx", index=False)
tabela.to_csv("tabela_medidas.csv", index=False)
print("\n✅ Tabela salva em tabela_medidas.xlsx e tabela_medidas.csv")

# ── Destaques para o artigo ───────────────────────────────────────
print("\n" + "="*80)
print("DESTAQUES PARA O ARTIGO")
print("="*80)

temp = tabela[tabela["Variável"] == "Temperatura Média (°C)"]
prec = tabela[tabela["Variável"] == "Precipitação (mm)"]

print(f"\n🌡️  Maior temperatura média:    {temp.loc[temp['Média'].idxmax(), 'Cidade']} ({temp['Média'].max()}°C)")
print(f"🌡️  Menor temperatura média:    {temp.loc[temp['Média'].idxmin(), 'Cidade']} ({temp['Média'].min()}°C)")
print(f"🌡️  Maior variabilidade (temp): {temp.loc[temp['CV (%)'].idxmax(), 'Cidade']} (CV = {temp['CV (%)'].max()}%)")

print(f"\n🌧️  Maior precipitação média:   {prec.loc[prec['Média'].idxmax(), 'Cidade']} ({prec['Média'].max()} mm)")
print(f"🌧️  Maior variabilidade (prec): {prec.loc[prec['CV (%)'].idxmax(), 'Cidade']} (CV = {prec['CV (%)'].max()}%)")

print(f"\n⚠️  CVs acima de 30%:")
altos = tabela[tabela["CV (%)"] > 30][["Cidade", "Variável", "CV (%)"]]
print(altos.to_string(index=False) if not altos.empty else "   Nenhum para temperatura")

print(f"\n📦 Outliers detectados:")
out = tabela[tabela["Outliers"] > 0][["Cidade", "Variável", "Outliers"]]
print(out.to_string(index=False) if not out.empty else "   Nenhum outlier detectado")