# import telebot
# from dotenv import load_dotenv
# import yt_dlp
# import os

# # 1. Load the environment variables from the .env file
# load_dotenv() 

# # 2. Get the token from the environment variables
# BOT_TOKEN = os.getenv("BOT_TOKEN")

# # 3. Initialize the bot using the token
# bot = telebot.TeleBot(BOT_TOKEN)

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     welcome_text = (
#         "👋 Welcome to the Video Downloader Bot!\n\n"
#         "Just paste a link, and I will send you the video.\n"
#         "Type /help to see detailed instructions and limitations."
#     )
#     bot.reply_to(message, welcome_text)

# @bot.message_handler(commands=['help'])
# def send_help(message):
#     help_text = (
#         "🛠️ *How to use this bot:*\n\n"
#         "1. Copy a video link from an app (YouTube, TikTok, X/Twitter, Instagram, etc.).\n"
#         "2. Paste the link into this chat and press send.\n"
#         "3. Wait a few moments while I download and process the video.\n\n"
#         "⚠️ *Important Limitations:*\n"
#         "• *File Size:* Telegram strictly limits bot uploads to *50MB*. If a video is too long or extremely high quality, I might not be able to send it.\n"
#         "• *Private Accounts:* I cannot download videos from private profiles, private groups, or age-restricted content.\n"
#         "• *Playlists:* I am currently set up to only download single videos, not entire playlists.\n\n"
#         "If you get an error, the video is likely too large or restricted!"
#     )
#     # Notice we added parse_mode='Markdown' here to make the text bold/italic!
#     bot.reply_to(message, help_text, parse_mode='Markdown')

# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     url = message.text.strip()
    
#     # Basic check to see if the message is a link
#     if not url.startswith('http'):
#         bot.reply_to(message, "Please send a valid URL starting with http or https.")
#         return

#     # Notify the user that the process has started
#     processing_msg = bot.reply_to(message, "⏳ Downloading video... this might take a minute.")

#     # Configure yt-dlp options
#     ydl_opts = {
#         # Try to get the best quality that is under Telegram's 50MB limit
#         'format': 'best[filesize<50M]/bestvideo[filesize<50M]+bestaudio/best', 
#         'outtmpl': 'downloaded_video_%(id)s.%(ext)s', # Save format
#         'noplaylist': True, # Don't download entire playlists
#         'quiet': True
#     }

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             # Extract info and download
#             info = ydl.extract_info(url, download=True)
#             # Get the exact filename it saved as
#             filename = ydl.prepare_filename(info)

#         # Send the video to the user
#         bot.edit_message_text("⬆️ Uploading to Telegram...", chat_id=message.chat.id, message_id=processing_msg.message_id)
        
#         with open(filename, 'rb') as video_file:
#             bot.send_video(message.chat.id, video_file)

#         # Clean up: delete the file from your computer/server after sending
#         os.remove(filename)
        
#         # Delete the "Uploading..." message
#         bot.delete_message(chat_id=message.chat.id, message_id=processing_msg.message_id)

#     except yt_dlp.utils.DownloadError:
#         bot.edit_message_text("❌ Error: Could not download the video. It might be private, restricted, or simply too large.", chat_id=message.chat.id, message_id=processing_msg.message_id)
#     except Exception as e:
#         bot.edit_message_text(f"❌ An unexpected error occurred: {str(e)}", chat_id=message.chat.id, message_id=processing_msg.message_id)

# print("Bot is running...")

# # This keeps the bot listening for new messages
# bot.infinity_polling()