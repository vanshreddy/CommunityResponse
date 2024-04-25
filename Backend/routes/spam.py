import re
from collections import Counter

# Function to detect spam comments based on various indicators
def detect_spam(comments, user_data=None):
    spam_keywords = ['http', 'www', 'click', 'subscribe', 'free', '!!!', 'buy', 'discount', 'promotion']
    contact_info_patterns = [r'\bcontact us\b', r'\bemail\b', r'\bphone\b', r'\@\w+', r'\d{7,}']
    spam_comments = {'promotional': [], 'malicious': [], 'irrelevant': [], 'repetitive': []}

    for comment in comments:
        # Lowercase comment for case-insensitive matching
        comment_lower = comment.lower()

        # Check for common spam keywords (promotional or malicious)
        if any(keyword in comment_lower for keyword in spam_keywords):
            spam_comments['promotional' if 'buy' in comment_lower or 'discount' in comment_lower else 'malicious'].append(comment)

        # Check for excessive links or contact information (malicious or promotional)
        if any(re.search(pattern, comment_lower) for pattern in contact_info_patterns):
            spam_comments['malicious'].append(comment)

        # Check for repetition of words (irrelevant or automated)
        word_list = re.findall(r'\w+', comment_lower)
        word_counts = Counter(word_list)
        most_common_words = word_counts.most_common(1)
        if most_common_words[0][1] > 3:  # more than 3 repetitions of the same word
            spam_comments['repetitive'].append(comment)

        if user_data:
            user_comments = user_data.get(comment_lower, [])
            if len(user_comments) > 3:  # more than 3 comments in a short period
                spam_comments['repetitive'].append(comment)

    return spam_comments

comments = [
    "Check this amazing deal at www.example.com!!!",
    "Subscribe now!!! Subscribe now!!!",
    "Contact us at info@example.com for more details.",
    "Buy now with 50% discount, only today!",
    "FREE FREE FREE FREE"
]
spam_detected = detect_spam(comments)
print(spam_detected)
