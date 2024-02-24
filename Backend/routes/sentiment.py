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
