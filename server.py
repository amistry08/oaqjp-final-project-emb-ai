from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    return render_template('index.hmtl')

@app.route('/emotionDetector')
def send_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    return f'For the given statement, the system response is anger: {response['anger']} disgust:{response['disgust']}, fear: {response['fear']}, joy:{response['joy']}and sadness: {response['sadness']}. The dominant emotion is {response['dominant_emotion']}.'

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)