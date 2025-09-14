import cv2
import telebot 
import time
from telebot import types
from datetime import datetime
import os
import platform
import pyautogui
from PIL import ImageGrab  
from option import token
from option import user_id
pyautogui.FAILSAFE = False 
TOKEN = token
AUTHORIZED_CHAT_ID = user_id
bot = telebot.TeleBot(TOKEN)

def system_command():
    system = platform.system()
    if system == "Windows":
        return {
            'lockscreen': "rundll32.exe user32.dll,LockWorkStation",
            'shutdown': "shutdown /s /t 0",
            'reboot': "shutdown /r /t 0",
            "modifier_key": "winleft"
        }
    elif system == "Linux":
        return {
            'lockscreen': "loginctl lock-session",
            'shutdown': "sudo shutdown -h now",
            'reboot': "sudo reboot",
            'modifier_key': "super"
        }
    elif system == "Darwin":
        return {
            'lockscreen': "pmset displaysleepnow",
            'shutdown': "sudo shutdown -h now",
            'reboot': "sudo reboot",
            'modifier_key': 'cmd'
        }
    
commands = system_command()
    
def send_camera_photo(chat_id):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        filename = f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        cv2.imwrite(filename, frame)
        with open(filename, 'rb') as photo:
            bot.send_photo(chat_id, photo)
        os.remove(filename)
    cap.release()

def send_camera_video(chat_id):
    cam = cv2.VideoCapture(0)
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    filename = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    out = cv2.VideoWriter(filename, fourcc, 20.0, (frame_width, frame_height)) 
    start_time = time.time()
    duration = 30
    while True:
         ret, frame = cam.read()
         if not ret:
            break
         out.write(frame)
         if time.time() - start_time > duration:
              break
    cam.release()
    out.release()

    with open(filename, 'rb') as video: 
         bot.send_video(chat_id, video)
    os.remove(filename)


def send_screenshot(chat_id):
    screenshot = ImageGrab.grab()
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    screenshot.save(filename)
    with open(filename, 'rb') as photo:
        bot.send_photo(chat_id, photo)
    os.remove(filename)

def send_keyboard(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_photo = types.KeyboardButton("/photo")
    bth_video = types.KeyboardButton("/record")
    btn_screenshot = types.KeyboardButton("/screenshot")
    btn_shutdown = types.KeyboardButton("/shutdown")
    btn_lockscreen = types.KeyboardButton("/lock")
    btn_reboot = types.KeyboardButton("/restart")
    btn_homescreen = types.KeyboardButton("/minimize")
    markup.add(btn_photo, btn_screenshot, btn_shutdown,btn_lockscreen,btn_reboot,bth_video,btn_homescreen)
    bot.send_message(chat_id, "Action:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.chat.id != AUTHORIZED_CHAT_ID:
        return  

    if message.text in [ "/photo"]:
            send_camera_photo(message.chat.id)
    elif message.text in ["/screenshot"]:
            send_screenshot(message.chat.id)
    elif message.text in ["/lock"]:
            bot.send_message(message.chat.id, "Locking...")
            os.system(commands['lockscreen'])
    elif message.text in ["/shutdown"]:
            bot.send_message(message.chat.id, "Shutting down...")
            os.system(commands['shutdown'])
    elif message.text in ["/restart"]:
            bot.send_message(message.chat.id,"Restarting...")
            os.system(commands['reboot'])
    elif message.text in ["/record"]:
        send_camera_video(message.chat.id)
    elif message.text in ["/minimize"]:
            bot.send_message(message.chat.id, "Minimizing...")
            pyautogui.hotkey(commands['modifier_key'], 'd')
    else:
        send_keyboard(message.chat.id)


send_camera_photo(AUTHORIZED_CHAT_ID)
send_keyboard(AUTHORIZED_CHAT_ID)
bot.polling()
