import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

# Configuração da sessão
cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://archive-api.open-meteo.com/v1/archive"

# ← confirme os nomes na mesma ordem das coordenadas
cidades = ["Teresina", "Fortaleza", "São Paulo"]

params = {
    "latitude":   [-5.0892, -3.7172, -23.5475],
    "longitude":  [-42.8019, -38.5431, -46.6361],
    "start_date": "2025-01-01",
    "end_date":   "2025-03-31",
    "daily": [
        "temperature_2m_mean",
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum"
    ],
    "timezone": "America/Sao_Paulo"  # ← sem isso as datas ficam em UTC
}

responses = openmeteo.weather_api(url, params=params)

frames = []
for i, response in enumerate(responses):
    daily = response.Daily()
    df = pd.DataFrame({
        "data":              pd.date_range(
                                start=pd.to_datetime(daily.Time(), unit="s", utc=True),
                                end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
                                freq=pd.Timedelta(seconds=daily.Interval()),
                                inclusive="left"
                             ).date,
        "cidade":            cidades[i],
        "temperatura_media": daily.Variables(0).ValuesAsNumpy(),
        "temperatura_max":   daily.Variables(1).ValuesAsNumpy(),
        "temperatura_min":   daily.Variables(2).ValuesAsNumpy(),
        "precipitacao":      daily.Variables(3).ValuesAsNumpy(),
    })
    frames.append(df)
    print(f"✅ {cidades[i]}: {len(df)} registros coletados")

base = pd.concat(frames, ignore_index=True)

print(f"\nTotal de linhas: {len(base)}")        # deve ser 270
print(f"\nDados faltantes:\n{base.isnull().sum()}")
print(f"\nPrimeiras linhas:\n{base.head()}")

base.to_csv("dados_climaticos.csv", index=False)
base.to_excel("dados_climaticos.xlsx", index=False)
print("\n✅ Arquivos CSV e XLSX salvos com sucesso!")