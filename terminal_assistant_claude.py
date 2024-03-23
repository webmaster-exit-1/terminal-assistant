"""
This module provides a terminal assistant using Anthropic's API.
You will need a PAID Anthropic API Key.
Made with help by using Anthropic's Claude A.I.
"""
import time
import os
import subprocess
from configparser import ConfigParser
import sys
import speech_recognition as sr
import requests
from pydub import AudioSegment
from pydub.playback import play
from anthropic import Anthropic
from gtts import gTTS

# Redirect stderr to /dev/null
sys.stderr = subprocess.DEVNULL

config = ConfigParser()
CONFIG_NAME = 'ta_auth.ini'

def create_config():
    """
    Function to create a configuration file.
    """
    anthropic_key = input("Anthropic API key: ")
    googleapi_api_key = input("GoogleAPI key: ")
    googleapi_search_engine_id = input("GoogleAPI search engine ID: ")
    config['AUTH'] = {
        'anthropic': anthropic_key,
        'googleapi_key': googleapi_api_key,
        'googleapi_search_id': googleapi_search_engine_id
    }
    with open(CONFIG_NAME, 'w', encoding='utf-8') as config_file:
        config.write(config_file)

def check_for_config():
    """
    Function to check for a configuration file.
    """
    if os.path.exists(CONFIG_NAME):
        config.read(CONFIG_NAME)
        return
    create_config()

check_for_config()

anthropic = Anthropic(api_key=config['AUTH']['anthropic'])

API_KEY = config['AUTH']['googleapi_key']
SEARCH_ENGINE_ID = config['AUTH']['googleapi_search_id']
ENDPOINT = "https://www.googleapis.com/customsearch/v1"

def ask_anthropic(prompt):
    """
    Function to interact with the Anthropic API.
    """
    response = anthropic.completions.create(
        prompt=f"{anthropic.HUMAN_PROMPT} {prompt} {anthropic.AI_PROMPT}",
        max_tokens_to_sample=1024,
        model="claude-v1",
    )
    return response.completion.strip()

def generate_speech(text):
    """
    Function to generate speech from text using gTTS.
    """
    gtts = gTTS(text=text, lang="en-au")
    gtts.save("output.mp3")

def recognize_speech():
    """
    Function to recognize speech using Google Speech Recognition.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = recognizer.listen(source, timeout=15, phrase_time_limit=20)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as error:
        print(f"Error: {error}")
        return ""

def perform_google_search(query):
    """
    Function to perform a Google search using the Custom Search JSON API.
    """
    params = {
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': query
    }
    response = requests.get(ENDPOINT, params=params, timeout=5)
    search_results = response.json()
    if 'items' in search_results:
        results = search_results['items']
        for result in results:
            print(result['title'])
            print(result['link'])
            print(result['snippet'])
            print()
    else:
        print("No results found.")

def play_audio():
    """
    Function to play the speech audio.
    """
    sound = AudioSegment.from_mp3("output.mp3")
    play(sound)

def chatbot():
    """
    Main chatbot loop.
    """
    username = input("Enter your username: ")
