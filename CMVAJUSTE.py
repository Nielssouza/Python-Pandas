import pandas as pd
Cmv_Ajuste = pd.read_excel("C:\\Users\daniel.costa\Regia Comércio de Informática Ltda\Controladoria Primetek - Documentos\Primetek\Auxiliar\Auxiliar.xlsx",
sheet_name="AJUSTECMV", usecols=["COD_ITEM", "EMPRESA", "NUM_DOC"])
print(Cmv_Ajuste.duplicated())
#print(Cmv_Ajuste.to_string)