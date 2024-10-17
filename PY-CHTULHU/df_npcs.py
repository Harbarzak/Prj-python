# Cargar los datos de los NPCs
import pandas as pd
df_npcs = pd.read_csv('npc.csv', on_bad_lines='skip')