from gtts import gTTS
import openai
import os
import speech_recognition as sr

openai.api_key = "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"

def get_voice_input():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Listening...")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
    return text

def text_to_speech(text, language='en', output_file='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    os.system("start " + output_file)

def get_response(input):
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=input
)
    return response['choices'][0]['text']

if __name__ == "__main__":
    print("Chatbot: Hii user!! How may I help you?")
    text_to_speech('Hii user!! How may I help you?')
    while True:
        user_input = get_voice_input()
        if user_input == 'exit':
           break
        response = get_response(user_input)
        print(response)
        text_to_speech(response)
    
########## ASSIGNMENT ########
#Get response from chatbot as voice
