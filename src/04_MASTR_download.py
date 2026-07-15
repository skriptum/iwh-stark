# Dieses Skript lädt das Marktstammdatenregister (MaStR) herunter 
# und speichert die Daten in einer CSV-Datei
#
# open-MASTR: https://github.com/OpenEnergyPlatform/open-MaStR
# (c) Rainer-Lemoine-Institut, OFFIS, fortiss

#%%
from open_mastr import Mastr
from sqlalchemy import create_engine
import os

#%%
sqlite_engine = create_engine("sqlite:///../data/mastr/mastr.db", echo=False)
os.environ["OUTPUT_PATH"] = "../data/mastr/"
db = Mastr(engine=sqlite_engine)

#%%
# Big step, ca 35 min
db.download(data = ["wind", "solar", "storage", "combustion", "biomass"])

#%%
db.to_csv(tables = ["wind", "solar", "storage", "combustion", "biomass"])

