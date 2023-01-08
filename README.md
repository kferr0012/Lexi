# Lexi: A Medical AI

## Summary :
#### Lexi is a medical artificial intelligence that uses a custom knowledge base system on its backend. This knowledge base is bootstrapped by the Unified Medical Language System and then supplemented with public sources of knowledge. Reputable websites related to medicine are identified and scraped, then information is extracted, curated, and added to the knowledge base. This work focuses on exposing endpoints to that knowledge in the form of a voice-based user interface, using Amazon's Alexa API. We envision multiple endpoints in the future like chatbost, document annotation, and even robotics.

## Design Graph 
![Image of DesignGraph2](/images/DesignGraph2.png)

## Current Features :
* Prescription Recommendation
    * As a doctor, I want Lexi to provide a prescription recommendation based on my patient's disease/illness.
* Definitions
    * As a doctor, I want Lexi to give me the definition of concepts. 

## Future Features : 
* Adverse Drug-to-Drug Detection
   * As a doctor, I want to be able to ask Lexi if there's any adverse interaction between a given list of drugs.
* Ask Mayo Clinic :
   * As a doctor, I want ask what Mayo Clinic says about a given drug.
   
## Terminology :
* Invocation Name :
    * The Invocation Name is used to launch Lexi through an Alexa or Amazon Astro endpoint.
* Intent :
    * A behavior/feature we want Lexi to perform.
* Utterance :
    * A command given by the user that instructs Lexi which Intent to perform.

## Usage :
* Start Lexi :
    * User says "launch medical bot"
    * (This is the Invocation Name, similar to saying "Alexa")
* Ask for a prescription recommendation :
    * User provides an utterance for Prescription Recommendation
    * (e.g. User says "My patient has a cold. What should I give him?")


