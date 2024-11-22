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
def discordInterner():
    webbrowser.open("https://discord.com/app")

def instagramInterner():
    webbrowser.open("https://www.instagram.com")

def steamInternet():
    webbrowser.open("https://store.steampowered.com")

def telegramInterner():
    webbrowser.open("https://web.telegram.org/a/")

def tikTokInterner():
    webbrowser.open("https://www.tiktok.com/")

def twitchInterner():
    webbrowser.open("https://www.twitch.tv")

def youTubeInterner():
    webbrowser.open("https://www.youtube.com")

# Функции для работы с Google сервисами
def googleDisk():
    webbrowser.open("https://drive.google.com/drive/")

def google():
    webbrowser.open("https://www.google.com")

def googleGmail():
    webbrowser.open("https://mail.google.com")

def googlePhoto():
    webbrowser.open("https://photos.google.com")

def googleTranstale():
    webbrowser.open("https://translate.google.com")

# Функции для работы с AI сервисами
def chatGPT():
    webbrowser.open("https://chat.openai.com")

def copilot():
    webbrowser.open("https://copilot.microsoft.com")

def leonardo():
    webbrowser.open("https://app.leonardo.ai")


#Разное
def catk():
    import tkinter as tk
    from tkinter import messagebox

    def on_click(button_text):
        if button_text == "=":
            try:
                result = eval(entry.get())
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Ошибка", "Неверное выражение!")
        elif button_text == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, button_text)

    # Создание главного окна
    root = tk.Tk()
    root.title("Калькулятор")
    root.resizable(False, False)

    # Поле ввода
    entry = tk.Entry(root, width=20, font=("Arial", 18), justify="right")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Кнопки калькулятора
    buttons = [
        "7", "8", "9", "+",
        "4", "5", "6", "-",
        "1", "2", "3", "*",
        "C", "0", "=", "/"
    ]

    # Создание кнопок
    row = 1
    col = 0
    for button_text in buttons:
        button = tk.Button(root, text=button_text, font=("Arial", 18), width=5, height=2,
                           command=lambda bt=button_text: on_click(bt))
        button.grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 3:
            col = 0
            row += 1

    # Запуск главного цикла
    root.mainloop()


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
        MenuItem("Разное", more),
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

#Меню для разного
more = Menu(
    MenuItem("Калькулятор", catk),
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
