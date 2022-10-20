import pandas as pd 
Rebate_comercial = pd.read_excel("C:\\Users\daniel.costa\Regia Comércio de Informática Ltda\Controladoria Primetek - Documentos\Primetek\Auxiliar\REBATE COMERCIAL\Rebatecomercial_202208.xlsx",
sheet_name="COM IMEI", usecols=["FILIAL", "NF", "SERIE","CODIGO", "QUANTIDADE"])
print(Rebate_comercial.to_string())
print(Rebate_comercial.duplicated())