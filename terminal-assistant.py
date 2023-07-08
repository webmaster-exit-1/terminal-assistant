import openai
import requests
import sounddevice as sd
import numpy as np
from gtts import gTTS
import os
import subprocess
from nmap3 import Nmap
from configparser import ConfigParser
import json
import speech_recognition as sr
import pyaudio

config = ConfigParser()
CONFIG_NAME = 'testbot_auth.ini'

# Config

def create_config():
    openai_key = input("OpenAI API key: ")
    googleapi_api_key = input("GoogleAPI key: ")
    googleapi_search_engine_id = input("GoogleAPI search engine ID: ")

    config['AUTH'] = {}
    config['AUTH'] = {
        'openai': openai_key,
        'googleapi_key': googleapi_api_key,
        'googleapi_search_id': googleapi_search_engine_id
    }

    with open(CONFIG_NAME, 'w') as f:
        config.write(f)

def check_for_config():
    if os.path.exists(CONFIG_NAME):
        config.read(CONFIG_NAME)
        return

    create_config()

check_for_config()

openai.api_key = config['AUTH']['openai']
API_KEY = config['AUTH']['googleapi_key']
SEARCH_ENGINE_ID = config['AUTH']['googleapi_search_id']
ENDPOINT = "https://www.googleapis.com/customsearch/v1"

# Initialize the recognizer
r = sr.Recognizer()

# Function to perform speech recognition
def recognize_speech(audio_data=None):
    # Create an instance of PyAudio
    audio = pyaudio.PyAudio()

    if audio_data is None:
        # Open a stream for recording
        with sr.Microphone() as source:
            print("Listening...")
            audio_data = r.record(source, duration=5)  # Record audio for 5 seconds

    # Perform speech recognition
    try:
        text = r.recognize_google(audio_data)
        print("Recognized text:", text)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service:", str(e))

# Define the function for interacting with the GPT model
def ask_gpt(prompt, model="gpt-3.5-turbo", tokens=2500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are playing the role of Kitty, the Talkative Catgirl."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=tokens,
        n=1,
        stop=None,
        temperature=0.8,
    )
    return response.choices[0].message['content']

# Function to perform Google Custom Search
def perform_custom_search(search_query):
    params = {
        "key": API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": search_query
    }
    response = requests.get(ENDPOINT, params=params)
    results = response.json().get("items", [])
    return results

# Function to generate speech from text using gTTS
def generate_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("./output.mp3")

    # Load the audio data from the generated file
    audio_data, _ = sd.read("./output.mp3", dtype=np.float32)

    # Create an audio stream for playback
    with sd.OutputStream(callback=audio_callback):
        pass

# Function to perform Nmap scan
def perform_nmap_scan(target):
    nmap = Nmap()

    # Perform an Nmap scan
    results = nmap.scan_top_ports(target)

    # Get the scan results
    scan_results = results[target]

    return scan_results

# Chatbot loop
def chatbot():
    print("Hi user! (Type 'quit' to exit)")

    role = "Kitty, the Talkative Catgirl"  # Set the initial role to the character name
    user_input = "" # Initialize the variable

    # Define the personality and introductory message for Kitty
    personality = {
        "name": "Kitty, the Talkative Catgirl",
        "intro_message": "\"Hewwo there~! I'm Kitty, and I just wuv making new fwiends! You seem like you could use a wittle company, so why not let me keep you company? I'm suuuuper talkative and I wuv helping out~! UwU\""
    }

    print(personality["name"] + ": " + personality["intro_message"])

    while True:
        user_input = recognize_speech() if not user_input.strip() else user_input
        prompt = f"user: {user_input}"
        response = f" {ask_gpt(prompt)}"

        # Check if the user input is a search query
        if user_input.startswith("!search"):
            search_query = user_input[len("!search"):].strip()
            results = perform_custom_search(search_query)

            # Display search results
            if results:
                print("Search Results:")
                for result in results:
                    print(f"Title: {result['title']}")
                    print(f"URL: {result['link']}")
                    print(f"Description: {result['snippet']}")
                    print()
            else:
                print("No results found.")

        # Check if the user input is an Nmap command
        elif user_input.startswith("!nmap"):
            target = user_input[len("!nmap"):].strip()
            results = perform_nmap_scan(target)

            # Display Nmap scan results
            if results:
                print("Nmap Scan Results:")
                for host, ports in results.items():
                    print(f"Host: {host}")
                    for port, data in ports.items():
                        print(f"Port: {port}")
                        print(f"Service: {data['service']}")
                        print()
            else:
                print("No results found.")

        else:
            # Generate speech from the chatbot's response
            generate_speech(response)

            print(f"{role}: {response}")

        input("Press Enter to respond...")

# Execute the chatbot
if __name__ == "__main__":
    chatbot()
