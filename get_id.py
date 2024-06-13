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

if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/@mooghenofficial/videos"
    download_playlist(playlist_url)
