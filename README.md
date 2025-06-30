

# 🗣️ Voice Assistant using Python

This is a simple **Voice Assistant** built with Python that can respond to your voice commands, answer questions, tell jokes, open websites, play music, and more. It uses **speech recognition** for understanding your voice and **text-to-speech** (TTS) to respond like a real assistant.

---

## ✅ Features

* 🎙️ Voice-activated using the keyword: **"Hey Alexa"**
* 💬 Responds to user commands such as:

  * Asking its name or age
  * Telling the current time
  * Telling neutral jokes
  * Opening websites (YouTube, Flipkart, LinkedIn, ChatGPT)
  * Playing local songs
* ❌ Graceful exit with voice command "exit"
* 🧠 Basic error handling for unrecognized speech or commands

---

## 🧰 Requirements

* Python 3.6+
* Microphone access
* The following Python libraries:

  ```bash
  pip install pyttsx3 SpeechRecognition pyjokes
  ```

> Also install PyAudio for microphone access:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🗂️ Project Structure

```
1. Import Libraries
2. Speech-to-Text Function
3. Text-to-Speech Function
4. Voice Activation with "Hey Alexa"
5. Command Recognition and Response
6. Error and Exit Handling
```

---

## 🚀 How to Run

1. Connect a microphone and ensure it's working
2. Run the script:

   ```bash
   python voice_assistant.py
   ```
3. Say **"Hey Alexa"** to activate the assistant
4. Use the following voice commands:

---

## 🧪 Sample Commands

| Command     | Action                              |
| ----------- | ----------------------------------- |
| "your name" | Replies with its name               |
| "old"       | Replies with its age                |
| "doing"     | Replies how it's doing              |
| "time"      | Speaks current time                 |
| "youtube"   | Opens YouTube in browser            |
| "flip"      | Opens Flipkart                      |
| "link"      | Opens LinkedIn                      |
| "chat"      | Opens ChatGPT                       |
| "joke"      | Tells a neutral joke                |
| "song"      | Plays a local song from your system |
| "exit"      | Says goodbye and ends the program   |

---

## 🎵 Notes

* Update the music path in this line to your local directory:

  ```python
  add = r"C:\Users\shiwa\OneDrive\Desktop\songs"
  ```
* Ensure the music folder contains playable audio files.

---

## 🧠 Error Handling

* If speech is not recognized:
  ➤ Prints `Not Understanding...`
* If unknown command is given:
  ➤ Says `"Sorry, I don't know the command"`

---

## 📄 License

This project is licensed under the MIT License.


