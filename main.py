import subprocess
import time
import pyautogui
import json
import random

try:
    json_file = f'videos.json'
    with open(json_file, 'r') as file:
        videos = json.load(file)
        random_video = random.choice(videos)
        url = random_video['url']
        print(url)
    Url_browser = f'https://www.youtube.com/watch?v={url}'
    profile_dir = 'Profile2'
    window_size = '300,300'
    command = [
        "C:/Program Files/Google/Chrome/Application/chrome.exe",
        f"--user-data-dir=C:/ai/browser/profiles/{profile_dir}",
        f"--profile-directory={profile_dir}",
        f"--app={Url_browser}",
    ]
    chrome_process = subprocess.Popen(command)
except Exception as e:
    print(f'Error on opening URL and profile: {e}')
    exit(1)

# Tunggu selama 30 detik
time.sleep(50)
pyautogui.press('f11') 
pyautogui.press('space') 
# Tangkap layar dan simpan sebagai PNG
time.sleep(5)
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

print("Screenshot saved as screenshot.png")
