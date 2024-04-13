from googleapiclient.discovery import build
from textblob import TextBlob


api_key = "YOUR_API_KEY"
youtube = build('youtube', 'v3', developerKey=api_key)


def get_comments(youtube, **kwargs):
    comments = []
    results = youtube.commentThreads().list(**kwargs).execute()

    while results:
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

        # check if there are more comments
        if 'nextPageToken' in results:
            kwargs['pageToken'] = results['nextPageToken']
            results = youtube.commentThreads().list(**kwargs).execute()
        else:
            break

    return comments


def analyze_comments(comments):
    sentiment_scores = []
    for comment in comments:
        analysis = TextBlob(comment)
        sentiment_scores.append(analysis.sentiment.polarity)
        print(f"Comment: {comment}\nSentiment: {analysis.sentiment}\n")
    return sentiment_scores

def calculate_average_sentiment(sentiment_scores):
    if sentiment_scores:
        return sum(sentiment_scores) / len(sentiment_scores)
    else:
        return None
    

def find_most_positive_comment(comments, sentiment_scores):
    max_score = max(sentiment_scores)
    max_index = sentiment_scores.index(max_score)
    return comments[max_index]