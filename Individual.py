"""
Target: 
    get all the activities in Individual
    get all the selected model of activities    
"""
from typing import Any
import Model
import Activity
class Individual():
    def __init__(self):
        self.activities: [Any] = []
        self.models: [Model] = []
        self.minZ = None

    def addActivityWithChoicedModel(self, activity: Activity, model: Model):
        if(activity is None):
            raise ValueError("Activity is None")

        if model is None:
            raise ValueError("Please provide a choiced model")

        self.activities.append(activity)
        self.models.append(model)