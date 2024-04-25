from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np

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

# Usage example: topic_modeling(comments)
