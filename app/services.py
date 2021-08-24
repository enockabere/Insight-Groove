import urllib.request
import json
from .models import Quotes

quote_url = None

def configure_request(app):
    global quote_url
    quote_url = app.config['QUOTES_API_BASE_URL']
def get_quotes():
    '''
    Function that returns json response to url request
    '''
    get_quotes_url = quote_url
    print(get_quotes_url)
    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
        
        quotes_result =None
        
        author = get_quotes_response.get('author')
        quote = get_quotes_response.get('quote')
        
        
        quotes_object = Quotes(author, quote)
    return quotes_object
   
         