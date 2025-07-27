"""
Aum Desai
Fall 2022
CS152B Project 06

This program is for Project 06.
You run it by putting python3 and the file name in the terminal. python3 elephant.py 0.43
It simulates the elephant population in Kruger National park, South Africa.
The result is a list of lists describing each elephant. 
It also gives the average population size, and average number of different elephant types.

"""

import sys
from numpy import average
import random as rand



IDXCalving_Interval = 0
IDXPercent_Darted = 1
IDXJuvenile_Age = 2
IDXMaximum_Age = 3
IDXProb_Calf_Survival = 4
IDXProb_Adult_Survival = 5
IDXProb_Senior_Survival = 6
IDXCarrying_Capacity = 7
IDXNum_Years = 8

IDXGender = 0
IDXAge = 1
IDXMonthsPregnant = 2
IDXMonthsContraceptiveRemaining = 3
 




def newElephant(parameters, age):
    	
    '''
    This function takes in 2 parameters and creates a new elephant list.
    '''

    elephant = [0,0,0,0]

    Gender = ['m','f']

    elephant[IDXGender] = rand.choice(Gender)
    elephant[IDXAge] = age

    if elephant[IDXGender] == 'f':

        if elephant[IDXAge] > parameters[IDXJuvenile_Age] and elephant[IDXAge] <= parameters[IDXMaximum_Age]:

            if rand.random() < 1.0/parameters[IDXCalving_Interval]:
                
                elephant[IDXMonthsPregnant] = rand.randint(1,22)

    return elephant



def initPopulation(parameters):

    '''
    This function takes in 1 parameter and returns a list of lists containing elephant data.
    '''

    population = []

    for elephant in range(parameters[IDXCarrying_Capacity]): 

        population.append(newElephant(parameters, rand.randint(1,parameters[IDXMaximum_Age])))

    return population



def incrementAge(population):

    '''
    This function takes in 1 parameter and increases the age of the elephants in the population by 1.
    Then it returns back the list.
    '''

    for elephant in range(len(population)):

        population[elephant][1] += 1

    return population


def calcSurvival(parameters, population):

    '''
    This function takes 2 parameters and determines which elephants survive. it then 
    returns the list.
    '''

    new_population = []

    for elephant in population:

        if elephant[1] == 1:

            if rand.random() < parameters[IDXProb_Calf_Survival]:

                new_population.append(elephant)

        elif elephant[1] > 1 and elephant[1] <=parameters[IDXMaximum_Age]:

            if rand.random() < parameters[IDXProb_Adult_Survival]:

                new_population.append(elephant)

        elif elephant[1] > parameters[IDXMaximum_Age]:

            if rand.random() < parameters[IDXProb_Senior_Survival]:

                new_population.append(elephant)

    return new_population


def dartElephants(parameters, population):

    '''
    This function takes in 2 parameters and determines whether a pregnant female elephant should
    be darted or not. then it returns the population list. 
    '''

    probability_Dart = parameters[IDXPercent_Darted]
    Juvenile_Age = parameters[IDXJuvenile_Age]
    Maximum_Age = parameters[IDXMaximum_Age]

    for elephant in population:

        if elephant[0] == 'f' and elephant[1] > Juvenile_Age and elephant[1] < Maximum_Age:

                if rand.random() < probability_Dart:

                    elephant[IDXMonthsPregnant] = 0
                    elephant[IDXMonthsContraceptiveRemaining] = 22
    
    return(population)


def cullElephants(parameters, population):

    '''
    This function takes 2 parameters and determines how many elephants to cull. Then it returns 
    the new population list.
    '''

    CarryingCap = parameters[IDXCarrying_Capacity]

    cullnum = len(population) - CarryingCap

    numCulled = cullnum

    if cullnum > 0:

        rand.shuffle(population)

        newPopulation = population[0:CarryingCap]

    else:

        newPopulation = population

    return(newPopulation, numCulled)

def controlPopulation( parameters, population ):

    '''
    This function takes 2 parameters and determines when to cull and dart.
    It returns the new population list and the number of elephants culled.
    '''

    # if the parameter value for "percent darted" is zero:
    if parameters[IDXPercent_Darted] == 0:

        # call cullElephants, storing the return values in a two variables
        (newpop,numCulled) = cullElephants(parameters,population)
    
    # else
    else:

        # call dartElephants and store the result in a variable named newpop
        newpop = dartElephants(parameters,population)

        # set a variable named numCulled to zero
        numCulled = 0

    #  return (newpop, numCulled)
    return(newpop,numCulled)


def simulateMonth(parameters, population):

    '''
    This function takes in 2 parameters and simulates what happens in 1 month.
    it then returns the population list. 
    '''

    CalvingInt = parameters[IDXCalving_Interval]
    JuvenileAge = parameters[IDXJuvenile_Age]
    MaxAge = parameters[IDXMaximum_Age]

    for e in population:

      
        gender = e[IDXGender]
        age = e[IDXAge]
        monthsPregnant = e[IDXMonthsPregnant]
        monthsContraceptive = e[IDXMonthsContraceptiveRemaining]

        if gender == 'f' and age > JuvenileAge:

            if monthsContraceptive > 0:

                e[IDXMonthsContraceptiveRemaining] -= 1

            elif monthsPregnant > 0:

                if monthsPregnant >= 22:

                    population.append(newElephant(parameters,1))

                    e[IDXMonthsPregnant] = 0

                else:

                    e[IDXMonthsPregnant] += 1

            else:

                if rand.random() < 1.0/(3.1*12-22):

                    e[IDXMonthsPregnant] = 1

    return(population)


def simulateYear(parameters, population):

    '''
    This function takes in 2 parameters and returns and simulates what occurs in 1 year 
    of an elephant population, then it returns the population list. 
    '''

    population = calcSurvival(parameters, population)

    population = incrementAge(population)

    for i in range(12):

        population = simulateMonth(parameters, population)

    return(population)


def calcResults(parameters,population,numCulled):

    '''
    This function takes in 3 parameters and determines the results of simulation.
    It calculates the number of calves, juveniles, adult males, adult females, and seniors. 
    '''

    JuvenileAge = parameters[IDXJuvenile_Age]
    MaxAge = parameters[IDXMaximum_Age]
    calves = 0
    juveniles = 0
    adult_males = 0
    adult_females = 0
    seniors = 0


    for e in population:

        if e[IDXAge] == 1:

            calves += 1
        
        if e[IDXAge] <= JuvenileAge and e[IDXAge] > 1:

            juveniles += 1

        if e[IDXAge] > JuvenileAge and e[IDXAge] < MaxAge and e[IDXGender] == 'm':

            adult_males += 1

        if e[IDXAge] > JuvenileAge and e[IDXAge] < MaxAge and e[IDXGender] == 'f':

            adult_females += 1

        if e[IDXAge] > MaxAge:

            seniors += 1

    result = [len(population), calves, juveniles, adult_males, adult_females, seniors, numCulled]

    return(result)


def runSimulation(parameters):

    '''
    This function takes in 1 parameter and determines how to run the simulation. It then returns the simulation
    results. 
    '''

    popsize = parameters[IDXCarrying_Capacity]

    population = initPopulation(parameters)

    [population,numCulled] =controlPopulation(parameters,population)

    results = []

    for i in range(parameters[IDXNum_Years]):

        population = simulateYear(parameters, population)

        [population,numCulled] = controlPopulation(parameters,population)

        results.append(calcResults(parameters,population,numCulled))

        if results[i][0] > 2 * popsize or results[i][0] == 0:

            #print('Terminating Early')

            break

    return(results)



def defaultParameters():

    '''
    This function simply holds the default parameters like storage box.
    It will return the list of default parameters whenever its called. 
    '''

    parameters = [3.1, 0.0, 12,60,0.85,0.996,0.20,1000,200]
    
    return parameters

def elephantSim(percDart, inputParameters = None):

    '''
    This functions runs the elephant simulation specifically using 2 arguments.
    It returns the average population. It is set up this way to optimize the probdart
    parameter.
    '''

    if inputParameters == None:

        parameters = defaultParameters()

    else:

        parameters = inputParameters

    parameters[IDXPercent_Darted] = percDart

    results = runSimulation(parameters)

    for i in range(4):

        results += runSimulation(parameters)

    totalpop = 0

    for i in range(len(results)):
        
        totalpop += results[i][0]

    avgPop = totalpop / len(results)

    ans = int(parameters[IDXCarrying_Capacity] - avgPop)

    return ans
    


def main(argv):

    '''
    This is the main function and it dictates what command line argument the user needs to input
    will put it and calculates how the results will be called upon after then simulation has
    run. 
    '''

    if len(argv) < 1:

        print('You must input a darting probability')

    probDart = float(argv[1])

    parameters = [3.1, probDart, 12,60,0.85,0.996,0.20,1000,200]

    results = runSimulation(parameters)

    print(results)

    totalpop = 0
    for i in range(len(results)):

        totalpop += results[i][0]

    averagepop = totalpop/ len(results)

    totalcalves = 0
    for i in range(len(results)):

        totalcalves += results[i][1]

    averagecalves = totalcalves/ len(results)

    totalJuv = 0
    for i in range(len(results)):

        totalJuv += results[i][2]

    averageJuv = totalJuv/ len(results)


    totalmales = 0
    for i in range(len(results)):

        totalmales += results[i][3]

    averagemales = totalmales/ len(results)

    totalfemales = 0
    for i in range(len(results)):

        totalfemales += results[i][4]

    averagefemales = totalfemales/ len(results)

    totalseniors = 0
    for i in range(len(results)):

        totalseniors += results[i][5]

    averageseniors = totalseniors/ len(results)

    totalcull = 0
    for i in range(len(results)):

        totalcull += results[i][6]

    averagecull = totalcull/ len(results)


    print('Average Population Size =',averagepop)
    print('Average Number of Calves =',averagecalves)
    print('Average Number of Juveniles =',averageJuv)
    print('Average Number of Males =',averagemales)
    print('Average Number of Females =',averagefemales)
    print('Average Number of Seniors =',averageseniors)
    print('Average Number of CulLed =',averagecull)


    
if __name__ == "__main__":
    main(sys.argv)
