import os
import tkinter as tk
from tkinter import filedialog, messagebox
from bookmarks_analyzer import extract_urls_from_bookmarks, categorize_url

class BookmarkScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bookmark Scanner")

        self.directory = tk.StringVar()
        self.url_list = []
        self.history = []
        self.history_index = -1

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        self.dir_label = tk.Label(frame, text="Selecciona el directorio de bookmarks:")
        self.dir_label.pack(anchor='w')

        self.dir_entry = tk.Entry(frame, textvariable=self.directory, width=50)
        self.dir_entry.pack(anchor='w')

        self.browse_button = tk.Button(frame, text="Examinar", command=self.browse_directory)
        self.browse_button.pack(anchor='w')

        self.scan_button = tk.Button(frame, text="Escanear", command=self.scan_directory)
        self.scan_button.pack(anchor='w')

        self.url_count_label = tk.Label(frame, text="Cantidad de URLs: 0")
        self.url_count_label.pack(anchor='w')

        self.url_type_label = tk.Label(frame, text="Tipos de URLs:")
        self.url_type_label.pack(anchor='w')

        self.url_listbox = tk.Listbox(frame, width=50, height=15)
        self.url_listbox.pack(anchor='w')

        self.navigation_frame = tk.Frame(self.root)
        self.navigation_frame.pack(padx=10, pady=10)

        self.back_button = tk.Button(self.navigation_frame, text="Atrás", command=self.back)
        self.back_button.grid(row=0, column=0, padx=5)

        self.forward_button = tk.Button(self.navigation_frame, text="Adelante", command=self.forward)
        self.forward_button.grid(row=0, column=1, padx=5)

        self.home_button = tk.Button(self.navigation_frame, text="Inicio", command=self.home)
        self.home_button.grid(row=0, column=2, padx=5)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory.set(directory)

    def scan_directory(self):
        directory = self.directory.get()
        if not os.path.isdir(directory):
            messagebox.showerror("Error", "Directorio no válido")
            return

        self.url_list.clear()
        for root, _, files in os.walk(directory):
            for file in files:
                if 'bookmark' in file.lower() or 'marcador' in file.lower():
                    file_path = os.path.join(root, file)
                    urls = extract_urls_from_bookmarks(file_path)
                    self.url_list.extend(urls)

        # Reset history and add current list
        self.history = [self.url_list.copy()]
        self.history_index = 0

        self.update_ui()

    def update_ui(self):
        self.url_listbox.delete(0, tk.END)
        url_counts = {'video': 0, 'text': 0}
        for url in self.history[self.history_index]:
            self.url_listbox.insert(tk.END, url)
            url_type = categorize_url(url)
            url_counts[url_type] += 1
        self.url_count_label.config(text=f"Cantidad de URLs: {len(self.history[self.history_index])}")
        self.url_type_label.config(text=f"Videos: {url_counts['video']}, Textos: {url_counts['text']}")

    def back(self):
        if self.history_index > 0:
            self.history_index -= 1
            self.update_ui()

    def forward(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.update_ui()

    def home(self):
        if self.history_index != 0:
            self.history_index = 0
            self.update_ui()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookmarkScannerApp(root)
    root.mainloop()
