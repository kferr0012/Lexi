from cmath import exp
import pandas as pd
from may_treat_lookup import *

disease_cui_df = pd.read_csv("../data/Lexi_data/Diseases_Cui.csv",sep="|")
may_treat_df = pd.read_csv("../data/Lexi_data/May_Treat.csv",sep="|")
pref_medicine_df= pd.read_csv("../data/Lexi_data/Pref-Medicine_Cui.csv",sep="|")

def translate_medication_CUI_to_name_test():

    print("=====================================================")
    print("Testing Function : translate_medication_CUI_to_name")
    print("==================================================")

    # Case 1 : CUI in CUI column of pref_medicine
    input=["C0000294","C0000378"]
    expected_result=[
        "mesna",
        "product containing mesna (medicinal product)",
        "product containing mesna",
        "mesna product",
        "mesna (product)",
        "mesna (substance)",
        "msa",
        "mesna (medication)",
        "droxidopa",
        "droxidopa (medication)",
        "product containing droxidopa",
        "product containing droxidopa (medicinal product)",
        "droxidopa product",
        "droxidopa (product)",
        "droxidopa (substance)"
    ]

    result = translate_medication_CUI_to_name(input)
    result = set(result)
    expected_result = set(expected_result)

    if result == expected_result:
        print("Test Case 1 Succeeded")
    else:
        print("Test Case 1 Failed with result : " + str(result-expected_result) + str(expected_result-result))

    #Case 2 : CUI not in CUI column of pref_medicine
    if translate_medication_CUI_to_name(["dummyinput"]) == -2:
        print("Test Case 2 Succeeded")
    else:
        print("Test Case 2 Failed")
  



def main():
    translate_medication_CUI_to_name_test()
    return

if __name__=="__main__":
    main()