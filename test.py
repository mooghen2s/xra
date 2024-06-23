import os
import subprocess
import json
import random
import shutil
import time
import mss

# Menjalankan Xvfb di latar belakang
os.system('Xvfb :1 -screen 1 1024x768x24 &')
os.environ['DISPLAY'] = ':1'

# Mendapatkan direktori saat ini
current_directory = os.getcwd()
for i in range(5):
    os.system(f'Xvfb :{i} -screen {i} 1024x768x24 &')
    os.environ['DISPLAY'] = f':{i}'
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.114 Safari/537.36"
    profile_dir = f'Profile{i}'
    json_file = f'videos.json'
    with open(json_file, 'r') as file:
        videos = json.load(file)
        random_video = random.choice(videos)
        url = random_video['url']
        if profile_dir == 'Profile1':
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.61 Safari/537.36"
        if profile_dir == 'Profile2':
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.55 Safari/537.36"
        if profile_dir == 'Profile3':
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.3"
        if profile_dir == 'Profile4':
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.141 Safari/537.36"
        if profile_dir == 'Profile0':
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.76 Safari/537.36"
    # Membuat perintah untuk menjalankan Google Chrome
    start_time_yt = random.randrange(1, 400)
    Url_browser = f'https://youtu.be/{url}&t={start_time_yt}'
    print(f'start Url: {Url_browser}')
    window_size = f'600,400'
    command_start_chrome = [
        'google-chrome',
        '--no-sandbox',
        '--disable-gpu',
        f'--user-data-dir={current_directory}/profiles/{profile_dir}',
        f'--profile-directory={profile_dir}',
        f'--app={Url_browser}',
        '--autoplay-policy=no-user-gesture-required',
        f'--user-agent={user_agent}',
        #f'--window-size={window_size}',
        '--disable-extensions'
    ]
    try:
        #shutil.rmtree(f'profiles/{profile_dir}')
        print(f'del {profile_dir}')
    except Exception as e:
        print(f'Error on delete last profile folder: {e}')
    chrome_process = subprocess.Popen(command_start_chrome)
    time.sleep(10)
    os.system('xdotool key enter')
    #pyautogui.press("enter")
    time.sleep(1)
    #pyautogui.keyUp("enter")
    with mss.mss() as sct:
        screenshot = sct.shot(output='screenshot.png')
time.sleep(10)
with mss.mss() as sct:
    screenshot = sct.shot(output='screenshot.png')
os.system('killall chrome')
os.system('killall Xvfb')
