from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


# Function to perform topic modeling
def topic_modeling(comments, num_topics=5, num_words=5):
    vec = CountVectorizer(stop_words='english')
    data = vec.fit_transform(comments)
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=0)
    lda.fit(data)
    
    # Print topics and the words associated with each topic
    features = vec.get_feature_names_out()
    for topic_idx, topic in enumerate(lda.components_):
        print("Topic %d:" % (topic_idx + 1))
        print(" ".join([features[i] for i in topic.argsort()[:-num_words - 1:-1]]))


# Function to cluster comments
def cluster_comments(comments, num_clusters=5):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(comments)
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    kmeans.fit(X)
    labels = kmeans.labels_
    
    clustered_comments = {i: [] for i in range(num_clusters)}
    for label, comment in zip(labels, comments):
        clustered_comments[label].append(comment)
    
    return clustered_comments

