import json
with open("Knowledge.json", "r") as knowledge_file:
  data = json.load(knowledge_file)

def getTreatementsFor(Disease):
  #returns a list of all available treatements for the given Disease
  diseases = data.get("Diseases")
  drugs = data.get("Drugs")
  for d in diseases:
    if Disease in d.get("DiName"):#Find Disease
      drugs_for = [drug.get("DrID") for drug in d.get("Drugs")] #get drug ids
      break
  if 'drugs_for' not in locals(): #disease not in database
    return []
  result = [drug.get("DrName") if drug.get("DrID") in drugs_for else result for drug in drugs]
  return result
def getBestTreatementFor(Disease):
  #returns the best treatement for the given Disease
  diseases = data.get("Diseases")
  drugs = data.get("Drugs")
  for d in diseases:
    if Disease in d.get("DiName"):#Find disease
      drugs_for = d.get("Drugs")#Get medications for
      break
  if 'drugs_for' not in locals(): #disease not in database
    return ""
  result = drugs_for[0]
  for d in drugs_for:#Find best medication
    if d.get("Effectiveness") > result.get("Effectiveness"):
      result = d
  for d in drugs:
    if d.get("DrID") == result.get("DrID"):
      result = d.get("DrName")
      break
  return result
def getSymptomsof(Disease):
  #TODO
  return []
def getDiseaseFrom(Symptoms):
  #TODO
  return "Death"
def getUsedForDiseases(Drug):
  #TODO
  return "Living"


print(getBestTreatementFor('Myocardial Infarcation'))