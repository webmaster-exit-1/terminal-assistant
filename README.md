# Your Personal Terminal Assistant

[![Pylint](https://github.com/webmaster-exit-1/terminal-assistant/actions/workflows/pylint.yml/badge.svg)](https://github.com/webmaster-exit-1/terminal-assistant/actions/workflows/pylint.yml)

## Dev Note: I'm just one guy, making code. If you follow or fork this, don't rely on my updated versions to work. Or even be the same code. So, if I were you and you see something I did and like it, grab it and run with it because I'm not a professional. This is just for fun. And I can and will make breaking changes, stupid ideas, and sometimes, just delete repo's and code I'm done with. Learn 2 Code. Have fun. Happy Hacking

> I created this version to remain productive and helpfull
> It's not a jailbroken version so NO naughty stuff

## Features

* Google Search </br>
* Google Voice Recognition </br>
* Google TTS (Speech playback -- Assistants Voice) </br>
* OpenAI GPT-4

## How to Use

1. Clone the repository to your local machine. </br>
2. Install the required dependencies:

```bash
git clone https://github.com/webmaster-exit-1/terminal-assistant
cd terminal-assistant
pip install -r requirements.txt
```

### Customization

1. Open the terminal-assistant.py file in your preferred text editor. </br>
2. Make any modifications you desire.

### Google Search

To enable the custom Google search feature, you need to obtain a Google API key and a custom search engine ID. Follow these steps to set it up: </br>

1. Sign up for a Google API key at the [Google Developers Console](https://console.developers.google.com/). </br>
2. Create a new project and enable the "Custom Search JSON API" for the project. </br>
3. Generate an API key for the project. </br>
4. Get your Google Search Engine ID here: [Programmable Search Engine](https://programmablesearchengine.google.com/controlpanel/all) </br>
5. Add your `GOOGLE_API_KEY` when prompted by the script. </br>
6. Add your `SEARCH_ENGINE_ID` when prompted by the script..

#### Language Model

By default, it uses the GPT-4 language model. If you want to change the language model, you can do so by editing the `ask_gpt()` function in the `terminal-assistant.py` file.

#### Usage

Run the `terminal-assistant.py` file using the python command. </br>
`"Enter"` To respond with text </br>
`"Shift+Enter"` To respond by voice </br>
Type `!search` to use Google search,example: `!search cats` </br>
To exit the chatbot, type `quit`.

##### Disclaimer

Terminal Assistant is a personal A.I. assistant and is not intended to replace human interaction or professional advice. Use it at your own risk.
