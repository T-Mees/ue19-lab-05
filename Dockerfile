# Utiliser une image Python légère
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers locaux dans le conteneur
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Définir la commande à exécuter par défaut
CMD ["python", "app.py"]
