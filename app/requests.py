 from app import app
 import urllib.request,json
 from .models import Source,Article
 
#  Getting api key
 api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_source(category):
  '''
  Function that gets the json response to our url request
  '''
  get_source_url = base_url.format(category,api_key)

  with urrlib.request.urlopen(get_source) as url:
    get_source_data = url.read()
    get_source_response = json.loads(get_source_data)

    source_results = None

    if get_source_response['results']:
      source_results_list = get_source_response['results']
      source_results = process_results(source_results_list) 

  return source_results
    
