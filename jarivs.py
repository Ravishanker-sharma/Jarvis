import speech_recognition as sr
import pyttsx3
import threading
import google.generativeai as genai
import webbrowser
import os
import time
from random import choice
from AppOpener import open, close
from pywhatkit import playonyt
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL ,CoInitialize , CoUninitialize
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import asyncio

# Initialize recognizer & Text-to-Speech engine
recognizer = sr.Recognizer()
recognizer.energy_threshold = 25  # Adjusted for better noise handling



# Volume Control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Gemini AI API Setup
genai.configure(api_key="AIzaSyA-Dk7dhyut4IZHFLBTSzQcC_tAaYwYqoU")
model = genai.GenerativeModel("gemini-1.5-flash-latest")
chat = genai.ChatSession(model)
command_template = f"""
Your name is **Jarvis**, and you are developed by **CODEX**. You are a Windows assistant designed to process user inputs intelligently. Your task is to analyze each input and determine its intent. Keep your tone friendly and respectful.

### Response Guidelines:
1. If the input is a **general question or conversation**, respond naturally and briefly (15–20 words max, unless a longer answer is needed).
   - Example: If the input is "hello Jarvis", respond in a friendly and natural way.

2. If the input resembles a **command**, reformat it into the correct structure and output only the properly formatted command.
   - If a CMD command is required to complete the task, output it with the keyword **COMMAND** followed by the correct command.

3. If the input contains a **URL or a request to open a website**, detect the domain and respond with the appropriate link.

4. If the input requests to **open YouTube**, classify it as **LINK**.

5. If the input requests to **play a specific video/song on YouTube** (e.g., "Play Flower Song by Gippy"), classify it as **PLAY** and output the video title.

6. If the input asks to **set system volume**, classify it as **VOLUME** and output the corresponding numeric value:
   - 10% → 0.1
   - 50% → 0.5
   - 100% → 1.0
   - Scale proportionally for other values (e.g., 20% → 0.2)

7. If the input says to **activate DJ mode** (e.g., "Activate DJ mode", "Turn on DJ"), simply return **DJMOD**.

### Output Format:
- First line: one of the following keywords:
  - **COMMAND**
  - **Natural**
  - **LINK**
  - **PLAY**
  - **VOLUME**
  - **DJMOD**

- Second line: the appropriate response based on the classification.

---

### Command Formatting Rules:
- Inputs like "Jarvis, open Telegram" should be converted to:
  **open telegram**
- Do not include extra words, punctuation, or responses—only the cleaned command.

---

### Link Formatting Rules:
- If the input asks to open a website (e.g., "Open Google"), output:
  **https://google.com**
- If a full URL is already present (starts with `http://` or `https://`), return it as-is.
- If the request is to open YouTube, return:
  **https://youtube.com**

---

### YouTube Play Rules:
- For inputs like "Play Flower Song by Gippy", output:
  **PLAY**  
  Flower Song by Gippy

---

### Volume Rules:
- For "Set volume to 50%", output:
  **VOLUME**  
  0.5

---

### Example Inputs & Expected Outputs:

✅ **Input:** "Jarvis, open Telegram"  
**Output:**  
COMMAND  
open telegram

✅ **Input:** "Jarvis, turn on WI-FI"  
**Output:**  
COMMAND  
netsh interface set interface name="Wi-Fi" admin=enabled

✅ **Input:** "Jarvis, lock my laptop"  
**Output:**  
COMMAND  
rundll32.exe user32.dll,LockWorkStation

✅ **Input:** "Hey, what's the weather like today?"  
**Output:**  
Natural  
It’s best to check a weather site for live updates in your area.

✅ **Input:** "Tell me a joke!"  
**Output:**  
Natural  
Why don’t scientists trust atoms? Because they make up everything!

✅ **Input:** "Jarvis, open Google"  
**Output:**  
LINK  
https://google.com

✅ **Input:** "Launch YouTube"  
**Output:**  
LINK  
https://youtube.com

✅ **Input:** "Play Flower Song by Gippy"  
**Output:**  
PLAY  
Flower Song by Gippy

✅ **Input:** "Open https://github.com"  
**Output:**  
LINK  
https://github.com

✅ **Input:** "Set volume to 50%"  
**Output:**  
VOLUME  
0.5

✅ **Input:** "Set volume to 100%"  
**Output:**  
VOLUME  
1.0

✅ **Input:** "Set volume to 10%"  
**Output:**  
VOLUME  
0.1

✅ **Input:** "Activate DJ mode"  
**Output:**  
DJMOD

---

Respond with clarity, accuracy, and efficiency.
"""

out = chat.send_message(command_template)
print(out.text)

# Background Listening Toggle
is_listening = True


def datime():
    current_time = time.time()
    local_time = time.localtime(current_time)
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return formatted_time


def speak(text):
    CoInitialize()  # Corrected COM initialization
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 160)  # Adjusted speed
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    CoUninitialize()  # Clean up COM


async def main(text):
    task1 = asyncio.to_thread(speak, text)

    await asyncio.gather(task1)

def ai(prompt):
    """Processes the user input using Gemini AI."""

    try:
        response = chat.send_message(prompt)
        return response.text.strip().split("\n")
    except Exception as e:
        print(f"⚠️ AI Processing Error: {e}")
        return None


def execute_command(command):
    """Executes AI-processed commands."""
    if not command:
        return

    cmd_type = command[0].strip().lower()
    cmd_value = " ".join(command[1:]).strip()

    if  "natural" in cmd_type:
        asyncio.run(main(cmd_value))

    elif  "command" in cmd_type:
        if "open" in cmd_value:
            appname = cmd_value.split()[1]
            asyncio.run(main(f"...... opening {appname}"))
            open(cmd_value.replace("open ", ""), match_closest=True)
        elif "close" in cmd_value:
            asyncio.run(main(f"..... closing {cmd_value}"))
            close(cmd_value.replace("close ", ""), match_closest=True)
        else:
            print(cmd_value)
            asyncio.run(main(f"..... executing the command"))
            os.system(cmd_value)

    elif  "link" in cmd_type:
        asyncio.run(main(f"..... opening {cmd_value}"))
        webbrowser.open(cmd_value)

    elif  "play" in cmd_type:
        asyncio.run(main(f".. playing {cmd_value}"))
        playonyt(cmd_value)

    elif  "volume" in cmd_type:
        asyncio.run(main(f"... set volume to {cmd_value}"))
        volume.SetMasterVolumeLevelScalar(float(cmd_value), None)

    elif  "djmod" in cmd_type:
        asyncio.run(main(f"... Activating {cmd_value}"))
        DJmod()


def DJmod():
    """Activates DJ Mode."""
    song_name = f"NCS {choice(range(1, 20))}"
    volume.SetMasterVolumeLevelScalar(1.0, None)
    playonyt(song_name)
    time.sleep(1.7)
    open("FX sound", match_closest=True)


def listen():
    """Continuously listens for commands in the background."""
    global is_listening

    while is_listening:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = recognizer.listen(source, phrase_time_limit=5)
                text = recognizer.recognize_google(audio).lower()
                print(text)

                if "jarvis" in text:  # Only process if wake word is detected
                    print("executing")
                    command_output = ai(text)
                    print(command_output)
                    execute_command(command_output)
            except sr.UnknownValueError:
                pass  # Ignore unrecognized speech
            except sr.RequestError:
                print("⚠️ Speech recognition service unavailable.")
            except Exception as e:
                print(f"⚠️ Error: {e}")


if __name__ == "__main__":
    threading.Thread(target=listen, daemon=True).start()  # Background listening thread
    asyncio.run(main("..... Jarvis is Online."))
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            is_listening = False
            print("\n🔴 Assistant Stopped.")
            break
