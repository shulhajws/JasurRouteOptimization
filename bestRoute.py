from typing import DefaultDict
INT_MAX = 2147483647

def bestRoute(locations, backToStartLoc):
    #Initialization
    sumDistance, counter, i, j = 0, 0, 0, 0
    min = INT_MAX
    route = [0] * (len(locations)-1)
    visitedLocationList = DefaultDict(int)
    visitedLocationList[0] = 1

    # Starting from the 0th indexed city i.e., the first city
    visitedLocationList[0] = 1
    route = [0] * len(locations)
 
    # Traverse the adjacency matrix locations[][]
    while i < len(locations) and j < len(locations[i]):
 
        # If it meets the end of traversing, which is in the corner of the Matrix
        if counter >= len(locations[i])-1 :
            break
 
        # If this path is unvisited then and if the 
        # cost is less then update the cost
        if j != i and (visitedLocationList[j] == 0):
            if locations[i][j] < min:
                min = locations[i][j]
                route[counter] = j + 1
        j += 1
 
        # If already check all the next cities, 
        # take the most minimum route and update the distance
        if j == len(locations[i]):
            sumDistance += min
            min = INT_MAX
            visitedLocationList[route[counter] - 1] = 1
            j = 0
            i = route[counter] - 1
            counter += 1

    # Add if get back to starting location
    if (backToStartLoc):
        i = route[counter - 1] - 1
        route[len(route)-1] = 1
        sumDistance += locations[i][0]

    return route, sumDistance

def bestRouteWithEndLoc(locations, backToStartLoc, endLoc):
    #Initialization
    sumDistance, counter, i, j = 0, 0, 0, 0
    min = INT_MAX
    route = [0] * (len(locations))
    visitedLocationList = DefaultDict(int)
    visitedLocationList[0] = 1

    # Starting from the 0th indexed city i.e., the first city
    visitedLocationList[0] = 1
 
    # Traverse the adjacency matrix locations[][]
    while i < len(locations)-1 and j < len(locations[i])-1:
 
        # If it meets the end of traversing, which is in the corner of the Matrix
        if counter >= len(locations[i])-1 -1:
            break
 
        # If this path is unvisited then and if the 
        # cost is less then update the cost
        if j != i and (visitedLocationList[j] == 0):
            if locations[i][j] < min:
                min = locations[i][j]
                route[counter] = j + 1
        j += 1
 
        # If already check all the next cities, 
        # take the most minimum route and update the distance
        if j == len(locations[i])-1:
            sumDistance += min
            min = INT_MAX
            visitedLocationList[route[counter] - 1] = 1
            j = 0
            i = route[counter] - 1
            counter += 1

    # Add end location
    if(endLoc!=-1):
        i = route[counter-1] -1
        route[len(route)-2]=len(route)
        sumDistance += locations[i][len(route)-1]
        counter += 1


    # Add if get back to starting location
    if (backToStartLoc):
        i = route[counter - 1] - 1
        route[len(route)-1] = 1
        sumDistance += locations[i][0]


    return route, sumDistance
