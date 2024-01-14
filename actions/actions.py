from typing import Any, Text, Dict, List
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import joblib
import os
import numpy as np

class CareerPredictionAction(Action):
    def name(self) -> Text:
        return "action_career_prediction"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the path to the Rasa project directory
        project_dir = os.path.dirname(os.path.abspath(__file__))

        # Specify the name of the model file
        model_filename = 'career_counseling_best_model_linear.joblib'

        # Create the full path to the model file
        model_path = os.path.join(project_dir, model_filename)
        svm_model = joblib.load(model_path)

        numerical_features = ['m_maths', 'm_sci', 'm_ss', 'm_eng']
        print("num features", numerical_features)

        # Extract numerical features from user input
        numerical_inputs = [float(tracker.get_slot(feature)) for feature in numerical_features]
        print("numerical input", numerical_inputs)

        # Reshape numerical_inputs to a 2D array
        numerical_inputs_2d = np.array(numerical_inputs).reshape(1, -1)

        # Predict using the loaded model
        predicted_career = svm_model.predict(numerical_inputs_2d)
        print("predicted career:", predicted_career)

        # Send the predicted career as a response
        dispatcher.utter_message(f"Thanks for sharing your marks, Based on your scores, I suggest considering a career in {predicted_career[0]}. However, it's important to note that there are various exciting career paths you can explore:\nScience Route: If you like subjects like Physics, Chemistry, Biology, or Math and are curious about the natural world, this is for you.\nCommerce Route: If you're interested in economics, business, and finance, this stream focuses on those areas.\nArts Route: If you enjoy literature, history, psychology, or creative arts, this stream is for subjects like those.\nFeel free to ask questions or seek advice about any of these career paths!")

        return []

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


