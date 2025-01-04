FROM python:3.11-slim

WORKDIR /app

# Kopírování requirements.txt pro instalaci závislostí
COPY requirements.txt requirements.txt

# Instalace závislostí z requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopírování všech souborů aplikace
COPY . .

# Exponování portu 5000
EXPOSE 5000

# Použití Gunicorn pro spuštění aplikace
CMD ["gunicorn", "-w", "4", "app:app", "--bind", "0.0.0.0:5000"]
