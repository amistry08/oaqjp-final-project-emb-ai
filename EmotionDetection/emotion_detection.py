import requests
import json


def emotion_detector(text_to_analyse):
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    user_input = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=user_input, headers=headers)

    formatted_response = json.loads(response.text)
    response_obj = {}

    if response.status_code == 200:
        if 'emotionPredictions' in formatted_response and len(formatted_response['emotionPredictions']) > 0:
            emotions = formatted_response['emotionPredictions'][0]['emotion']

            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)
            max_score = 0
            dominant_emotion = None

            for score in emotions:
                max_score = max(emotions[score], max_score)
                if(max_score == emotions[score]):
                    dominant_emotion = score

            response_obj = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        else:
            response_obj = {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
            }
        return response_obj
        

    elif response.status_code == 500:
        
        response_obj = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return response_obj

    