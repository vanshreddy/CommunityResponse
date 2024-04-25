import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report


# Sample data 
comments = [
    "Check this amazing deal at www.example.com!!!",
    "Subscribe now!!! Subscribe now!!!",
    "Contact us at info@example.com for more details.",
    "Buy now with 50% discount, only today!",
    "FREE FREE FREE FREE",
    "This video is very informative, thanks for sharing!",
    "Great explanation, cleared up a lot of confusion!",
    "This is just an advertisement. Not helpful."
]
labels = [1, 1, 1, 1, 1, 0, 0, 1]  # 1 for spam, 0 for not spam

# Preprocessing and vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(comments, labels, test_size=0.25, random_state=42)

# Create a pipeline with TF-IDF and a Naive Bayes classifier
model = make_pipeline(TfidfVectorizer(stop_words='english'), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))

# Using the model to detect spam
def detect_spam(comment):
    pred = model.predict([comment])
    return 'Spam' if pred[0] == 1 else 'Not spam'

example_comment = "Huge discount on our new product at this link!!!"
print(detect_spam(example_comment))
