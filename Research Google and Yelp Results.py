##What's the challenge:
##	Ensuring the provider database is up to date and accurate
##	
##Can we use the Google search or yelo api, to search an address, and get back information about the location? 
##Do it by step by step, and ask for user input, and see if this is what they are looking for. 
##Keep the search result link, the yelp and the google result, for each line item, to act as a reference 
##
##Take a practice I know exists, use it as a test, have the program rip through the spreadsheet of addresses and return search results. 
##
##Create a flow chart, and reconnect with Justin.
##search google maps for the search result, and see if it is open or closed

#1. iterate through the sheets, combining name and address into a text field that we search for. Return the top 5 search results for this thing. 




##https://python-googlesearch.readthedocs.io/en/latest/
##https://pypi.org/project/google/
##https://cmdlinetips.com/2018/12/how-to-loop-through-pandas-rows-or-how-to-iterate-over-pandas-rows/

#flowchart https://code2flow.com/3sskBv

#what are static types in python? Does adding them speed up the code? also, cython, for adding c performance to your python, eases the heavy lifying for some computationally intensive sections of your code

#google api key: AIzaSyByMfz-rWKZ5qQBgpwIK0bgbaiu-kfrhI4


from googlesearch import search
import os
import pandas as pd
import numpy as np
from openpyxl import load_workbook
from googleplaces import GooglePlaces, types, lang

file_location_of_list_of_practices = r'C:\Users\isaama2\Desktop\Eloqua Data Combiner Files\Investigating Possibly Closed Locations\Possibly Closed Locations List.xlsx' #need to add this practice file
YOUR_API_KEY = 'AIzaSyByMfz-rWKZ5qQBgpwIK0bgbaiu-kfrhI4'
def search_for_web_results(file_location_of_list_of_practices, YOUR_API_KEY):
    practices = pd.read_excel(file_location_of_list_of_practices)
    #print(practices)
    for index, row in practices.iterrows(): #don't use this, use https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas/55557758#55557758  
        practice_name = getattr(row, "Common Account Name")
        practice_address = getattr(row, "Physical Street")
        practice_city = getattr(row, "Physical City")
        
        google_places = GooglePlaces(YOUR_API_KEY)
        query_result = google_places.text_search(query = practice_name + practice_address)
        print(len(query_result.places))
        for place in query_result.places:
            print (place.name)
            print (place.place_id)
            print('\n')

##      google maps api for python: https://developers.google.com/places/web-service/intro, https://developers.google.com/places/web-service/get-api-key, https://console.cloud.google.com/projectselector2/google/maps-apis/overview?pli=1&supportedpurview=project

##      https://stackoverflow.com/questions/50504897/google-places-api-in-python


##        for url in search(practice_name + practice_address, pause = 2.0, stop = 1):
##            print(url)    
##        row = 1
##        practice_name = practices.iloc[row,4]
##        practice_address = practices.iloc[row,5]
##        row + 1
##            print(practice_name)
##            print(practice_address)


search_for_web_results(file_location_of_list_of_practices, YOUR_API_KEY)
