from textblob import TextBlob

def detect_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "happy"
    elif polarity < -0.2:
        return "sad"
    else:
        return "calm"
