import pyautogui
import time

# Give you time to open the chat manually
print("You have 10 seconds to open chat on WhatsApp Web...")
time.sleep(10)

# Message to send
message = "whatsapp msg"

# Send message 100 times
for i in range(50):
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    time.sleep(0.5)  # slight delay between messages

print("All 100 messages sent!")
