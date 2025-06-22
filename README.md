# 🧠 Jarvis: A Voice-Activated Windows Assistant Powered by Gemini AI
Jarvis is an AI-powered voice assistant for Windows. Built with Python and Google’s Gemini 1.5, it can listen, understand, and respond to voice commands — whether you're opening apps, playing music, adjusting volume, or just having a chat.

## ✨ Features
  🎙️ Voice Activation – Responds to “Jarvis” with smart background listening.
  
  🧠 Gemini AI – Processes natural language with Google’s Gemini 1.5 model.
  
  🗣️ Text-to-Speech – Speaks responses using realistic voice.
  
  🖥️ App Control – Open and close Windows apps via voice.
  
  🎵 YouTube Integration – Plays any song/video with pywhatkit
  
  🔊 Volume Control – Adjust system volume with voice (10%–100%).
  
  🌐 Browser Support – Opens any website or direct URL.
  
  🎧 DJ Mode – Boosts volume, plays random NCS track, and opens FX sound booster.
  
  🔍 Intent Classification – Every input is classified into one of:

    COMMAND
    LINK
    PLAY
    VOLUME  
    NATURAL
    DJMOD

## ⚙️ Tech Stack

  Voice Recognition	speech_recognition
  
  TTS (Speak Output)	pyttsx3, comtypes
  
  AI Understanding	google.generativeai
  
  App Launching	AppOpener
  
  YouTube Playback	pywhatkit
  
  Volume Control	pycaw
  
  Browser Control	webbrowser
  
  Async Execution	asyncio, threading

## 🛠️ Installation
### 🧰 Requirements
  Python 3.8+
  
  Windows OS
  
  Google API Key for Gemini

📦 Install Dependencies
```
pip install -r requirements.txt
Example requirements.txt:
speechrecognition
pyttsx3
pycaw
pywhatkit
google-generativeai
AppOpener
comtypes
```
## 🔑 Gemini API Setup
```
Visit Google AI Studio.

Copy your API key.

Replace the following line in jarivs.py:


genai.configure(api_key="YOUR_API_KEY_HERE")
▶️ Running Jarvis
```
```
python jarivs.py
Once running, you’ll see:
```
```
..... Jarvis is Online.
🎤 Listening...
Now speak to your assistant. Try:
```
```
"Jarvis, open Google"
"Play Love Yourself by Justin Bieber"
"Set volume to 50%"
"Activate DJ mode"
"Tell me a joke"
💬 Example Inputs & Outputs
Spoken Input	Output Type	Action
Jarvis, open Telegram	COMMAND	Opens the Telegram app
Set volume to 30%	VOLUME	Sets system volume to 0.3
Play Flower Song by Gippy	PLAY	Plays the song on YouTube
Activate DJ mode	DJMOD	Plays NCS track at full volume
Open https://github.com	LINK	Opens GitHub in the browser
Tell me a joke	NATURAL	Speaks back a fun response using Gemini AI
```

## 📁 Project Structure
```
jarivs.py
README.md
requirements.txt
```
## ⚠️ Limitations
  ✅ Requires Windows (due to COM and pycaw).
  
  ❗ Wake word detection is simple: it only listens when it hears “jarvis”.
  
  ⛔ No graphical interface (yet) — CLI-based experience only.

## 👤 Author
  Developed By Ravishanker Sharma
