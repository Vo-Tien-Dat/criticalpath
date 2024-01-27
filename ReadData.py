from typing import Any
import pandas as pd

from collections import deque

from typing import Optional, Text, Dict, List, Union, Iterable, Any
import numpy as np
import random
import os 

from Models import *



activity_manager = ActivityManager()


nDesiredIndividual = 20
path_df = 'Dat-thesis.xlsx'
df = pd.read_excel(path_df)


def setData(df):
    new_data = df.iloc[1::, ::].copy()
    global root_data
    root_data = new_data

def getData():
    return root_data


def convertDataFrameToActivities(df) -> [Activity]:
    new_data = df.iloc[1::, ::].copy()

    activities = []

    for index, value in new_data.iterrows():
        activity_number = value['Activity']
        predecessor = value['Predecessor']
        if(predecessor == '-'):
            predecessor =  []
        else:
            if(type(predecessor) == int):
                predecessor = [predecessor]
            else:
                predecessor = [ x for x in predecessor.split(',')]

        # Xử lý model của activity
        model_names = value[2::].index
        models = []
        modelSize = len(model_names)
        for i in range(0, modelSize, 2):
            costOfModel = value[model_names[i]]
            durationOfModel = value[model_names[i + 1]]
            if(costOfModel != '-' and durationOfModel != '-'):
                model = Model(model_number = (int(i/2) + 1), values = {
                    'Cost': costOfModel,
                    'Duration': durationOfModel
                })
            models.append(model)

        activity = activity_manager.CreateActivity(activity_number = int(activity_number), predecessor = predecessor, models = models)
        activities.append(activity)

    return activities

def format_data(df) -> [Activity]:
    new_data = df.iloc[1::, ::].copy()

    activities = []

    for index, value in new_data.iterrows():
        activity_number = value['Activity']
        predecessor = value['Predecessor']
        if(predecessor == '-'):
            predecessor =  []
        else:
            if(type(predecessor) == int):
                predecessor = [predecessor]
            else:
                predecessor = [ x for x in predecessor.split(',')]

        # Xử lý model của activity
        model_names = value[2::].index
        models = []
        modelSize = len(model_names)
        for i in range(0, modelSize, 2):
            costOfModel = value[model_names[i]]
            durationOfModel = value[model_names[i + 1]]
            if(costOfModel != '-' and durationOfModel != '-'):
                model = Model(model_number = (int(i/2) + 1), values = {
                    'Cost': costOfModel,
                    'Duration': durationOfModel
                })
            models.append(model)

        activity = activity_manager.CreateActivity(activity_number = int(activity_number), predecessor = predecessor, models = models)
        activities.append(activity)

    return activities



def GetMinDurationOfEachActivity(activity: Activity) -> Model:

    models: [Model] = activity.models
    modelSize = len(models)
    if(modelSize <= 0):
        return None
    else:
        res = models[0]
        for model in models:
            if(model.values['Duration'] < res.values['Duration']):
                res = model
        return res

def GetMinDurationOfActivities(activities: [Activity]) -> Activity:
    minModelOfActivity: Model = GetMinDurationOfEachActivity(activity=activities[0])
    minActivity = activities[0]
    for activity in activities:
        modelOfCurrentActivity: Model = GetMinDurationOfEachActivity(activity = activity)
        if(modelOfCurrentActivity is not None):
            minModelDuration = minModelOfActivity.values['Duration']
            currentModelDuration = modelOfCurrentActivity.values['Duration']
            if(minModelDuration > currentModelDuration):
                minModelOfActivity = modelOfCurrentActivity
                minActivity = activity
        else:
            print("Model of Activity is NULL")
    return minActivity


def setMinModelOfEachActivity(activities: [Activity]):
    for activity in activities:
        minModelOfActivity: Model = GetMinDurationOfEachActivity(activity= activity)
        activity.minModel = minModelOfActivity


def CreateDataset(nActivity):
    data = []
    for i in range(1, nActivity):
        # data.append(CreateActivity(i))
        activity_manager.CreateActivity(i)

    data = activity_manager.getAllActivities()
    return data

def CreateEachIndividual(activities: [Activity] = []) -> [Individual]:
    individual = Individual()
    for activity in activities:
        models = activity.models
        model = random.choice(models)
        # print(model.model_number)
        individual.addActivityWithChoicedModel(activity=activity, model=model)

    return individual

def CallbackOnlyModelNumberForEachActivity(model: Model):
    return {
        'model_number': model.model_number,
        'values': model.values}

def CallbackOnlyModelNumber(model: Model):
    return model.model_number

def InitPopulation(nDesiredIndividual: int = 30, activities: [Activity] = []) -> [Model]:
    activitiesSize = len(activities)
    if(activitiesSize == 0):
        raise ValueError("Please supply at least one Activity")

    if(nDesiredIndividual <= 0):
        raise ValueError("No existing the number of Population")

    nCreatedIndividualCount = 1
    individuals: [Individual] = []
    while(nCreatedIndividualCount <= nDesiredIndividual):
        individual = CreateEachIndividual(activities=activities)
        individuals.append(individual)
        activities = individual.activities
        models = individual.models
        nCreatedIndividualCount = nCreatedIndividualCount + 1

    return individuals


def printActivities(activities: [Activity]):
    for activity in activities:
        print('Activity ' + str(activity.activity_number) + ': \n')
        print(activity)
        print(activity.predecessor)
        models = activity.models
        for model in models:
            print(model.values)


def convertIndividualToDataFrame(individual: Individual, file_name: str = "undenified"):
    print(file_name)
    activities = individual.activities
    models = individual.models
    size = len(activities)

    data = {
        'Activity': [], 
        'Predecessor': [], 
        'Duration_of_normal_model': [], 
        'Cost_of_normal_model': [],
        'Duration_of_min_model': [],
        'Cost_of_min_model': [],
        'Mode_number': [],
        }
    for pos in range(0, size, 1):
      activity = activities[pos]
      model = models[pos]
      
      activity_number = activity.activity_number
      predecessors = activity.predecessor
      time = model.values['Duration']
      
      if(len(predecessors) == 0):    predecessors = '-'
      else: predecessors = ', '.join(str(x) for x in predecessors)
      
      data['Activity'].append(activity_number)
      data['Predecessor'].append(predecessors)
      data['Duration_of_normal_model'].append(str(time))

      min_model = activity.minModel
      data['Cost_of_min_model'].append(min_model.values['Cost'])
      data['Cost_of_normal_model'].append(model.values['Cost'])
      data['Duration_of_min_model'].append(min_model.values['Duration'])

      #Number mode
      data['Mode_number'].append(model.model_number)

    marks_data = pd.DataFrame(data)

    marks_data.to_excel(file_name,  index=False)
      

def getDesiredIndividual(individual: Individual) -> pd.DataFrame:
    activities = individual.activities
    models = individual.models
    size = len(activities)

    data = {
        'Activity': [], 
        'Predecessor': [], 
        'Duration_of_normal_model': [], 
        'Cost_of_normal_model': [],
        'Duration_of_min_model': [],
        'Cost_of_min_model': [],
        'Mode_number': [],
        }
    
    for pos in range(0, size, 1):
      activity = activities[pos]
      model = models[pos]
      
      activity_number = activity.activity_number
      predecessors = activity.predecessor
      time = model.values['Duration']
      
      if(len(predecessors) == 0):    predecessors = '-'
      else: predecessors = ', '.join(str(x) for x in predecessors)
      
      data['Activity'].append(activity_number)
      data['Predecessor'].append(predecessors)
      data['Duration_of_normal_model'].append(str(time))

      min_model = activity.minModel
      data['Cost_of_min_model'].append(min_model.values['Cost'])
      data['Cost_of_normal_model'].append(model.values['Cost'])
      data['Duration_of_min_model'].append(min_model.values['Duration'])

      #Number mode
      data['Mode_number'].append(model.model_number)

    marks_data = pd.DataFrame(data)

    return marks_data

# def run():
    
#     activities = format_data(df)

#     setMinModelOfEachActivity(activities = activities)
    

#     individuals: [Individual] = InitPopulation(nDesiredIndividual= nDesiredIndividual, activities= activities)
#     count = 1 
#     FOLDER_PATH = "./individuals/"
#     os.mkdir(FOLDER_PATH) 
#     PREFIX_FILE_NAME = "INDIVIDUAL_"
#     SUFFIX_FILE_NAME = count
#     for individual in individuals:
#       convertIndividualToDataFrame(individual, FOLDER_PATH + PREFIX_FILE_NAME + str(SUFFIX_FILE_NAME) + '.xlsx')
#       count = count + 1
#       SUFFIX_FILE_NAME = count


# run()
    