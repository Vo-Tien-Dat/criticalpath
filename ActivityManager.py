"""
    Target: 
        manage all the activity
"""

import Activity
import Model
class ActivityManager():
    def __init__(self):
        self.activity_manager = {}

    def CreateActivity(self, activity_number: int, predecessor: [int], models: [Model]) -> Activity:
        newActivity = Activity(activity_number = activity_number, predecessor = predecessor, models = models)
        self.activity_manager[activity_number] = newActivity
        return self.activity_manager[activity_number]

    def getActivity(self, activity_number) ->  Activity:
        return self.activity_manager[activity_number]

    def getAllActivities(self):
        data = []
        for activity in self.activity_manager.values():
            data.append(activity)
        return data