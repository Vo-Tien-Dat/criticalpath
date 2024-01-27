class Model():
    def __init__(self, model_number: int, values: {}):
        self.model_number = model_number
        self.values = values

class Activity():
    def __init__(self, activity_number: int, predecessor: [int], models: [Model]) -> None:
       self.activity_number = activity_number
       self.predecessor = predecessor
       self.models = models
       self.minModel = None

       self.pre_activities: [int] = predecessor
       self.next_activities: [int] = []

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