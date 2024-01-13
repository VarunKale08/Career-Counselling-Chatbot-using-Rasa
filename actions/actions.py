from typing import Any, Text, Dict, List

from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher




class ActionGetUserGrade(Action):


   def name(self) -> Text:
       return "action_get_user_grade"


   def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


       g_level = tracker.get_slot("g_level")
       print("g_level:", g_level)
       message = ""
       if g_level.lower() in ["10th", "x", "tenth", "ten", "10"]:
           message = "So studying in 10th grade, may I know your marks to analyze your field of interest?" 
       elif g_level.lower() in ["12th", "xii", "twelfth", "twelve", "12"]:
           message = "So studying in 12th grade, may I know your marks to analyze your field of interest?"
       else:
           message = "I know that you are in {} grade but I'm here to guide 10th and 12th graders on their career paths. Ask me anything related to these academic levels!".format(g_level)
      
      
      
       dispatcher.utter_message(text=message)


       return []

# debugging for all subs  
# class ValidateForm(Action):
#     def name(self) -> Text:
#         return "action_validate_form"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         m_maths = tracker.get_slot("m_maths")
#         m_sci = tracker.get_slot("m_sci")
#         m_ss = tracker.get_slot("m_ss")
#         m_eng = tracker.get_slot("m_eng")
#         print("maths:", m_maths)
#         print("sci",m_sci)
#         print("ss",m_ss)
#         print("eng",m_eng)
        
#         if not all([m_maths is not None and m_maths != "",m_sci is not None and m_sci != "", m_ss is not None and m_ss != "", m_eng is not None and m_eng != ""]):
#             dispatcher.utter_message("Please fill in all required fields.")
#             return []


#         dispatcher.utter_message("Form submitted successfully!")
#         return []
    

class ValidateFormMaths(Action):
    def name(self) -> Text:
        return "action_validate_form_maths"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        m_maths = tracker.get_slot("m_maths")

        print("maths:", m_maths)

        
        if m_maths is None or m_maths == "":
            dispatcher.utter_message("I am unable to understand what you just said. Please provide appropriate information.")
            return []


        dispatcher.utter_message("Marks successfully recorded!")
        return []

class ValidateFormSci(Action):
    def name(self) -> Text:
        return "action_validate_form_sci"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        m_sci = tracker.get_slot("m_sci")

        print("Science:", m_sci)

        
        if m_sci is None or m_sci == "":
            dispatcher.utter_message("I am unable to understand what you just said. Please provide appropriate information.")
            return []


        dispatcher.utter_message("Marks successfully recorded!")
        return []
    
class ValidateFormSs(Action):
    def name(self) -> Text:
        return "action_validate_form_ss"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        m_ss = tracker.get_slot("m_ss")

        print("ss:", m_ss)

        
        if m_ss is None or m_ss == "":
            dispatcher.utter_message("I am unable to understand what you just said. Please provide appropriate information.")
            return []


        dispatcher.utter_message("Marks successfully recorded!")
        return []
    
class ValidateFormEng(Action):
    def name(self) -> Text:
        return "action_validate_form_eng"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        m_eng = tracker.get_slot("m_eng")

        print("eng:", m_eng)

        
        if m_eng is None or m_eng == "":
            dispatcher.utter_message("I am unable to understand what you just said. Please provide appropriate information.")
            return []


        dispatcher.utter_message("Marks successfully recorded!")
        return []


