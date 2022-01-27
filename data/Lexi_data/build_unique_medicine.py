import pandas as pd


Pref_Medicine_CUI_DF = pd.read_csv("./Pref-Medicine_Cui.csv",sep="|")

Pref_Medicine_CUI_DF = Pref_Medicine_CUI_DF.drop_duplicates(subset='CUI',keep="first")

# print(Pref_Medicine_CUI_DF)

Pref_Medicine_CUI_DF.to_csv("Unique_Pref-Medicine_CUI_CS.csv",index=False)