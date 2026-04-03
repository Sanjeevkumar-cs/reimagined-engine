# 🎬 Telegram Video Downloader Bot

A simple and highly effective Telegram bot built with Python that downloads videos from platforms like YouTube, TikTok, X (Twitter), and Instagram, and sends the actual video file directly to your Telegram chat.

Powered by `yt-dlp` and `pyTelegramBotAPI`, this bot acts as your personal media fetcher, ensuring you don't have to visit sketchy downloader websites to save your favorite clips.

## ✨ Features

- **Direct File Delivery:** Delivers the actual `.mp4` video file straight to the Telegram chat.
- **Smart Quality Selection:** Automatically fetches the best possible video quality that fits within Telegram's strict 50MB bot upload limit.
- **Auto-Cleanup:** Automatically deletes the video from the host computer's hard drive after sending it to Telegram to save storage space.
- **Multi-Platform Support:** Works seamlessly with hundreds of websites supported by `yt-dlp`.

## 🛠️ Prerequisites

Before running this bot, ensure you have the following installed on your machine:

- **Python 3.8+**
- **Node.js** (Crucial: Required by `yt-dlp` to solve YouTube's anti-bot JavaScript challenges in the background).

## 🚀 Installation & Setup

**1. Clone the repository:**

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
```
*(Remember to change the `YOUR_USERNAME` and `YOUR_REPO_NAME` placeholders in the clone link before saving!)*

---
## ⚠️ Disclaimer
This project is for educational purposes only. Downloading content from third-party platforms may violate their Terms of Service and copyright laws. The repository owner assumes no responsibility for how this tool is used by individuals. Please respect the rights of content creators.
