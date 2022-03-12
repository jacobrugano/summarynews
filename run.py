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


        '''
        To store the contents gotten above.
        '''
        headlines = zip(title,author,descriptions,image,publication_date,news_url,content)
    return render_template('home.html', headlines = headlines)


'''
Creating a route function @approute and rendering the html template.
'''
@app.route("/cnn")
def cnn():

    newsapi = NewsApiClient(api_key="44216e90102b4e7bbc548343f8cdc3ea")

    ''' 
    Code-block for getting the top stories from the API
    '''
    all_articles = newsapi.get_everything(sources = 'cnn') #source to help us from where to get the news by API.

    ''' 
    code-block to fetch headlines
    '''
    c_articles = all_articles['articles']
    
    '''
    We make a list of the items to display on our application
    '''

    cnn_title = []
    # cnn_author = []
    cnn_descriptions = []
    cnn_image = []
    cnn_publication_date = []
    cnn_news_url = []
    # cnn_content= []

    '''
    Code block using a for-loop to fetch the contents of articles.
    '''
    for i in range(len(c_articles)): 
        cmain_article = c_articles[i]

        cnn_title.append(cmain_article['title'])  #To append the title into the list.
        cnn_descriptions.append(cmain_article['description'])  #To append the description into the list.
        cnn_image.append(cmain_article['urlToImage'])  #Append the urlToImage into the list.
        cnn_publication_date.append(cmain_article['publishedAt'])  #Append the published date into the list.
        cnn_news_url.append(cmain_article['url'])  #Append the url into the list.
        # cnn_author.append(cmain_article['author']) 
        # cnn_content.append(cmain_article['content']) 

        '''
        To store the contents gotten above.
        '''
        ccontents = zip(cnn_title,cnn_descriptions,cnn_image,cnn_publication_date,cnn_news_url)
        return render_template('cnn.html', ccontents=ccontents)



if __name__ == '__main__':
    app.run(debug=True)

