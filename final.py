import requests
from datetime import datetime, timedelta


api_key = 'jAzsEGAGRFEgxObDARcs5xNuSstCqEgX'


# Set up the API endpoint and parameters
endpoint = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
query = 'Princeton University'


# Creating and adding date range parameters
start_date = '20220101'  # the full year of 2022
end_date = '20221231'    


params = {
    'api-key': api_key,
    'q': query,
    'begin_date': start_date,
    'end_date': end_date
}


# Make the API request
response = requests.get(endpoint, params=params)


#  if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()


    # Extract the number of articles
    num_articles = data['response']['meta']['hits']


    # Print the result
    print(f"Number of articles about Princeton University in the specified date range: {num_articles}")




    # can we save the articles to a text file or another document format?

