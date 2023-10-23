Reddit News Scraper

## Overview

This Python script is designed to scrape top news titles from the Reddit r/news subreddit. It retrieves the top news posts, preprocesses the titles, performs sentiment analysis, and saves the cleaned titles and sentiment labels for further analysis.

## Features

- Scrapes top news titles from Reddit r/news.
- Performs text preprocessing, including removing HTML tags, URLs, special characters, and stop words.
- Utilizes the VADER sentiment analysis tool to determine sentiment scores.
- Categorizes sentiment as "Positive," "Negative," or "Neutral."
- Saves cleaned titles, sentiment labels, and sentiment scores to a text file for analysis.

## Prerequisites

- Python 3.x
- PRAW (Python Reddit API Wrapper)
- NLTK (Natural Language Toolkit)
- wordcloud (if using word cloud generation)

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/RedditNewsScraper.git
