# Bierzemy lekką wersję Pythona
FROM python:3.11-slim

# Tworzymy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy nasz kod do środka kontenera
COPY app.py .

# Instalujemy Flask
RUN pip install Flask

# Uruchamiamy aplikację
CMD ["python", "app.py"]
