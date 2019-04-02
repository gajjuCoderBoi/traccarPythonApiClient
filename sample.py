from datetime import datetime
from traccarApi import traccarApi

##############  Enter URL in full format like "http://yoursite.com:PORT/api/    ######################3
url = "http://exampleurl.com:1234/api/"

email = ''  #### Enter Email to Login
password = ''  ### Enter Password to Login

datetimeFormat = '%Y-%m-%d %H:%M:%S'
traccar = traccarApi(url=url, _user=email, _pass=password)

startdate = datetime.strptime('2019-03-31 12:14:05', datetimeFormat)
enddate = datetime.strptime('2019-04-01 12:14:05', datetimeFormat)
deviceid = 1

######################## Get Devices ################################
devices = traccar.getDevices()
for device in devices:
    print(device)

##########################################################################

###################### Get Rout of Device #################################



routes = traccar.getRoutes(startDate=startdate, endDate=enddate, deviceId=deviceid)

for route in routes:
    print(route)

##########################################################################


###################### Get Events of Device #################################

events = traccar.getEvents(startDate=startdate, endDate=enddate, deviceId=deviceid)

for event in events:
    print(event)

##########################################################################


###################### Get Stops of Device #################################



stops = traccar.getStops(startDate=startdate, endDate=enddate, deviceId=deviceid)

for stop in stops:
    print(stop)

##########################################################################


###################### Get Summary of Device #################################



summary = traccar.getSummary(startDate=startdate, endDate=enddate, deviceId=deviceid)

for summary in summary:
    print(summary)

##########################################################################


###################### Get Trips of Device #################################



trips = traccar.getTrips(startDate=startdate, endDate=enddate, deviceId=deviceid)

for trip in trips:
    print(trip)

##########################################################################
