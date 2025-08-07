## This project is a custom WhatsApp chatbot that reads incoming messages from a personal chat window and responds intelligently using Google’s Gemini API. The bot works through screen automation using pyautogui and pyperclip


## DEMO VIDEO
https://drive.google.com/file/d/1gmTKY2uVdtER0Agq8_lpwosGbWPxhzdK/view?usp=drive_link
 
##  Features
 
   Detects the latest incoming message in the chat
   Sends message content to Gemini API for a smart response
   Types and sends the reply automatically
   Runs in a continuous loop and skips replying to self-messages
   Uses clipboard to extract message text safely


##  Tech Stack
 Python
 pyautogui – For automating screen actions
 pyperclip – For clipboard control
 Gemini API – For AI-based text generation
 time – For handling loop timing and delays

##  How It Works
The bot uses pyautogui to select and copy the most recent message in the WhatsApp window.
It checks whether the message is from the other person (not from you).
The message is sent to Gemini using client.py.
The response is received and typed back into WhatsApp via keyboard simulation.
The process repeats in a loop until manually stopped.

NOTE:-Make sure WhatsApp Web/Desktop is open and the target chat is selected.

