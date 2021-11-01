
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'Zqs_4othi2YG17YZ05NWe7g5PjG6pl5jXdrJKCk3g4HL'
url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/9fd2dab7-9bc0-4e34-a68e-a5b519e73e84'


#Setup services
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

#Perform conversion
with open('sentences1.wav', 'rb') as f:
    res = stt.recognize(audio = f, content_type='audio/mp3', model = 'en-US_NarrowbandModel', continuous=True).get_result()

res

text = res['results'][0]['alternatives'][0]['transcript']
text

confidence = res['results'][0]['alternatives'][0]['confidence']
confidence

with open('output.txt', 'w') as out:
    out.writelines(text)
    
