"""
Target: 
    Save all models in activity
    get all next activities
    get all previous activities
    gt activity number
    
"""

import Model

class Activity():
    def __init__(self, activity_number: int, predecessor: [int], models: [Model]) -> None:
       self.activity_number = activity_number
       self.predecessor = predecessor
       self.models = models
       self.minModel = None

       self.pre_activities: [int] = predecessor
       self.next_activities: [int] = []