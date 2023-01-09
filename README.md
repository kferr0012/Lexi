# Lexi: A Medical AI

## Summary :
### Lexi is a medical artificial intelligence that uses a custom knowledge base system on its backend. This knowledge base is bootstrapped by the Unified Medical Language System and then supplemented with public sources of knowledge. Reputable websites related to medicine are identified and scraped, then information is extracted, curated, and added to the knowledge base. This work focuses on exposing endpoints to that knowledge in the form of a voice-based user interface, using Amazon's Alexa API. We envision multiple endpoints in the future like chatbots, document annotation, and even robotics.

## Design Graph 
![Image of DesignGraph2](/images/DesignGraph2.png)

### User Usagae :
* A user will be able to interact with Lexi through Amazon Alexa and Amazon Astro devices. The commands given by a user are passed from these devices to the middle layer, AWS Lambda, to handle business logic. Based on the user's input, AWS Lambda will perform the necessary queries from its knowledge sources and return natural language responses to the user. Currently, the main knowledge source being used is the Unified Medical Langauge System (UMLS) data contained in S3 buckets.

### Developer Usage :
* A developer will be able to interact with Lexi through endpoints exposed by AWS API Gateway. API Gateway will forward requests to a server hosted with AWS EC2. The Widget component exposes endpoints for querying knowledge from UMLS and provides querying capability for definitions and relationships of medical concepts.

## Current Features :
* Prescription Recommendation
    * As a doctor, I want Lexi to provide a prescription recommendation based on my patient's disease/illness.
* Definitions
    * As a doctor, I want Lexi to give me the definition of concepts. 

## Future Features : 
* Adverse Drug-to-Drug Detection :
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
    

## Docker Container for PyLucene Feature :
https://hub.docker.com/repository/docker/krferr/lexi_pylucene/general

## Relevant Docs :
https://www.nlm.nih.gov/research/umls/index.html


