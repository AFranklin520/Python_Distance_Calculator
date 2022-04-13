# FranklinP6
# Programmer: Anthony Franklin
# Email: afranklin18@cnm.edu
# Purpose: demonstrate use of functions




#Test Case
#Santa Fe: 35.692512, -105.938750
#Albuquerque: 35.079204, -106.649776
#Distance 57.44 miles (straight line from Abq to Santa Fe on Google Maps)

 

from math import sin, cos, sqrt, atan2, radians

 

#Declared Functions
def header():
    'Welcome message for user.'
    print('Hi there, I am here to help find the distance between two locations.')
    print('I will need the latitude and longitude of each location.')
    print("Let's go!")

 

def get_location():
    'Returns radian float Latitude and Longitude as dictionary keys.'
    lat = radians(float(input("Please enter the latitude: ".strip())))
    lng = radians(float(input("Please enter the longitude: ".strip())))
    point = {"latitude":lat,"longitude":lng}
    return point
def distance_between_points(point1,point2):
    'Input:dictionary with latitude, longitude keys, radian values and uses the haversine formula'
    R = 6371
    lat1 = point1["latitude"]
    lon1 = point1["longitude"]
    lat2 = point2["latitude"]
    lon2 = point2["longitude"]

 

    dlon = lon2 - lon1
    dlat = lat2 - lat1

 

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

 

    distance = R * c
    return distance

 

#Program
while True:
    header()
    print('Get latitude and logitude for location 1')
    point1 = get_location()
    print('Get latitude and logitude for location 2')   
    point2 = get_location()
    print ("The distance in miles is:",round(distance_between_points(point1,point2)*0.6214,2))   
    again = input("\nDo you want to calcluate another distance? Enter 'y' or 'n':").lower().strip()
    if again == 'n':
        print ("\nThanks for using Distance Calculator!! :)")
        break
