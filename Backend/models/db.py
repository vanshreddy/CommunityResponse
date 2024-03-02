from datetime import datetime
from typing import Dict

class YouTubeVideo:
    def __init__(self, videoID: str, title: str, uploadedOn: datetime, channelID: str):
        self.videoID = videoID
        self.title = title
        self.uploadedOn = uploadedOn
        self.channelID = channelID

class Comment:
    def __init__(self, commentID: str, videoID: str, userID: str, content: str, commentedOn: datetime):
        self.commentID = commentID
        self.videoID = videoID
        self.userID = userID
        self.content = content
        self.commentedOn = commentedOn

class User:
    def __init__(self, userID: str, username: str, profileURL: str):
        self.userID = userID
        self.username = username
        self.profileURL = profileURL

class SentimentAnalysis:
    def __init__(self, analysisID: str, commentID: str, sentiment: str, positivityScore: float, negativityScore: float, neutralityScore: float):
        self.analysisID = analysisID
        self.commentID = commentID
        self.sentiment = sentiment
        self.positivityScore = positivityScore
        self.negativityScore = negativityScore
        self.neutralityScore = neutralityScore
