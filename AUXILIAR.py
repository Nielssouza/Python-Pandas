import pandas as pd
# Lendo arquivo.
Auxiliar = pd.read_excel("C:\\Users\daniel.costa\Regia Comércio de Informática Ltda\Controladoria Primetek - Documentos\Primetek\Auxiliar\Auxiliar.xlsx", 
sheet_name="Rebate_DEP", usecols=["COD_ITEM","DEPARTAMENTO", "DATAINICIO", "DATAFIM", "REBATE"])
#print(Auxiliar.to_string())
print(Auxiliar.duplicated())
