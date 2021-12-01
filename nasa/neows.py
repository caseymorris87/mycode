#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = input('Enter the start date: ')
    enddate = input('Enter the end date: ')

    startdate = "start_date=" + startdate
    enddate = "end_date=" + enddate


    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + enddate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()
    
    print(f"Object Count: {neodata['element_count']}")
   
    count = 0
    sizes = []
    speeds = []
    distances = []


    for date in neodata['near_earth_objects']:
        for obj in neodata['near_earth_objects'][date]:
            if obj['is_potentially_hazardous_asteroid']:
                count = count + 1
            # sizes.append(obj['estimated_diameter']['kilometers']['estimated_diameter_max'])
            # speeds.append(obj['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
            # distances.append(obj['close_approach_data']['miss_distance']['kilometers'])


    print(f"{count} objects can kill us")

    

    ## display NASAs NEOW data
    #print(neodata)

if __name__ == "__main__":
    main()

