import re
from wordcloud import WordCloud
from stop_words import get_stop_words

STOPWORDS_RU = get_stop_words('russian')

def cloud(text, chat):
    text = re.sub(r'==.*?==+', '', text)
    text = text.replace('\n', '')
    wordcloud = WordCloud(width = 2000, 
                      height = 1500, 
                      random_state=1, 
                      background_color='black', 
                      margin=20, 
                      colormap='Pastel1', 
                      collocations=False, 
                      stopwords = STOPWORDS_RU).generate(text)
    wordcloud.to_file(f'{chat}.png')