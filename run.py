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
    top_highlights = topheadlines['articles']

    '''
    A list of the items to display on our application
    '''
    title = []
    author = []
    descriptions = []
    image = []
    publication_date = []
    news_url = []
    content= []


    '''
    Code block using a for-loop to fetch the contents of articles.
    '''
    for i in range(len(top_highlights)): 
        main_highlight = top_highlights[i]

        title.append(main_highlight['title'])  #To append the title into the list.
        author.append(main_highlight['author'])
        descriptions.append(main_highlight['description'])  #To append the description into the list.
        image.append(main_highlight['urlToImage'])  #Append the urlToImage into the list.
        publication_date.append(main_highlight['publishedAt'])  #Append the published date into the list.
        news_url.append(main_highlight['url'])  #Append the url into the list.
        content.append(main_highlight['content'])


#To store the contents gotten above.
        headlines = zip(title, author, descriptions,image,publication_date,news_url, content)
    return render_template('home.html', headlines = headlines)

if __name__ == '__main__':
    app.run(debug=True)