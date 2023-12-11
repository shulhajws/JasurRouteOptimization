import numpy as np
from bestRoute import bestRouteWithEndLoc, bestRoute

self = 0
locationData = np.array([
    [self, 1.8, 0.5, 1.4, 1.2, 6.1, 1.6, 2.9, 6, 0.85],
    [2.1, self, 1.7, 3.4, 3.3, 4.8, 1, 4.3, 8.2, 2.1],
    [0.45, 1.3, self, 1.7, 1.6, 5.6, 1.1, 3, 5.5, 1],
    [1.5, 2.8, 1.5, self, 0.6, 7.1, 2.7, 2.2, 7.1, 0.6],
    [1.3, 3, 1.8, 0.2, self, 7.4, 2.9, 2.5, 7.3, 0.85],
    [6.4, 4.8, 5.9, 7.6, 7.6, self, 5.3, 8.6, 0.35, 6.9],
    [1.6, 1, 1.2, 2.9, 2.8, 5.3, self, 3.4, 5.2, 2.1],
    [3.3, 3.9, 3, 2.8, 2.7, 8.3, 3.4, self, 8.2, 2.1],
    [6, 8.2, 5.6, 7.3, 7.2, 0.35, 5.3, 8.2, self, 6.5],
    [0.85, 2.1, 0.95, 1.1, 1, 6.5, 2, 2.1, 6.4, self]
])
locationNames = ["Purwakarta Station", 
                "Mie Gacoan", 
                "Yogya Department Store", 
                "Pasar Rebo Market",
                "Baso Cepot",
                "STS Sadang Square",
                "Al Ghazali Primary School",
                "Sambal Hejo SHSD Restaurant",
                "Sadang Sari Housing Complex",
                "R.E. Martadinata Road (House)"]

#Initialization
print("""
================== JASUR ROUTE OPTIMIZATION ================== 

Services and Locations:
1. Drive from/to Purwakarta Station
2. Buy food in Mie Gacoan
3. Purchase in Yogya Department Store
4. Purchase in Pasar Rebo Market
5. Purchase in Baso Cepot
6. Purchase in STS Sadang Square
7. Drive from/to Al Ghazali Primary School
8. Buy food in Sambal Hejo SHSD Restaurant
9. Drive from/to Sadang Sari Housing Complex
10. Drive from/to R.E. Martadinata Road (House)
""")

locationStopList = []
endLoc=-1

#Selecting Locations To Visit
numLocVisited = int(input("How many stops do you have to make? "))
for i in range(1, numLocVisited+1):
    locationStop = int(input("Location " + str(i) +": "))
    if (locationStop == 1) or (locationStop == 7) or (locationStop == 9) or (locationStop == 10):
        isEnd = input("Do you need to visit this location as the end location? (y/n) ")
        if(isEnd=="y"):
            endLoc = locationStop-1
        else:
            locationStopList.append(locationStop-1)            
    else:
        locationStopList.append(locationStop-1)
if(endLoc!=-1):
    locationStopList.append(endLoc)

#Selecting Start Location
startLoc = int(input("Hi, courier! Where are you now? "))
locationStopList = [startLoc-1] + locationStopList

#Going Back to Start Location
isBack = input("Do you need to go back to your starting location? (y/n) ")

#Getting Locations Graph
filteredLocationData = locationData[locationStopList][:, locationStopList]

#Performing TSP by Nearest Neighbor
if(isBack=="y"):
    if(endLoc!=-1):
        route, sumDistance = bestRouteWithEndLoc(filteredLocationData, True, endLoc)
    else:
        route, sumDistance = bestRoute(filteredLocationData, True)
else:
    if(endLoc!=-1):
        route, sumDistance = bestRouteWithEndLoc(filteredLocationData, False, endLoc)
    else:
        route, sumDistance = bestRoute(filteredLocationData, False)

print()
print("For efficiency, the best route for you to drive is: ")
print(locationNames[startLoc-1], end="")
for i in range(len(route)-1):
    print(f" -> {locationNames[locationStopList[route[i]-1]]}", end="")
if(isBack=="y"):
    print(f" -> {locationNames[startLoc-1]}", end="")
    
print()
print(f"The total distance you will travel is {sumDistance:.2f}.\n")
print()

