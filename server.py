"""FUCK YOU"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """FUCK YOU"""
    return render_template("index.html")

@app.route("/emotionDetector")
def run_sentiment_analysis():
    """FUCK YOU"""
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyze)

    if emotions["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
    f"For the given statement, the system response is 'anger': {emotions['anger']}, "
    f"'disgust': {emotions['disgust']}, "
    f"'fear': {emotions['fear']}, "
    f"'joy': {emotions['joy']} and "
    f"'sadness': {emotions['sadness']}. "
    f"The dominant emotion is {emotions['dominant_emotion']}."
)

if __name__ == "__main__":
    app.run(debug=True)
    