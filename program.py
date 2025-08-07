import pyautogui
import time
import pyperclip
from client import get_gemini_reply, extract_last_sender



MY_NAME = "Hamza"


#  Clean sender detection 
def get_last_sender(chat_log: str) -> str:
    last_message = chat_log.strip().split("/2025] ")[-1]
    if ":" in last_message:
        sender = last_message.split(":")[0].strip()
        return sender
    return ""


#  Step 1: Focus WhatsApp Window which is open inside chrome window 
pyautogui.click(1036, 754)
time.sleep(2)

while True:
    time.sleep(10)  # interval between checks

    #  Step 2: Select and copy the chat
    pyautogui.moveTo(491, 153)
    pyautogui.dragTo(1324, 643, duration=2.0, button='left')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(3)
    pyautogui.click(491, 153)

    #  Step 3: Read copied chat
    chat_history = pyperclip.paste()
    print("Copied Chat:\n", chat_history)

    #  Step 4: Check if last message is from target sender
    chat_history = pyperclip.paste()
    last_sender = extract_last_sender(chat_history)

    if "Hamza" in last_sender:
     continue  # Don't reply to yourself

    reply = get_gemini_reply(chat_history, last_sender)

    #  Step 6: Paste and send the reply
    pyperclip.copy(reply)
    pyautogui.click(1081, 684)  # Message box
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')

