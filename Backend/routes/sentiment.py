from flask import request, jsonify
from textblob import TextBlob

def analyze_sentiment():
    data = request.json
    if not data or 'texts' not in data:
        return jsonify({'error': 'No texts provided for analysis'}), 400

    texts = data['texts']
    if not isinstance(texts, list):
        return jsonify({'error': 'Input must be an array of strings'}), 400

    results = []
    for text in texts:
        analysis = TextBlob(text)
        sentiment = analysis.sentiment
        results.append({
            'text': text,
            'polarity': sentiment.polarity,
            'subjectivity': sentiment.subjectivity
        })

    return jsonify(results)


def calculate_average_sentiment(results):
    total_polarity = 0
    total_subjectivity = 0
    for result in results:
        total_polarity += result['polarity']
        total_subjectivity += result['subjectivity']
    average_polarity = total_polarity / len(results)
    average_subjectivity = total_subjectivity / len(results)
    return average_polarity, average_subjectivity


def find_most_positive_text(results):
    most_positive_text = max(results, key=lambda x: x['polarity'])
    return most_positive_text

def find_most_subjective_text(results):
    most_subjective_text = max(results, key=lambda x: x['subjectivity'])
    return most_subjective_text