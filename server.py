
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  

@app.route("/emotionDetector")
def RunSentimentAnalysis(input_text):    
    emotions = emotion_detector(input_text)
    dominant_emotion_key = max(emotions,key=emotions.get)
    dominant_emotion = emotions[dominant_emotion_key]

    return f"For the given statement, the system response is {emotions}. The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(debug=True)