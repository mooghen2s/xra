import os
import shutil
import youtube_dl
import json

def download_playlist(url):
    ydl_opts = {
        'quiet': False,  # Ubah menjadi True jika Anda ingin mengurangi keluaran log
        'flat-playlist': True,
        'dump_single_json': True,
        'extract_flat': True,
        'list-format' : True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=False)
        if 'entries' in result:
            entries = result['entries']
            videos = [{'number': idx + 1, 'url': entry['url']} for idx, entry in enumerate(entries)]
            with open('videos.json', 'w') as f:
                json.dump(videos, f, ensure_ascii=False, indent=4)
            print("Daftar putar berhasil disimpan dalam format JSON dengan nomor untuk setiap video.")
        else:
            print("Tidak ada video yang ditemukan dalam daftar putar.")
def set_max_output():
    last_profile_dir = 50
    input_file = 'videos.json'
    if not os.path.exists(input_file) or os.path.getsize(input_file) == 0:
        print("File zhistory.json tidak ada atau kosong.")
        return
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
     except json.JSONDecodeError:
        print(f"Gagal membaca file {input_file}, pastikan file tersebut berformat JSON yang benar.")
        return
    last_profile_index = -1
    for i in range(len(data)-1, -1, -1):
        if data[i].get('number') == last_profile_dir:
            last_profile_index = i
            break
    if last_profile_index != -1 and last_profile_index != len(data) - 1:
        data = data[:last_profile_index + 1]
    try:
        with open(input_file, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        print(f"Gagal menulis ke file {input_file}")
if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/@mooghenofficial/videos"
    download_playlist(playlist_url)
    set_max_output()
