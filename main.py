import json
import ReadData as ReadData
import CriticalPath
import CalculateMinZ
import CalculateCrossOver
import pandas as pd

import Activity
import Individual
# configuration_package = open('package.json')
 
# data = json.load(configuration_package)


# FILE_NAME_INDIVIDUAL = data['sub_folder'][0]['individual']
# FILE_NAME_MIN_Z = data['sub_folder'][1]['min_z']
# # print(FILE_NAME_INDIVIDUAL)
# configuration_package.close()

N_DESIRED_INDIVIDUALS = 5

global individuals

def InitProgram():
    path_df = 'Dat-thesis.xlsx'
    df = pd.read_excel(path_df)
    ReadData.setData(df = df)
    data = ReadData.getData()
    activities: [Activity] = ReadData.convertDataFrameToActivities(data)
    ReadData.setMinModelOfEachActivity(activities)
    individuals = ReadData.InitPopulation(N_DESIRED_INDIVIDUALS, activities=activities)
    
    desiredIndividuals = []
    for individual in individuals:
        desiredIndividual = ReadData.getDesiredIndividual(individual)
        desiredIndividuals.append(desiredIndividual)
        


if __name__ == '__main__':

    InitProgram()

    # ReadData.run()
    # root.run()
    # calculate_min_z.calculate()
    # cross_over.run()
    