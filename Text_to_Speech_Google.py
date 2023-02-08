import requests
import json

def text_to_speech(text, file_name):
    url = "https://texttospeech.googleapis.com/v1/text:synthesize"
    payload = {
        "input": {
            "text": text
        },
        "voice": {
            "languageCode": "en-US",
            "name": "en-US-Wavenet-D"
        },
        "audioConfig": {
            "audioEncoding": "MP3"
        }
    }
    headers = {
        "Authorization": "Bearer " + "<API_KEY>",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
        print("Text-to-Speech completed successfully.")
    else:
        print("Error while performing Text-to-Speech.")