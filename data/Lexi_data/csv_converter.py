import pandas as pd

Diseases_CUI_DF = pd.read_csv("./Diseases_Cui.csv",sep="|")
May_Treat_DF = pd.read_csv("./May_Treat.csv",sep="|")
Pref_Medicine_CUI_DF = pd.read_csv("./Pref-Medicine_Cui.csv",sep="|")

Diseases_CUI_DF.to_csv("Disease_Cui_CS.csv",index=False)
May_Treat_DF.to_csv("May_Treat_CS.csv",index=False)
Pref_Medicine_CUI_DF.to_csv("Pref-Medicine_CUI_CS.csv",index=False)