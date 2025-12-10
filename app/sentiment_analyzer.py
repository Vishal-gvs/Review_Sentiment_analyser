"""
Sentiment Analysis Module
"""
import re
from textblob import TextBlob


# Import NLTK for VADER
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon if not present
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon', quiet=True)

def analyze_review_vader(text):
    """
    Analyze sentiment using VADER (Valence Aware Dictionary and sEntiment Reasoner)
    
    Args:
        text (str): Review text
        
    Returns:
        dict: Result containing sentiment label and compound score
    """
    # Ensure text is string
    text = str(text) if text else ""
    
    # Initialize VADER
    sid = SentimentIntensityAnalyzer()
    
    # Get scores
    scores = sid.polarity_scores(text)
    compound = scores['compound']
    
    # Classify based on compound score
    if compound >= 0.05:
        sentiment = 'positive'
    elif compound <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
        
    return {
        'sentiment': sentiment,
        'compound_score': round(compound, 3),
        'pos': scores['pos'],
        'neg': scores['neg'],
        'neu': scores['neu']
    }

def predict_sentiment_ml(reviews):
    """
    Predict sentiment using ML model.
    NOTE: Currently acting as a fallback using VADER logic since trained model is missing.
    
    Args:
        reviews (list): List of review texts
        
    Returns:
        list: List of predicted sentiment labels
    """
    results = []
    sid = SentimentIntensityAnalyzer()
    
    for review in reviews:
        # Simple fallback using VADER logic
        scores = sid.polarity_scores(str(review))
        if scores['compound'] >= 0.05:
            results.append('positive')
        elif scores['compound'] <= -0.05:
            results.append('negative')
        else:
            results.append('neutral')
            
    return results

def prepare_text(text):
    """
    Task 1: Data Collection and Preparation
    Clean and prepare text for sentiment analysis
    
    Args:
        text (str): Raw review text
        
    Returns:
        str: Cleaned and prepared text
    """
    if not isinstance(text, str):
        return str(text)

    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and punctuation, keep only alphanumeric and whitespace
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text

def analyze_sentiment(text):
    """
    Task 2: Sentiment Analysis
    Analyze sentiment of a review using TextBlob
    
    Args:
        text (str): Review text (can be raw or prepared)
        
    Returns:
        dict: Dictionary containing sentiment label and polarity score
    """
    # Prepare the text
    prepared_text = prepare_text(text)
    
    # Create TextBlob object
    blob = TextBlob(prepared_text)
    
    # Get polarity (-1 to 1)
    polarity = blob.sentiment.polarity
    
    # Classify sentiment
    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return {
        'sentiment': sentiment,
        'polarity': round(polarity, 3),
        'subjectivity': round(blob.sentiment.subjectivity, 3)
    }

def analyze_batch(reviews):
    """
    Analyze multiple reviews at once
    
    Args:
        reviews (list): List of review texts
        
    Returns:
        list: List of analysis results
    """
    results = []
    for review in reviews:
        if review and str(review).strip():  # Skip empty reviews
            result = analyze_sentiment(review)
            result['review'] = review
            results.append(result)
    return results

def get_sentiment_distribution(analyses):
    """
    Task 3: Calculate sentiment distribution
    
    Args:
        analyses (list): List of analysis results
        
    Returns:
        dict: Distribution of sentiments
    """
    distribution = {
        'positive': 0,
        'negative': 0,
        'neutral': 0
    }
    
    for analysis in analyses:
        sentiment = analysis.get('sentiment', 'neutral')
        distribution[sentiment] = distribution.get(sentiment, 0) + 1
    
    return distribution




