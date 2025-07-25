
# 🎬 YouTube Video Downloader - GUI App

This is a powerful, clean, and user-friendly desktop app that downloads YouTube videos in high quality.

> No ads.  
> No shady browser extensions.  
> Just Python, power, and pixels. 😎

---

## 💡 Features

- 🔗 Paste any YouTube link
- 🎯 Fetches actual available video resolutions (360p, 720p, 1080p+)
- ✅ Choose the quality YOU want
- 💾 Choose where to save the file
- 🎞️ Merges high-quality video + audio using `FFmpeg`
- 🔥 Built with tkinter (dark-mode GUI)
- 📡 Live status updates during download

---

## 🔧 Requirements

- 🐍 Python 3.7 or above  
- 📥 [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
- 🎞️ [FFmpeg](https://ffmpeg.org/download.html)

---

## 🚀 Installation & Setup

### 1. Clone the Project

```bash
git clone https://github.com/yourusername/youtube-downloader-gui.git
cd youtube-downloader-gui
```

Or download the ZIP and extract it.

---

### 2. Install Python Requirements

```bash
pip install yt-dlp
```

(Optional: Set up a virtual environment)

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate       # macOS/Linux
```

---

### 3. Install FFmpeg (Required!)

> ⚠️ FFmpeg is needed to merge video and audio in HD downloads like 720p, 1080p.

#### Option A: Add to System PATH ✅

1. Download from https://ffmpeg.org/download.html  
2. Extract it  
3. Add the `bin` folder (e.g., `C:\ffmpeg\bin`) to your **System Environment Variables > PATH**

#### Option B: Hardcode the Path in Code

Edit `main.py` and set:

```python
'ffmpeg_location': 'C:/Your/Actual/Path/ffmpeg.exe'
```

---

## ▶️ Run the App

```bash
python main.py
```

The GUI will open:

- Paste your YouTube URL  
- Click "Get Available Qualities"  
- Choose resolution  
- Select save folder  
- Click 💥 **Download**

Done!

---

## 🛠 Optional: Build as `.exe`

Make it portable!

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile main.py
```

Final `.exe` will be in the `/dist/` folder.

---

## 🧪 Troubleshooting

| Issue | Solution |
|-------|----------|
| ❌ FFmpeg not found | Add it to PATH or set correct location in code |
| ❌ “Best” quality fails | Select a resolution manually from dropdown |
| ❌ App crashes on high-res | Make sure FFmpeg is installed correctly |
| ❌ Slow speed | yt-dlp depends on your internet |

---

## 🧠 Future Upgrades

- 🔄 Playlist downloader  
- 🎵 Audio-only (MP3) mode  
- 💬 Subtitle + metadata support  
- 🎨 Dark/light theme toggle  
- 🧾 History + logging system

---

## 🧙 Author

Made with caffeine, frustration, and a bit of energy by [Swayam](https://github.com/SwayamShalgar)

> _“I didn’t feel like paying YouTube Premium. So I coded my own.”_

---

## 🏷️ Tags

`#Python` `#yt-dlp` `#FFmpeg` `#tkinter` `#YouTubeDownloader` `#OpenSource` `#GUIApp`
