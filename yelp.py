# -*- coding: utf-8 -*-
# CS111 PS06 Fall 2020
#
# Amanda Cheung / Alyssa Choi
# ac119 / ac111
# ps06- task 2
# October 7, 2020

# Working with dictionaries and tuples and real world data
# YELP data set covers different metropolitan areas in 4
# countries (not including Boston).

# ---------------------------------------------#
# DO NOT CHANGE ANYTHING IN THIS BLOCK OF CODE #
# ---------------------------------------------#
# This section loads in the dictionaries you will need for this pset

# Load in dictionaries stored as Python code
from miniDict import miniDict  # n=321
from mediumDict import mediumDict # n = 41878


#-----------------------#
# FUNCTIONS TO COMPLETE #                                                                           
#-----------------------#

def getBusinessCount(bizDict, businessName):
    '''
    Returns the number of times a business appears in a given dictionary.
    '''
    # TODO: Write me
    counter = 0
    for biz in bizDict:
        if bizDict[biz]["name"].lower() == businessName.lower():
            counter += 1
    return counter
    

def uniqueCities(bizDict):
    '''
    Returns a list of all the unique cities in a given dictionary.
    '''
    # TODO: Write me
    newList = []
    for biz in bizDict:
        if bizDict[biz]["city"] not in newList:
            newList.append(bizDict[biz]["city"])
    return newList
    

def findCategories(bizDict, cutoff):
    '''
    Returns a list of tuples, with each two-element tuple containing the
    category and the number of businesses that list that category, as long
    as the category occurs in the dictionary at or above the given cutoff.
    '''
    # TODO: Write me
    newList = []
    newDict = {}
    
    for biz in bizDict:
        for category in bizDict[biz]["categories"]:   
            newDict[category] = newDict.get(category, 0) + 1
    
    for item in newDict:
        if newDict[item] >= cutoff:
            newList.append((item, newDict[item]))
    
    return newList          
        

    
def findBusinesses(bizDict, category, city, starLimit, minReview):
    '''
    Returns a list of tuples of businesses (using the given category) with
    the name, address and number of stars for each business in the given city,
    at or exceeding starLimit, and at or exceeding the minimum number of reviews
    minReview.
    '''
    # TODO: Write me
    newList = []
    for biz in bizDict:
        if category in bizDict[biz]["categories"] and city == bizDict[biz]["city"] and starLimit <= bizDict[biz]["stars"] and minReview <= bizDict[biz]["review_count"]:
            newList.append((bizDict[biz]["name"], bizDict[biz]["address"], bizDict[biz]["stars"]))
    return newList



def bestPizzaPlace(bizDict):
    '''
    Returns the best pizza place as a list containing a tuple with the business
    name, address, city, and state.  The best pizza place is the one with the
    most number of stars and reviews. If they're tied, function returns
    both pizza places.
    '''
    # TODO: Write me

    bestPizzaPlace = []
    mostReviews = 0
    
    for biz in bizDict:
        star = bizDict[biz]["stars"]
        review = bizDict[biz]["review_count"]
        name = bizDict[biz]["name"]
        address = bizDict[biz]["address"]
        city = bizDict[biz]["city"]
        state = bizDict[biz]["state"]
        if "Pizza" in bizDict[biz]["categories"] and star == 5:
            if mostReviews < review:
                mostReviews = review
                bestPizzaPlace = [(name, address, city, state)]
            elif mostReviews == review:
                bestPizzaPlace.append((name, address, city, state))    
    return bestPizzaPlace

        

#---------------------------------------------#
# TESTING CODE - COMMENT AND UNCOMMENT THINGS #
#---------------------------------------------#
   
if __name__=="__main__":
    print("Start testing...")

#    howManyStarbucks = getBusinessCount(mediumDict,'Starbucks')
#    print("How many Starbucks?", howManyStarbucks)

#    miniCitiesList = uniqueCities(miniDict)
#    medCitiesList = uniqueCities(mediumDict)
#    print()
#    print("Minicities:", miniCitiesList)
#    print("Medcities:", medCitiesList)
 
#    whereToEatInLasVegas = findBusinesses(
#        mediumDict,
#        'Restaurants',
#        'Las Vegas',
#        5,
#        100
#    )
#    whereToShopInPhoenix = findBusinesses(
#        mediumDict,
#        'Shopping',
#        'Phoenix',
#        4,
#        100
#    )
#    print()
#    print("Where to eat in Las Vegas:", whereToEatInLasVegas)
#    print("Where to shop in Phoenix:", whereToShopInPhoenix)

#    miniCatD20 = findCategories(miniDict, 20)
#    print()
#    print("mini dict categories with more than 20 businesses: ")
#    print(miniCatD20)

#    mediumCatD500 = findCategories(mediumDict, 500)
#    print()
#    print("medium dict categories with more than 500 businesses: ")
#    print(mediumCatD500)

#    yummyPizza = bestPizzaPlace(miniDict)
#    superYummyPizza = bestPizzaPlace(mediumDict)
    print("End testing...")
