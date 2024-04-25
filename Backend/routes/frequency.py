from collections import Counter
from nltk.corpus import stopwords
import nltk
import matplotlib.pyplot as plt

nltk.download('stopwords')

# Analyze the frequency of words in the comments excluding common stop words
def word_frequency_analysis(comments):
    stop_words = set(stopwords.words('english'))
    words = []
    
    for comment in comments:
        words.extend([word.lower() for word in comment.split() if word.lower() not in stop_words])
    
    word_counts = Counter(words)
    return word_counts

# Plot the most frequent words to visualize key topics or themes in the comments
def plot_word_frequency(word_counts):
    words, counts = zip(*word_counts.most_common(20))
    plt.figure(figsize=(10, 5))
    plt.bar(words, counts)
    plt.title('Top 20 Most Frequent Words in Comments')
    plt.xticks(rotation=45)
    plt.ylabel('Frequency')
    plt.show()


# Categorize comments into positive, negative, and neutral based on their sentiment
def categorize_comments(comments):
    categories = {'positive': [], 'negative': [], 'neutral': []}
    for comment in comments:
        sentiment = TextBlob(comment).sentiment.polarity
        if sentiment > 0:
            categories['positive'].append(comment)
        elif sentiment < 0:
            categories['negative'].append(comment)
        else:
            categories['neutral'].append(comment)
    return categories
