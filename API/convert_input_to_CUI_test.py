import pandas as pd
from may_treat_lookup import *

disease_cui_df = pd.read_csv("../data/Lexi_data/Diseases_Cui.csv",sep="|")
may_treat_df = pd.read_csv("../data/Lexi_data/May_Treat.csv",sep="|")
pref_medicine_df= pd.read_csv("../data/Lexi_data/Pref-Medicine_Cui.csv",sep="|")

def convert_input_to_CUI_test():

    print("==========================================")
    print("Testing Function : convert_input_to_CUI")
    print("==========================================")

    # Case 1, User Input is in the dataframe 
    output = convert_input_to_CUI("abdominal pain")
    if output == "C0000737":
        print("Test Case 1 Succeeded")
    else:
        print("Test Case 1 Failed")

    # Case 2, User Input is not in the dataframe
    if convert_input_to_CUI("RandomString") == -2:
        print("Test Case 2 Succeeded")
    else:
        print("Test Case 2 Failed")

def main():
    convert_input_to_CUI_test()
    return

if __name__=="__main__":
    main()