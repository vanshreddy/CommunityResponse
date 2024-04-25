from gender_guesser.detector import Detector

# Function to guess gender from first names
def guess_gender(names):
    d = Detector()
    return [d.get_gender(name.split()[0]) for name in names]

# Function to perform sentiment analysis and correlate with gender
def sentiment_analysis_by_gender(comments, names):
    genders = guess_gender(names)
    sentiments = [TextBlob(comment).sentiment.polarity for comment in comments]
    
    gender_sentiment = zip(genders, sentiments)
    gender_analysis = {}
    for gender, sentiment in gender_sentiment:
        if gender not in gender_analysis:
            gender_analysis[gender] = []
        gender_analysis[gender].append(sentiment)
    
    for gender in gender_analysis:
        average_sentiment = sum(gender_analysis[gender]) / len(gender_analysis[gender])
        print(f"{gender.title()} Average Sentiment: {average_sentiment:.2f}")

