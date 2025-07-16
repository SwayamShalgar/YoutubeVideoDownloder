import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import yt_dlp
import os
import shutil

def get_ffmpeg_path():
    # Try to locate ffmpeg in PATH or common folders
    path = shutil.which("ffmpeg")
    if path:
        return path
    # fallback (custom path if installed manually)
    fallback_path = "C:/ffmpeg-7.1.1-essentials_build/ffmpeg.exe"  # CHANGE THIS!
    return fallback_path if os.path.exists(fallback_path) else None

def fetch_available_qualities():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Missing URL", "Paste the YouTube link first!")
        return

    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            resolutions = sorted(set(
                str(fmt.get('height')) + 'p'
                for fmt in formats
                if fmt.get('vcodec') != 'none' and fmt.get('height') is not None
            ), key=lambda x: int(x.replace('p', '')), reverse=True)

            quality_menu['values'] = resolutions
            if resolutions:
                quality_var.set(resolutions[0])  # Set to highest
            else:
                quality_var.set("360p")
                quality_menu['values'] = ["360p"]
    except Exception as e:
        messagebox.showerror("Error fetching qualities", str(e))

def download_video():
    url = url_entry.get().strip()
    quality = quality_var.get().replace('p', '')
    path = path_var.get().strip()
    ffmpeg_path = get_ffmpeg_path()

    if not url or not path:
        messagebox.showerror("Missing Info", "Provide both URL and save path.")
        return
    if not ffmpeg_path:
        messagebox.showerror("FFmpeg Error", "FFmpeg not found! Please install it or add to PATH.")
        return

    ydl_opts = {
        'format': f"bestvideo[height={quality}]+bestaudio/best",
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'ffmpeg_location': ffmpeg_path,
        'noplaylist': True,
        'quiet': True,
        'progress_hooks': [progress_hook]
    }

    try:
        status_var.set("⏳ Downloading...")
        root.update()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        status_var.set("✅ Download Complete!")
    except Exception as e:
        status_var.set(f"❌ Error: {e}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_var.set(folder_selected)

def progress_hook(d):
    if d['status'] == 'downloading':
        status_var.set(f"⬇️ {d['_percent_str']} @ {d['_speed_str']}")
    elif d['status'] == 'finished':
        status_var.set("🔧 Merging video & audio...")

# GUI setup
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("550x370")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TCombobox", fieldbackground="#2e2e2e", background="#2e2e2e", foreground="#ffffff")

ttk.Label(root, text="YouTube URL:").pack(pady=(15, 5))
url_entry = ttk.Entry(root, width=70)
url_entry.pack()

ttk.Button(root, text="🔍 Get Available Qualities", command=fetch_available_qualities).pack(pady=(8, 8))

ttk.Label(root, text="Select Quality:").pack(pady=(5, 5))
quality_var = tk.StringVar()
quality_menu = ttk.Combobox(root, textvariable=quality_var, values=[], state="readonly")
quality_menu.pack()

ttk.Label(root, text="Save Folder:").pack(pady=(15, 5))
path_frame = ttk.Frame(root)
path_frame.pack()
path_var = tk.StringVar()
path_entry = ttk.Entry(path_frame, textvariable=path_var, width=50)
path_entry.pack(side=tk.LEFT, padx=(0, 10))
ttk.Button(path_frame, text="Browse", command=browse_folder).pack(side=tk.LEFT)

ttk.Button(root, text="🚀 Download", command=download_video).pack(pady=20)

status_var = tk.StringVar()
ttk.Label(root, textvariable=status_var, font=("Consolas", 10), foreground="#00ff99").pack()

root.mainloop()
