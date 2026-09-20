import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

        result = emotion_detector("I am so scared of that man")
        self.assertEqual(result['dominant_emotion'], 'fear')

        result = emotion_detector("I am so sad about the news")
        self.assertEqual(result['dominant_emotion'], 'sadness')


if __name__ == '__main__':
    unittest.main()
