from typing import Any, Text, Dict, List


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
  
class ValidateForm(Action):
    def name(self) -> Text:
        return "action_validate_form"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        m_maths = tracker.get_slot("m_maths")
        m_sci = tracker.get_slot("m_sci")
        m_ss = tracker.get_slot("m_ss")
        m_eng = tracker.get_slot("m_eng")
        print("maths:", m_maths)
        print("sci",m_sci)
        print("ss",m_ss)
        print("eng",m_eng)
        
        if not all([m_maths is not None and m_maths != "",m_sci is not None and m_sci != "", m_ss is not None and m_ss != "", m_eng is not None and m_eng != ""]):
            dispatcher.utter_message("Please fill in all required fields.")
            return []


        dispatcher.utter_message("Form submitted successfully!")
        return []
    

class ValidateFormMaths(Action):
    def name(self) -> Text:
        return "action_validate_form_maths"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        m_maths = tracker.get_slot("m_maths")
        print("maths:", m_maths)
        
        if not all([m_maths is not None and m_maths != ""]):
            dispatcher.utter_message("Please provide your maths marks properly.")
            return []
     
        return []

class ValidateFormScience(Action):
    def name(self) -> Text:
        return "action_validate_form_science"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        m_sci = tracker.get_slot("m_sci")
        print("sci",m_sci)
        
        if not all([m_sci is not None and m_sci != ""]):
            dispatcher.utter_message("Please provide your science marks properly.")
            return []
        
        return []


class ValidateFormSocialStudies(Action):
    def name(self) -> Text:
        return "action_validate_form_social_studies"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        m_ss = tracker.get_slot("m_ss")
        print("ss",m_ss)
        
        if not all([m_ss is not None and m_ss != ""]):
            dispatcher.utter_message("Please provide your social studies marks properly.")
            return []
        
        return []



class ValidateFormEnglish(Action):
    def name(self) -> Text:
        return "action_validate_form_english"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        m_eng = tracker.get_slot("m_eng")
        print("eng",m_eng)
        
        if not all([m_eng is not None and m_eng != ""]):
            dispatcher.utter_message("Please provide your english marks properly.")
            return []
  
        dispatcher.utter_message("Form submitted successfully!")
        return []










