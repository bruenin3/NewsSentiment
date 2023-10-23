import praw
import re
import string
import requests
import os
import configparser
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize NLTK and download necessary resources
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')

# Load the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Initialize PRAW with your API credentials
#Replace with your credentials. 
reddit = praw.Reddit(
    client_id='ClientID',
    client_secret='client_secret',
    user_agent='user_agent',
)

# Access the r/news subreddit
subreddit = reddit.subreddit('news')

# Retrieve the top 10 news titles
top_titles = subreddit.top(limit=1000)  # Adjust the limit as needed

# Initialize the NLTK stop words
stop_words = set(stopwords.words('english'))

# Function for text preprocessing
def preprocess_text(text):
    # Remove HTML tags and URLs
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+', '', text)
    
    # Remove special characters and punctuation
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize text
    words = word_tokenize(text)
    
    # Remove stop words
    words = [word for word in words if word not in stop_words]
    
    return ' '.join(words)

# Create a text file to save the titles and sentiment labels
with open('news_titles_with_sentiment.txt', 'w', encoding='utf-8') as file:
    for post in top_titles:
        title = post.title
        cleaned_title = preprocess_text(title)
        sentiment = analyzer.polarity_scores(cleaned_title)
        
        # Determine sentiment label based on the compound score
        if sentiment['compound'] >= 0.05:
            sentiment_label = "Positive"
        elif sentiment['compound'] <= -0.05:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"
        
        # Write the title, sentiment, and upvotes to the text file
        file.write(f"Title: {title}\n")
        file.write(f"Cleaned Title: {cleaned_title}\n")
        file.write(f"Sentiment Label: {sentiment_label}\n")
        file.write(f"Compound Score: {sentiment['compound']}\n")
        file.write("------------\n")

print("Data saved to 'news_titles_with_sentiment.txt'")
