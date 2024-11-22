from PIL import Image
import requests
from io import BytesIO
import sys
import os
import webbrowser
import json
from pystray import Icon, Menu, MenuItem
import tkinter as tk


# Путь к папке с настройками
settings_folder = "C:\\Rodger"
settings_file = os.path.join(settings_folder, "settings.json")

# Функции для работы с интернет-ресурсами
def discordInterner(icon, item):
    webbrowser.open("https://discord.com/app")

def instagramInterner(icon, item):
    webbrowser.open("https://www.instagram.com")

def steamInternet(icon, item):
    webbrowser.open("https://store.steampowered.com")

def telegramInterner(icon, item):
    webbrowser.open("https://web.telegram.org/a/")

def tikTokInterner(icon, item):
    webbrowser.open("https://www.tiktok.com/")

def twitchInterner(icon, item):
    webbrowser.open("https://www.twitch.tv")

def youTubeInterner(icon, item):
    webbrowser.open("https://www.youtube.com")

# Функции для работы с Google сервисами
def googleDisk(icon, item):
    webbrowser.open("https://drive.google.com/drive/")

def google(icon, item):
    webbrowser.open("https://www.google.com")

def googleGmail(icon, item):
    webbrowser.open("https://mail.google.com")

def googlePhoto(icon, item):
    webbrowser.open("https://photos.google.com")

def googleTranstale(icon, item):
    webbrowser.open("https://translate.google.com")

# Функции для работы с AI сервисами
def chatGPT(icon, item):
    webbrowser.open("https://chat.openai.com")

def copilot(icon, item):
    webbrowser.open("https://copilot.microsoft.com")

def leonardo(icon, item):
    webbrowser.open("https://app.leonardo.ai")

"""
def ThAT(icon, item):
    a = tk.Tk()
    a.title("ЧеГО?")
    a.geometry("500x700")
    a.resizable(False, False)

    t1 = tk.Label(text="Для чего она?")
    t1.pack()
    t1 = tk.Label(text="")
    t1.pack()
    t1 = tk.Label(text="")
    t1.pack()


    a.mainloop()
"""

# Получение публичного IP
def fetch_public_ip():
    try:
        response = requests.get("https://api.ipify.org")
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return "Ошибка получения IP"

# Загрузка изображения для иконки
image_url = "https://cdn.icon-icons.com/icons2/640/PNG/512/windows-desktop-os-software_icon-icons.com_59116.png"
try:
    response = requests.get(image_url)
    response.raise_for_status()
    icon_image = Image.open(BytesIO(response.content)).resize((64, 64))
except requests.RequestException as e:
    print(f"Ошибка загрузки изображения: {e}")
    sys.exit(1)
except FileNotFoundError:
    print(f"Ошибка: Файл {image_url} не найден.")
    sys.exit(1)

# Проверка и создание папки для настроек
if not os.path.exists(settings_folder):
    os.makedirs(settings_folder)
    os.system('attrib +h "C:\\Rodger"')


# Загрузка или создание файла настроек
def load_settings():
    if os.path.exists(settings_file):
        with open(settings_file, "r") as file:
            return json.load(file)
    else:
        return {"show_ip": True}  # Если файл настроек не существует, возвращаем настройки по умолчанию


# Сохранение настроек в файл
def save_settings(settings):
    with open(settings_file, "w") as file:
        json.dump(settings, file)

# Строим меню
def build_menu_with_ip():
    # Если show_ip == True, то показываем IP, иначе скрываем
    ip_item_text = f"Ваш IP: {fetch_public_ip()}" if settings["show_ip"] else "Ваш IP: скрыт"
    return Menu(
        MenuItem("----------------------", lambda icon, item: None, enabled=False),
        MenuItem("           Rodger", lambda icon, item: None, enabled=False),
        MenuItem("----------------------", lambda icon, item: None, enabled=False),
        MenuItem(ip_item_text, lambda icon, item: None, enabled=False),
        MenuItem("Открыть в интернете:", workOnInternet),
        MenuItem("Настройки", settinks),
        MenuItem("Выход", lambda icon, item: icon.stop())
    )

# Меню для AI сервисов
allAI = Menu(
    MenuItem("Chat GPT", chatGPT),
    MenuItem("Copilot", copilot),
    MenuItem("Leonardo", leonardo),
)

# Меню для Google сервисов
allGoogle = Menu(
    MenuItem("Disk", googleDisk),
    MenuItem("Google", google),
    MenuItem("Gmail", googleGmail),
    MenuItem("Photo", googlePhoto),
    MenuItem("Translate", googleTranstale),
)

# Меню для настройки интернет-ресурсов
workOnInternet = Menu(
    MenuItem("AI", allAI),
    MenuItem("Discord", discordInterner),
    MenuItem("Instagram", instagramInterner),
    MenuItem("Google", allGoogle),
    MenuItem("Steam", steamInternet),
    MenuItem("Telegram", telegramInterner),
    MenuItem("TikTok", tikTokInterner),
    MenuItem("Twitch", twitchInterner),
    MenuItem("YouTube", youTubeInterner),
)

# Меню для настроек
def toggle_ip_visibility(icon, item):
    settings["show_ip"] = not settings["show_ip"]  # Переключаем состояние
    save_settings(settings)  # Сохраняем изменения в файл
    icon.menu = build_menu_with_ip()  # Обновляем меню
    icon.update_menu()  # Обновляем меню иконки

settinks = Menu(
    MenuItem("Скрыть/Показать IP", toggle_ip_visibility),
    #MenuItem("О чем программа?", ThAT),
)

# Загрузка настроек при старте
settings = load_settings()

# Запуск иконки с меню
icon = Icon(
    "Roger",
    icon_image,
    menu=build_menu_with_ip()
)

# Запуск иконки
icon.run()
