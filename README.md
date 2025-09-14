# Micande Remote Bot

A Telegram bot for remote computer control. Control your PC from anywhere using simple Telegram commands.

## Features

- **Camera Photo** - Take photos using webcam
- **Video Recording** - Record 30-second videos from camera  
-  **Screenshot** - Capture current screen
- **Lock Screen** - Lock your computer
- **Shutdown** - Turn off computer remotely
-  **Restart** - Reboot your system
- **Minimize** - Minimize all windows

## Supported Systems

-  Windows
-  Linux  
-  macOS

## Installation

### 1. Install Dependencies
```bash
pip install opencv-python pyTelegramBotAPI pyautogui Pillow
```

### 2. Get Bot Token
1. Go to [@BotFather](https://t.me/BotFather) in Telegram
2. Create new bot with `/newbot`
3. Copy the token

### 3. Get Your Chat ID
1. Go to [@micandeId_bot](https://t.me/micandeId_bot)
2. Send any message to get your chat ID

### 4. Configure
Edit `option.py` file:
```python
token = "YOUR_BOT_TOKEN_HERE"     # Replace with your bot token
user_id = 123456789               # Replace with your chat ID
```

### 5. Run
```bash
python bot.py
```

## Commands

- `/photo` - Take webcam photo
- `/screenshot` - Take screenshot
- `/record` - Record 30s video
- `/lock` - Lock computer
- `/shutdown` - Shutdown computer
- `/restart` - Restart computer
- `/minimize` - Minimize all windows

## Security

- Only authorized user (specified in `user_id`) can control the bot
- Bot ignores all other users
- No data is stored or logged

## Requirements

- Python 3.7+
- Webcam for photo/video features
- Internet connection
- Telegram account

## Disclaimer

This tool is for educational purposes and authorized use only. Use responsibly and only on computers you own or have permission to control.

## Author

Created by micande(https://micande.site/)

## License

This project is open source and available under the MIT License.
