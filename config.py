import os

# Configuració de Producció 
MAX_RETRIES = 3 

# Ara el token es llegeix de forma segura des de l'entorn
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")