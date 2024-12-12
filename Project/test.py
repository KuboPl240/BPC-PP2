import tkinter as tk
import vlc
from pytubefix import YouTube
from pytubefix.cli import on_progress

# Funkcia na získanie odkazu na video z YouTube
def get_video_url():
    # Zadajte URL YouTube videa
    url = url_entry.get()
    yt = YouTube(url, on_progress_callback = on_progress)
    return yt.streams.get_highest_resolution().url

# Funkcia na prehrávanie videa
def play_video():
    video_url = get_video_url()  # Získanie URL videa
    media = instance.media_new(video_url)  # Vytvorenie média
    player.set_media(media)  # Nastavenie média pre prehrávač
    player.play()  # Prehranie videa

# Nastavenie okna pomocou tkinter
root = tk.Tk()
root.title("YouTube Video Player")

# Vytvorenie vstupu pre URL videa
url_label = tk.Label(root, text="Enter YouTube Video URL:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Tlačidlo na prehrávanie videa
play_button = tk.Button(root, text="Play Video", command=play_video)
play_button.pack(pady=20)

# Nastavenie VLC pre prehrávanie videa
instance = vlc.Instance()  # Vytvorenie VLC inštancie
player = instance.media_player_new()  # Vytvorenie prehrávača

# Spustenie hlavnej slučky tkinter
root.mainloop()

