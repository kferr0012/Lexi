# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

#Import dependencies to access S3 bucket
import boto3

client = boto3.client('s3') #low-level functional API
resource = boto3.resource('s3') #high-level object-oriented API
my_bucket = resource.Bucket('d162c3e5-f455-4da0-96de-4668deafb2eb-us-east-1') #subsitute this for your s3 bucket name.

import pandas as pd


#3 Files 
#Disease CUI csv
obj1 = client.get_object(Bucket='d162c3e5-f455-4da0-96de-4668deafb2eb-us-east-1', Key='Media/Disease_Cui_CS.csv')
disease_cui_df = pd.read_csv(obj1['Body'])

#May Treat csv
obj2 = client.get_object(Bucket='d162c3e5-f455-4da0-96de-4668deafb2eb-us-east-1', Key='Media/May_Treat_CS.csv')
may_treat_df = pd.read_csv(obj2['Body'])

#Pref Medicine csv #Updated to filter CUIs on this file
obj3 = client.get_object(Bucket='d162c3e5-f455-4da0-96de-4668deafb2eb-us-east-1', Key='Media/Unique_Pref-Medicine_CUI_CS.csv')
pref_medicine_df=pd.read_csv(obj3['Body'])

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hi I am Lexi, your medical bot assistant."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "I didn't understand your input. Can you repeat that?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


#Kevin's Code
class PrescribeMedicationIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("prescribeMedicationIntent")(handler_input)
        
    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        diseaseType = slots["disease"].value
        
        #Dummy Response
        speak_output= "Disease detected " + diseaseType
        
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
        

        #Manage payload 
        try:
            medications = recommend_medication(diseaseType)
            
            if medications == -1 or medications == 1 or medications == -2 or medications == 2 or medications == -3 or medications == 3:
                speak_output += ". Couldn't find " + diseaseType + " in the database"
            else:
                speak_output += ". I recommend : "
                for med in medications:
                    if med != medications[-1]:
                        speak_output += med + ", "
                    else:
                        speak_output += med + "."
        except Exception as e:
            speak_output += ". Error detected when constructing output. "
            speak_output += str(e)
                
        
        
        # try:

        #     df = grid_sizes.loc[grid_sizes['STR1']==diseaseType,"STR2"]

        #     treatment = df.iloc[0]
            
        #     speak_output += ". The recommended treatment is " + treatment + "."
                
        # except:
        #     speak_output += ". Couldn't find " + diseaseType + " in the database."
        
        return(
            handler_input.response_builder.speak(speak_output).response
            )



# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(PrescribeMedicationIntentHandler()) #Added new handler
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()