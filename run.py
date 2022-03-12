from flask import Flask, render_template
from newsapi import NewsApiClient #Import the API and import it here.
app = Flask(__name__)


#Create a route function and render the html file.
@app.route("/")
def index():

    '''
    A root page function that returns info on the index file.
    '''
    newsapi = NewsApiClient(api_key="44216e90102b4e7bbc548343f8cdc3ea")
    
    #Code-block for getting the top stories from the API
    '''
    Code to get the summary of top headlines
    '''
    topheadlines = newsapi.get_top_headlines(sources = "bbc-news") #source to help us from where to get the news by API.
    top_articles = topheadlines['articles']

    '''
    A list of the items to display on our application
    '''
    news = []
    descriptions = []
    image = []
    publication_date = []
    news_url = []



    
if __name__ == '__main__':
    app.run(debug=True)