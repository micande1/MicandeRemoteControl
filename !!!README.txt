# Telegram Bot Setup Instructions

## IMPORTANT!!!
THE BOT WILL NOT WORK IF YOU DON'T FOLLOW THESE INSTRUCTIONS:

### Library Installation  
Before starting, you need to install libraries: "opencv-python", "pyTelegramBotAPI", "pyautogui", "Pillow".
```
pip install opencv-python pyTelegramBotAPI pyautogui Pillow
```

### Configuration

1. To get the token go to @BotFather in telegram and create a bot using /newbot. Then insert the token you receive into the option.py file

2. You need to get CHAT_ID which you can find out using my bot @micandeId_bot. This id needs to be inserted into option.py in the AUTHORIZED_CHAT_ID variable.

3. Run it and get your ready bot.

### Additional important points:

- Make sure Python has permissions to take screenshots
- Better to use virtual environment to avoid conflicts  
- Check that firewall doesn't block connections to telegram API
- Need Python version 3.7 or higher
- Never show your bot token to other people
- If you have import errors try updating pip

---

# Инструкция по настройке Telegram бота

## ВАЖНО!!!
БОТ НЕ БУДЕТ РАБОТАТЬ ЕСЛИ ВЫ НЕ СДЕЛАЕТЕ ТО ЧТО ЗДЕСЬ НАПИСАНО:

### Установка библиотек
Перед началом нужно установить библиотеки: "opencv-python", "pyTelegramBotAPI", "pyautogui", "Pillow".
```
pip install opencv-python pyTelegramBotAPI pyautogui Pillow
```

### Настройка

1. Получение токена нужно зайти в @BotFather в телеграмме и создать бота через /newbot. Дальше токен который мы получаем нужно вставить в файл option.py

2. Нужно получить CHAT_ID который можно узнать с помощью моего бота @micandeId_bot. Этот id нужно вставить в option.py в переменную AUTHORIZED_CHAT_ID.

3. Запускаем и получаем готового бота.

### Дополнительные важные моменты:

- Убедитесь что у питона есть права на создание скриншотов
- Лучше использовать виртуальное окружение чтобы не было конфликтов
- Проверьте что файрвол не блокирует соединения к телеграм API
- Нужен Python версии 3.7 или выше
- Никогда не показывайте токен бота другим людям
- Если есть ошибки с импортом то попробуйте обновить pip