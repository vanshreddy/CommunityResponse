import emoji
from collections import Counter
import matplotlib.pyplot as plt

# Function to extract and count emojis in comments
def extract_emojis(comments):
    emojis_list = [c for comment in comments for c in comment if c in emoji.UNICODE_EMOJI['en']]
    emoji_counts = Counter(emojis_list)
    return emoji_counts

# Function to plot the frequency of top emojis
def plot_emoji_usage(emoji_counts):
    emojis, counts = zip(*emoji_counts.most_common(10))
    plt.figure(figsize=(10, 5))
    plt.bar(emojis, counts)
    plt.title('Top 10 Emojis in Comments')
    plt.xlabel('Emoji')
    plt.ylabel('Frequency')
    plt.show()
