'''
Server.py
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    '''
    index route
    '''
    return render_template('index.html')

@app.route('/emotionDetector')
def send_detection():
    '''
    emotionDetector route
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid text! Please try again!."

    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Invalid text! Please try again!."

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is "
        f"anger: {anger_score}, disgust: {disgust_score}, fear: {fear_score}, "
        f"joy: {joy_score}, sadness: {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
