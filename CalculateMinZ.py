from gamspy import Container, Set, Alias, Parameter, Variable, Equation, Model, Sum, Sense
import numpy as np
import sys
import pandas as pd



#-----------------------------------------Read data from excel---------------------------------------    
def calculate(prefix_file_name_in:str = 'FILE_MIN_Z_'):
    result_object = [] 
    nDesiredIndividual = 20
    for index in range(nDesiredIndividual): 

        FOLDER_PATH = "./min_z/"
        PREFIX_FILE_NAME_IN = "FILE_MIN_Z_"
        SUFFIX_FILE_NAME_IN = index + 1
        file_name_out = PREFIX_FILE_NAME_IN + str(SUFFIX_FILE_NAME_IN) + '.xlsx'  
        tam = pd.read_excel(FOLDER_PATH + file_name_out)

        extracted_data = pd.DataFrame(columns=["Activity" , "C_ij" , "Max_S" , "Min_S"])

        extracted_data = pd.concat([extracted_data, pd.DataFrame(tam)], ignore_index = True)

        print(len(extracted_data["Activity"]))


        m = Container()

        H = 2300


        #-----------------------------------------Model sets and parameters---------------------------------
    #     activity = Set(container=m, name="sites", records=np.array([i for i in range(1, len(extracted_data["Activity"]) + 1)]))
    #     area = Set(container=m, name="mills", records=["value"])


    #     C_ij = Parameter(
    #         container=m, name="C_ij", domain=activity, records=np.array([float(i) for i in (extracted_data["C_ij"])])
    #     )

    #     max_S = Parameter(
    #         container=m, name="max_S", domain=activity, records=np.array([int(i) for i in (extracted_data["Max_S"])])
    #     )

    #     min_S = Parameter(
    #         container=m, name="min_S", domain=activity, records=np.array([int(i) for i in (extracted_data["Min_S"])])
    #     )


    #     #--------------------------------------------Constant-------------------------------------------
    #     x = Variable ( container = m , name = "d" , domain = activity , type = "positive" )

    #     e1 = Equation ( container = m , name = "eq1" , domain = activity )
    #     e1[ activity ] = x[ activity ] >= min_S[ activity ]

    #     e2 = Equation ( container = m , name = "eq2" , domain = activity )
    #     e2[ activity ] = x[ activity ] <= max_S[ activity ]


    #     #----------------------------------------------Objectivve function---------------------------------------
    #     Z = Sum([activity], H * x[activity]) + Sum([activity], C_ij[[activity]] * ( max_S[ activity ] - x[activity]))

    #     ans = Model ( container = m , name = "ans" , equations = m . getEquations () , problem = "LP" , sense =
    #     Sense . MIN , objective = Z )

    #     ans.solve()

    #     result_object.append(ans.objective_value)
    #     print(ans.objective_value)


    # res_fi = pd.DataFrame(result_object)

    # res_fi.columns =['Min_Z']
    # res_fi.to_excel('RESULT_MIN_Z.xlsx',  index=False)

    print(res_fi)
