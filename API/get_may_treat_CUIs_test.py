import pandas as pd
from may_treat_lookup import *

disease_cui_df = pd.read_csv("../data/Lexi_data/Diseases_Cui.csv",sep="|")
may_treat_df = pd.read_csv("../data/Lexi_data/May_Treat.csv",sep="|")
pref_medicine_df= pd.read_csv("../data/Lexi_data/Pref-Medicine_Cui.csv",sep="|")

def get_may_treat_CUIs_test():

    print("==========================================")
    print("Testing Function : get_may_treat_CUIs")
    print("==========================================")

    # Case 1 : CUI is in CUI1 column of the file
    expected_result=["C0291771","C0291772","C2714632","C4704592"]
    result = get_may_treat_CUIs("C0000737")
    if  result == expected_result:
        print("Test Case 1 Succeeded")
    else:
        print("Test Case 1 Failed with return value : " + str(result))

    # Case 2 : CUI is not in the CUI1 column of thefile
    result = get_may_treat_CUIs("DummyString")
    if  result == -2: #-2 is used to indicate not found
        print("Test Case 2 Succeeded")
    else:
        print("Test Case 2 Failed with return value : " + str(result))

def main():
    get_may_treat_CUIs_test()
    return

if __name__=="__main__":
    main()