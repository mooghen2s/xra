import subprocess
import time
import keyboard
import mss
import json
import random
import shutil
import argparse
import os

def nonton_youtube(profile_dir):
    try:
        json_file = f'videos.json'
        with open(json_file, 'r') as file:
            videos = json.load(file)
            random_video = random.choice(videos)
            url = random_video['url']
            if profile_dir == 'Profile1':
                window_pos = "0000,1000"
            if profile_dir == 'Profile2':
                window_pos = "0000,1500"
            if profile_dir == 'Profile3':
                window_pos = "0000,2000"
            if profile_dir == 'Profile4':
                window_pos = "0000,000"
            print(url)            
        current_directory = os.getcwd()
        start_time_yt = random.randrange(1, 400)
        end_time_yt = random.randrange(1, 200)
        Url_browser = f'https://youtu.be/{url}&t={start_time_yt}'
        window_size = '300,300'
        command = [
            "C:/Program Files/Google/Chrome/Application/chrome.exe",
            f"--user-data-dir={current_directory}/profiles/{profile_dir}",
            f"--profile-directory={profile_dir}",
            f"--app={Url_browser}",
            f"--autoplay-policy=no-user-gesture-required",
            #f"--window-position={window_pos}"
        ]
        chrome_process = subprocess.Popen(command)
    except Exception as e:
        print(f'Error on opening URL and profile: {e}')
        exit(1)

    # Tunggu selama 30 detik
    time.sleep(5)
    keyboard.press_and_release('f11')
    time.sleep(5)

    #keyboard.press_and_release('k') 
    # Tangkap layar dan simpan sebagai PNG
    #time.sleep(150)
    print(profile_dir)
    with mss.mss() as sct:
        screenshot = sct.shot(output='screenshot.png')
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Nonton YouTube dengan profil tertentu.')
    parser.add_argument('profile_number', type=int, help='Nomor profil yang akan digunakan')
    args = parser.parse_args()
    profile_dir = f'Profile{args.profile_number}'
    nonton_youtube(profile_dir)
