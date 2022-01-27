# import pandas as pd

# disease_cui_df=pd.read_csv("../data/Lexi_data/Diseases_Cui.csv",sep="|")
# may_treat_df=pd.read_csv("../data/Lexi_data/May_Treat.csv",sep="|")
# pref_medicine_df=pd.read_csv("../data/Lexi_data/Pref-Medicine_Cui.csv",sep="|")


# Function 1
# Given a disease type string from user, find the respective CUI
# Return respective CUI : str
def convert_input_to_CUI(user_input):

    #Try to perform lookup
    try:
        # returns CUI in string format if found
        sub_df = disease_cui_df.loc[disease_cui_df["STR"]==user_input,"CUI"]
        # print(type(sub_df)) np array
        ans=sub_df.tolist()

        if len(sub_df)==0:
            return -2 #indicate not found

        return ans[0]

    except:
        # -1 to indicate error
        return -1

# Function 2
# Given a disease CUI (type string), find the CUIs of medications that may treat this disease
# Return a list of CUI's type : list[str]
def get_may_treat_CUIs(input_CUI):
    
    #Try to perform lookup
    try:
        sub_df = may_treat_df.loc[may_treat_df["CUI1"]==input_CUI,"CUI2"]
        list_of_CUI2s = sub_df.tolist()

        if len(list_of_CUI2s) > 0:
            return list_of_CUI2s
        else:
            return -2 #indicate not found
    except:
        # -1 to indicate error
        return -1

# Function 3
# Given a list of medication CUIs, find the string Medications of these CUIS
# Return a list of Medications type : list[str]
def translate_medication_CUI_to_name(list_of_medication_CUIs):
    
    #Try to perform lookup
    try:
        sub_df = pref_medicine_df.loc[pref_medicine_df["CUI"].isin(list_of_medication_CUIs),"STR"]
        list_of_medication_names = sub_df.tolist()

        if len(list_of_medication_names) == 0:
            return -2 #indicate not found
        else:
            return list_of_medication_names

    except:
        return -1 #indicate error

# Function 4
# Master function that combines Function [1,3]
# Receives input directly from Alexa
# Returns a list of medications list[str]
def recommend_medication(disease_input):
    CUI = convert_input_to_CUI(disease_input)
    if CUI == -1:
        return -1
    elif CUI == -2:
        return 1

    may_treat_CUIs = get_may_treat_CUIs(CUI)
    if may_treat_CUIs == -1:
        return -2
    elif may_treat_CUIs == -2:
        return 2

    list_of_medications = translate_medication_CUI_to_name(may_treat_CUIs)
    if list_of_medications == -1:
        return -3
    elif list_of_medications == -2:
        return 3

    return list_of_medications

  

def main():
    ans=recommend_medication("brain cancer")
    if ans == -1:
        print("Error at first function call")
    elif ans == 1:
        print("Not found at first funciton call")
    elif ans == -2:
        print("Error at second function call")
    elif ans == 2:
        print("Not found at second function call")
    elif ans == -3:
        print("Error at third function call")
    elif ans == 3:
        print("Not found at third function call")
    else:
        print(ans)

if __name__ == "__main__":
    main()