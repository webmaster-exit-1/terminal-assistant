# Kitty - Your Personal Chatbot Assistant

### Dev Note: I'm just one guy, making code. If you follow or fork this, don't rely on my updated versions to work. Or even be the same code. So, if I were you and you see something I did and like it, grab it and run with it because I'm not a professional. This is just for fun. And I can and will make breaking changes, stupid ideas, and sometimes, just delete repo's and code I'm done with. Learn 2 Code. Have fun. Happy Hacking.

Kitty is a personal chatbot assistant that can help you with various tasks. It is powered by OpenAI's GPT-3 language model and can provide new and interesting replies to your queries. Kitty is also a great programmer and enjoys teaching. She'll even speak to you using Google's gTTS.

## Features

- Advanced Speech Recognition: Kitty can listen to your voice commands and convert them into text using the SpeechRecognition library.
- Custom Google Search: You can use the `!search` command to perform a custom Google search and get search results right within the chatbot.
- NMap Scanning: With the `!nmap` command, Kitty can perform an NMap scan to discover open ports and services on a target host.
- Audio Playback: Kitty provides audio playback functionality using the sounddevice library to play back generated speech.
- Programming Assistance: Kitty can teach you programming and provide coding examples to help you learn and improve your programming skills.

## How to Use

1. Clone the repository to your local machine.
2. Install the required dependencies:

```bash
git clone https://github.com/webmaster-exit-1/terminal-assistant
cd terminal-assistant
pip install -r requirements.txt
```

### Customization:

1. Open the terminal-assistant.py file in your preferred text editor.
2. Make any modifications you desire.
3. If you do not edit, you may end up with a furry talking catgirl terminal assistant, lol. (for the lols)

### Google Search:

To enable the custom Google search feature, you need to obtain a Google API key and a custom search engine ID. Follow these steps to set it up:
1. Sign up for a Google API key at the [Google Developers Console](https://console.developers.google.com/).
2. Create a new project and enable the "Custom Search JSON API" for the project.
3. Generate an API key for the project.
4. Add your `GOOGLE_API_KEY` when prompted by the script.
5. Add your `SEARCH_ENGINE_ID` when prompted by the script..

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
