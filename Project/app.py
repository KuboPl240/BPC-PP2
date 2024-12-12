from tkinter import *
from tkinter import messagebox
import song
import vlc
from pytubefix import YouTube
from pytubefix.cli import on_progress

class App:
    def __init__(self, root, songs, history, on_song_add, on_search):
        self.songs = songs
        self.history = history if history else songs
        self.root = root
        self.root.title("Song Collector")
        self.root.geometry("500x400")
        self.root.configure(bg="#2E2E2E")
        self.all_items = songs
        self.on_song_add = on_song_add
        self.on_search = on_search
        self.current_song = None

        self.bg_color = "#2E2E2E"
        self.fg_color = "#FFFFFF"
        self.entry_bg = "#3C3C3C"
        self.button_bg = "#4A4A4A"
        self.listbox_bg = "#3C3C3C"
        self.listbox_fg = "#FFFFFF"

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_suggestions)

        self.Entry = Entry(self.root, textvariable=self.search_var, width=40, bg=self.entry_bg, fg=self.fg_color)
        self.Entry.grid(row=0, column=0, pady=10, padx=10)

        self.search_button = Button(root, text="Search", command=self.handle_search_action, bg=self.button_bg, fg=self.fg_color)
        self.search_button.grid(row=0, column=1, pady=10, padx=10)

        self.add_button = Button(root, text="ADD", command=self.show_add_form, bg=self.button_bg, fg=self.fg_color)
        self.add_button.grid(row=0, column=2, pady=10, padx=10)

        self.suggestion_box = Listbox(self.root, width=50, height=10, bg=self.listbox_bg, fg=self.listbox_fg)
        self.suggestion_box.grid(row=1, column=0, columnspan=3, pady=10, padx=10)
        self.suggestion_box.bind("<<ListboxSelect>>", self.select_suggestion)

        self.details_label = Label(self.root, text="", bg=self.bg_color, fg=self.fg_color, justify=LEFT)
        self.details_label.grid(row=1, column=0, pady=10, padx=10)
        self.details_label.grid_remove()

        self.populate_suggestions(self.history)
        self.vlc_instance = vlc.Instance()
        self.vlc_player = self.vlc_instance.media_player_new()

        self.add_label_name = Label(root, text="New song name:", bg=self.bg_color, fg=self.fg_color)
        self.add_entry_name = Entry(root, width=40, bg=self.entry_bg, fg=self.fg_color)

        self.add_label_interpreter = Label(root, text="Interpreter:", bg=self.bg_color, fg=self.fg_color)
        self.add_entry_interpreter = Entry(root, width=40, bg=self.entry_bg, fg=self.fg_color)

        self.add_label_year = Label(root, text="Year of release:", bg=self.bg_color, fg=self.fg_color)
        self.add_entry_year = Entry(root, width=40, bg=self.entry_bg, fg=self.fg_color)

        self.add_label_link = Label(root, text="Link to a song:", bg=self.bg_color, fg=self.fg_color)
        self.add_entry_link = Entry(root, width=40, bg=self.entry_bg, fg=self.fg_color)

        self.save_button = Button(root, text="SAVE", command=self.add_song, bg=self.button_bg, fg=self.fg_color)
        self.back_button = Button(root, text="BACK", command=self.show_search_form, bg=self.button_bg, fg=self.fg_color)
        
        self.play_button = Button(root, text="Play", command=self.play_video, bg=self.button_bg, fg=self.fg_color)
        self.play_button.grid(row=4, column=1, pady=10, padx=10)
        self.play_button.grid_remove()

        self.stop_button = Button(root, text="Stop", command=self.stop_video, bg=self.button_bg, fg=self.fg_color)
        self.stop_button.grid(row=4, column=2, pady=10, padx=10)
        self.stop_button.grid_remove()

        self.volume_label = Label(self.root, text="Volume", bg=self.bg_color, fg=self.fg_color)
        self.volume_label.grid(row=5, column=0, pady=10, padx=10)
        self.volume_label.grid_remove()

        self.volume_slider = Scale(self.root, from_=0, to=100, orient='horizontal', command=self.adjust_volume, bg=self.bg_color, fg=self.fg_color)
        self.volume_slider.set(50)  
        self.volume_slider.grid(row=5, column=1, columnspan=2, pady=10, padx=10)
        self.volume_slider.grid_remove()



    def update_suggestions(self, *args):
        search_text = self.search_var.get().lower()
        if search_text:
            self.suggestion_box.delete(0, END)
            filtered = [item for item in self.all_items if search_text in str(item).lower()]
            for item in filtered:
                self.suggestion_box.insert(END, item)
            self.suggestion_box.grid()
            self.details_label.grid_remove()
        else:
            self.details_label.grid_remove()
            self.suggestion_box.grid()
            self.populate_suggestions(self.history)

    def select_suggestion(self, event):
        selected = self.suggestion_box.curselection()
        if selected:
            value = self.suggestion_box.get(selected[0])
            self.display_song_details(value)

    def handle_search_action(self):
        search_text = self.search_var.get().strip()
        filtered = [item for item in self.all_items if search_text.lower() in str(item).lower()]
        if filtered:
            self.display_song_details(filtered[0])
        else:
            self.suggestion_box.delete(0, END)
            self.suggestion_box.insert(END, "No matches found")

    def display_song_details(self, song):
        if isinstance(song, str): 
            song = next((s for s in self.all_items if str(s) == song), None)

        if song:  
            self.suggestion_box.grid_remove()
            self.on_search(song)
            self.current_song = song
            self.details_label.config(text=f"Song Name: {song.name}\n"
                                            f"Interpreter: {song.interpreter}\n"
                                            f"Year: {song.year}\n"
                                            f"Link: {song.link}")
            self.details_label.grid()
            self.play_button.grid()
        else:
            messagebox.showerror("Error", "Song details not found.")
            self.play_button.grid_remove()

    def populate_suggestions(self, songs):
        self.suggestion_box.delete(0, END)
        for item in songs:
            self.suggestion_box.insert(END, item)

    def show_search_form(self):
        self.hide_add_form()
        self.Entry.grid(row=0, column=0, pady=10, padx=10)
        self.search_button.grid(row=0, column=1, pady=10, padx=10)
        self.add_button.grid(row=0, column=2, pady=10, padx=10)
        self.suggestion_box.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

    def show_add_form(self):
        self.Entry.grid_remove()
        self.search_button.grid_remove()
        self.add_button.grid_remove()
        self.suggestion_box.grid_remove()
        self.details_label.grid_remove()
        self.play_button.grid_remove()
        self.add_label_name.grid(row=0, column=0, pady=10, padx=10)
        self.add_entry_name.grid(row=0, column=1, pady=10, padx=10)

        self.add_label_interpreter.grid(row=1, column=0, pady=10, padx=10)
        self.add_entry_interpreter.grid(row=1, column=1, pady=10, padx=10)

        self.add_label_year.grid(row=2, column=0, pady=10, padx=10)
        self.add_entry_year.grid(row=2, column=1, pady=10, padx=10)

        self.add_label_link.grid(row=3, column=0, pady=10, padx=10)
        self.add_entry_link.grid(row=3, column=1, pady=10, padx=10)

        self.save_button.grid(row=4, column=1, pady=10, padx=10)
        self.back_button.grid(row=4, column=0, pady=10, padx=10)

    def hide_add_form(self):
        self.add_label_name.grid_remove()
        self.add_entry_name.grid_remove()
        self.add_label_interpreter.grid_remove()
        self.add_entry_interpreter.grid_remove()
        self.add_label_year.grid_remove()
        self.add_entry_year.grid_remove()
        self.add_label_link.grid_remove()
        self.add_entry_link.grid_remove()
        self.save_button.grid_remove()
        self.back_button.grid_remove()

    def add_song(self):
        new_song = self.add_entry_name.get().strip()
        interpreter = self.add_entry_interpreter.get().strip()
        year = self.add_entry_year.get().strip()
        link = self.add_entry_link.get().strip()
        try:
            if not new_song:
                raise ValueError("The song name field is empty.")
            if not interpreter:
                raise ValueError("The interpreter field is empty.")
            if not year:
                raise ValueError("The year field is empty.")
        except Exception as e:
            self.handle_exception(e)
        else:
            new_entry = Song(new_song, interpreter, year, link)
            self.on_song_add(new_entry)
            self.populate_suggestions(self.history)
            self.add_entry_name.delete(0, END)
            self.add_entry_interpreter.delete(0, END)
            self.add_entry_year.delete(0, END)
            self.add_entry_link.delete(0, END)
            self.show_search_form()

    def handle_exception(self, exception):
        messagebox.showerror("Error", f"{str(exception)}")
        return

    def get_video_url(self):
        """Získa URL videa aktuálnej pesničky."""
        if self.current_song and hasattr(self.current_song, "link"):
            return self.current_song.link
        return None

    def play_video(self):
        """Prehrá pesničku otvorením URL cez VLC."""
        self.stop_button.grid()
        self.volume_slider.grid()
        self.volume_label.grid()
        video_url = self.get_video_url()
        if video_url:
            try:
                yt = YouTube(video_url, on_progress_callback=on_progress)
                stream_url = yt.streams.get_highest_resolution().url
                media = self.vlc_instance.media_new(stream_url)
                self.vlc_player.set_media(media)
                self.vlc_player.play()
                self.vlc_player.audio_set_volume(self.volume_slider.get())
            except Exception as e:
                messagebox.showerror("Error", f"Failed to play video: {e}")
        else:
            messagebox.showerror("Error", "No valid link to play the song.")
    
    def stop_video(self):
        self.vlc_player.stop()
        self.stop_button.grid_remove()
        self.volume_slider.grid_remove()
        self.volume_label.grid_remove()

    def adjust_volume(self, val):
        volume = int(val)
        self.vlc_player.audio_set_volume(volume)