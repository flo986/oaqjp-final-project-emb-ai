import unittest
from EmotionDetection.emotion_detection import emotion_detector

def dominant_emotion(dict_of_emotions):
    dominant_emotion = ""
    dominant_emotion_value = 0
    for emotion in dict_of_emotions:
        if dict_of_emotions[emotion] > dominant_emotion_value:
            dominant_emotion = emotion
            dominant_emotion_value = dict_of_emotions[emotion]

    return dominant_emotion

class TestEmotions(unittest.TestCase):
    def test_emotions(self):
        self.assertEqual(dominant_emotion(emotion_detector("I am glad this happened")),"joy")
        self.assertEqual(dominant_emotion(emotion_detector("I am really mad about this")),"anger")
        self.assertEqual(dominant_emotion(emotion_detector("I feel disgusted just hearing about this")),"disgust")
        self.assertEqual(dominant_emotion(emotion_detector("I am so sad about this")),"sadness")
        self.assertEqual(dominant_emotion(emotion_detector("I am really afraid that this will happen")),"fear")

unittest.main()