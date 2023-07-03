# Kitty - Your Personal Chatbot Assistant

Kitty is a personal chatbot assistant that can help you with various tasks. It is powered by OpenAI's GPT-3 language model and can provide new and interesting replies to your queries. Kitty is also a great programmer and enjoys teaching. She'll even speak to you using Google's gTTS.

## Features:
- Advanced Speech Recognition: Kitty can listen to your voice commands and convert them into text using the SpeechRecognition library.
- Custom Google Search: You can use the !search command to perform a custom Google search and get search results right within the chatbot.
- NMap Scanning: With the !nmap command, Kitty can perform an NMap scan to discover open ports and services on a target host.
- Audio Wave Animation: Kitty provides an interactive audio wave animation that visualizes the sound while playing back the generated speech using the sounddevice library.
- Programming Assistance: Kitty can teach you programming and provide coding examples to help you learn and improve your programming skills.

### How to Use:
1. Clone the repository to your local machine.
2. Install the required dependencies using the provided pip command.

### Customization:
1. Open the terminal-assistant.py file in your preferred text editor.
2. Make any modifications you desire.

### Google Search:
To enable the custom Google search feature, you need to obtain a Google API key and a custom search engine ID. Follow these steps to set it up:
1. Sign up for a Google API key at the [Google Developers Console](https://console.developers.google.com/).
2. Create a new project and enable the "Custom Search JSON API" for the project.
3. Generate an API key for the project.
4. In the terminal-assistant.py file, locate the section for custom search (look for the commented lines starting with "#").
5. Add your `GOOGLE_API_KEY` when prompted by the script.
6. Add your `SEARCH_ENGINE_ID` when prompted by the script..

#### Kitty's Name and Character:
You can customize Kitty's name and character by modifying the respective section in the `terminal-assistant.py` file.

#### Language Model:
By default, Kitty uses the GPT-3 language model. If you want to change the language model, you can do so by editing the `ask_gpt()` function in the `terminal-assistant.py` file.

#### Usage:
Run the `terminal-assistant.py` file using the python command.
Type your query or speak and press Enter to get a response from Kitty.
To exit the chatbot, type `quit`.

##### Disclaimer:
Kitty is a personal chatbot assistant and is not intended to replace human interaction or professional advice. Use it at your own risk.
