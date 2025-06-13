import urllib.parse
from sqlalchemy import create_engine
import pandas as pd

# Mot de passe encodé
password = urllib.parse.quote_plus("@udrey29Le")

# Connexion sécurisée
engine = create_engine(f"postgresql://postgres:{password}@localhost:5432/education")

# Lecture des données
df = pd.read_sql("SELECT * FROM annuaire", engine)
print(df.head())

print("Connexion réussie. Nombre de lignes :", len(df))