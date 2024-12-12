from tkinter import Tk
from tkinter import messagebox
from app import App
import song
import json


history = []
songs = []

def load_songs_from_json():
    try:
        with open('songs.json', 'r', encoding='utf-8') as file:
            content = file.read().strip()  
            print(file.read())
            if not content:  
                raise ValueError("File is empty.")
            loaded_data = json.loads(content)  
    except json.JSONDecodeError as e:
        messagebox.showerror("Erorr",f"Cannot read file with songs {e}")
    except ValueError as e:
        messagebox.showerror("Erorr",f"Cannot read file with songs. {e}")
    else:
        for item in loaded_data["Songs"]:
            track = song.Song(item['name'],item['interpreter'],item['year'],item['link'])
            songs.append(track)
    return songs

def save_songs_to_json(song_list):
    songs_data = {"Songs": [song.to_json() for song in song_list]}
    with open("songs.json", "w", encoding="utf-8") as file:
        json.dump(songs_data, file, ensure_ascii=False, indent=4)

def load_search_history_from_json():
    songs_history = []
    try:
        with open('search_history.json', 'r', encoding='utf-8') as file:
            content = file.read().strip() 
            if not content:  
                raise ValueError("File is empty.")
            loaded_data = json.loads(content)  
    except json.JSONDecodeError as e:
        messagebox.showerror("Erorr",f"Cannot read file with search history. {e}")
    except ValueError as e:
        messagebox.showerror("Erorr",f"Cannot read file with search history. {e}")
    else:
        for item in loaded_data:
            for song in songs:
                if song.get_name() == item:
                    songs_history.append(song)
    songs_history=list(set(songs_history))
    print(songs_history)
    return list(reversed(songs_history))

def handle_new_song(song):
    try:
        for track in songs:
            if track == song:
               raise Exception("Song is already in database") 
        print(f"New song added: {song}")
    except Exception as e:
        app.handle_exception(e)
    else:
        songs.append(song)
        save_songs_to_json(songs)

def search_song(song):
    global history 
    if song not in history:
        history.insert(0, song)
        history=list(set(history))
    try:
        with open('search_history.json', 'r') as file:
            search_history = json.load(file)
    except:
        app.handle_exception("Cannot read file with search history, creating a new one.")
        search_history = []
    search_history.append(song.get_name())
    with open('search_history.json', 'w') as file:
        json.dump(search_history, file, indent=4)
    

if __name__ == "__main__":
    root = Tk()
    songs = load_songs_from_json()
    history = load_search_history_from_json()
    app = App(root, songs, history, handle_new_song, search_song)
    root.mainloop()






