from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  

@app.route("/emotionDetector")
def RunSentimentAnalysis():    
    textToAnalyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(textToAnalyze)
    dominant_emotion_key = max(emotions,key=emotions.get)
    

    return f"For the given statement, the system response is 'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} and 'sadness: {emotions['sadness']}'. The dominant emotion is {dominant_emotion_key}."

if __name__ == "__main__":
    app.run(debug=True)